"""Run with AKU_TEST_ROOT set to an approved scratch directory; no implicit /tmp."""
import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location("brain", Path(__file__).resolve().parents[1] / "scripts/brain.py")
brain = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(brain)


class BrainTests(unittest.TestCase):
    def setUp(self):
        scratch = Path(os.environ["AKU_TEST_ROOT"]).resolve(strict=True)
        self.temp = tempfile.TemporaryDirectory(dir=scratch, prefix="aku-test-")
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.root = self.base / "data"
        with contextlib.redirect_stdout(io.StringIO()):
            brain.init(self.root)

    def test_init_preserves_existing_notes_and_config(self):
        note = self.root / "vault/00_Start/Start.md"
        note.write_text("User correction", encoding="utf-8")
        with contextlib.redirect_stdout(io.StringIO()):
            brain.init(self.root)
        self.assertEqual(note.read_text(encoding="utf-8"), "User correction")
        self.assertFalse(brain.config(self.root)["sync"]["enabled"])

    def test_repo_data_overlap_and_missing_volume_rejected(self):
        for value in (brain.REPO / "data", brain.REPO.parent, Path("/Volumes/aku-test-volume-definitely-not-mounted/data")):
            with self.assertRaises(ValueError):
                brain.root_path(str(value))

    def test_nonempty_unowned_folder_is_not_initialized(self):
        target = self.base / "existing"
        target.mkdir()
        (target / "important.txt").write_text("keep", encoding="utf-8")
        with self.assertRaises(ValueError):
            brain.init(target)
        self.assertEqual((target / "important.txt").read_text(), "keep")

    def test_symlink_cannot_escape_data_root(self):
        (self.root / "escape").symlink_to(self.base, target_is_directory=True)
        with self.assertRaises(ValueError):
            brain.child(self.root, "escape/other.txt")
        pointer = self.root / "work/audio.partial.wav"
        pointer.symlink_to(self.base / "outside.wav")
        with self.assertRaises(ValueError):
            brain.safe_output(pointer, self.root)

    def fixture(self):
        job = self.root / "work/jobs/synthetic"
        (job / "frames").mkdir(parents=True)
        (job / "clips").mkdir()
        (job / "frames/frame_000000.jpg").write_bytes(b"synthetic fixture")
        (job / "clips/clip_00000.mp4").write_bytes(b"synthetic fixture")
        media = self.root / "media/synthetic"
        media.mkdir()
        (media / "source.mp4").write_bytes(b"synthetic fixture")
        manifest = {"duration_seconds": 1.2, "has_audio": False, "stage": "prepared", "source_relpath": "media/synthetic/source.mp4"}
        brain.save_json(job / "manifest.json", manifest)
        brain.save_json(job / "frames.done.json", {"count": 1})
        brain.save_json(job / "clips.json", [{"path": "work/jobs/synthetic/clips/clip_00000.mp4"}])
        rows = [{"start": i, "end": min(1.2, i + 1), "gaps": [], "evidence": {}, **{k: False for k in brain.MODALITIES}} for i in range(2)]
        self.write_rows(job, rows)
        return job, rows

    def write_rows(self, job, rows):
        (job / "coverage.jsonl").write_text("".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8")

    def coverage(self):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            code = brain.check_coverage(self.root, "synthetic")
        return code, json.loads(output.getvalue())

    def test_unreviewed_and_unsubstantiated_flags_are_partial(self):
        job, rows = self.fixture()
        self.assertEqual(self.coverage()[0], 2)
        for row in rows:
            row.update({k: True for k in brain.MODALITIES})
        self.write_rows(job, rows)
        self.assertEqual(self.coverage()[0], 2)

    def test_documentation_grid_gaps_and_missing_files(self):
        job, rows = self.fixture()
        for row in rows:
            for field in brain.MODALITIES:
                row[field] = True
                row["evidence"][field] = {"source": "synthetic fixture", "method": "unit test", "reviewer": "test"}
        self.write_rows(job, rows)
        self.assertEqual(self.coverage()[0], 0)
        rows[1]["start"] = 0
        self.write_rows(job, rows)
        self.assertEqual(self.coverage()[0], 2)
        rows[1]["start"] = 1
        rows[0]["gaps"] = ["unintelligible"]
        self.write_rows(job, rows)
        self.assertEqual(self.coverage()[0], 2)
        rows[0]["gaps"] = []
        self.write_rows(job, rows)
        (job / "clips/clip_00000.mp4").unlink()
        self.assertEqual(self.coverage()[0], 2)

    @unittest.skipUnless(shutil.which("ffmpeg"), "FFmpeg unavailable")
    def test_synthetic_video_preparation_resume_and_missing_artifact(self):
        source = self.base / "synthetic.mp4"
        env = brain.env_for(self.root)
        subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-nostdin",
                        "-f", "lavfi", "-i", "testsrc2=size=160x90:rate=24",
                        "-f", "lavfi", "-i", "sine=frequency=440:sample_rate=16000",
                        "-t", "2.2", "-c:v", "libx264", "-c:a", "aac", str(source)], check=True, env=env)
        with contextlib.redirect_stdout(io.StringIO()):
            brain.prepare(self.root, source, "synthetic")
        job = self.root / "work/jobs/synthetic"
        manifest = json.loads((job / "manifest.json").read_text())
        self.assertTrue(brain.artifacts_present(self.root, job, manifest))
        self.assertEqual(len(brain.read_rows(job / "coverage.jsonl")), 3)
        self.assertEqual(self.coverage()[0], 2)
        original_rows = (job / "coverage.jsonl").read_bytes()
        with contextlib.redirect_stdout(io.StringIO()):
            brain.prepare(self.root, source, "synthetic")
        self.assertEqual((job / "coverage.jsonl").read_bytes(), original_rows)
        (job / "audio.wav").unlink()
        with self.assertRaises(ValueError):
            brain.prepare(self.root, source, "synthetic")


if __name__ == "__main__":
    unittest.main()
