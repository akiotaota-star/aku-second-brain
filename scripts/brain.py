#!/usr/bin/env python3
"""Local scaffolding and video preparation. No network calls or model inference."""
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone

REPO = Path(__file__).resolve().parents[1]
MODALITIES = ("transcript_reviewed", "visual_reviewed", "motion_reviewed", "audio_reviewed")
FOLDERS = ("00_Start", "01_Inbox", "02_Quellen", "03_Wissen", "04_Stories",
           "05_Stil", "06_Hooks", "07_Performance", "08_Kali_Society",
           "09_Content_Studio", "10_Reviews", "99_Templates")


def now():
    return datetime.now(timezone.utc).isoformat()


def under(path, parent):
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def root_path(value):
    p = Path(value).expanduser()
    if not p.is_absolute():
        raise ValueError("Datenpfad muss absolut sein.")
    for candidate in (p, p.resolve()):
        parts = candidate.parts
        if len(parts) >= 2 and parts[1] == "Volumes":
            if len(parts) < 3 or not Path("/Volumes", parts[2]).is_mount():
                raise ValueError("Gewähltes Volume ist nicht eingebunden. Kein Ersatzordner wird angelegt.")
    p = p.resolve()
    if under(p, REPO) or under(REPO, p):
        raise ValueError("Datenablage und Repository müssen getrennte Ordner sein.")
    return p


def child(root, relative):
    p = root / relative
    if not under(p.resolve(), root.resolve()):
        raise ValueError("Ziel verlässt Datenablage (möglicherweise durch einen Symlink).")
    return p


def save_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    if path.is_symlink() or tmp.is_symlink():
        raise ValueError("Symlink als Schreibziel abgelehnt.")
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)


def config(root):
    value = json.loads(child(root, "system/config.json").read_text(encoding="utf-8"))
    if value.get("version") != 1:
        raise ValueError("Unbekannte Konfigurationsversion.")
    return value


def env_for(root):
    env = os.environ.copy()
    for key, relative in {
        "TMPDIR": "work/tmp", "TMP": "work/tmp", "TEMP": "work/tmp",
        "XDG_CACHE_HOME": "work/cache", "PIP_CACHE_DIR": "work/cache/pip",
        "HF_HOME": "work/models/huggingface", "TORCH_HOME": "work/models/torch",
        "UV_CACHE_DIR": "work/cache/uv", "npm_config_cache": "work/cache/npm",
        "HOMEBREW_CACHE": "work/cache/homebrew",
    }.items():
        folder = child(root, relative)
        folder.mkdir(parents=True, exist_ok=True)
        env[key] = str(folder)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["AKU_BRAIN_ROOT"] = str(root)
    return env


def init(root):
    marker = child(root, "system/config.json")
    if marker.exists():
        config(root)
        print("Bereits eingerichtet; keine bestehenden Inhalte verändert:", root)
        return
    if root.exists() and any(root.iterdir()):
        raise ValueError("Ersteinrichtung benötigt einen neuen oder leeren Datenordner.")
    root.mkdir(parents=True, exist_ok=True)
    for folder in FOLDERS:
        child(root, "vault/" + folder).mkdir(parents=True, exist_ok=True)
    for folder in ("system", "media", "work/jobs", "private-vault/01_Kunden", "private-vault/02_Gespraeche",
                   "private-vault/Inbox", "inbox/videos", "inbox/scripts", "inbox/drive", "inbox/analytics", "inbox/business"):
        child(root, folder).mkdir(parents=True, exist_ok=True)
    env_for(root)
    for source in (REPO / "templates").glob("*.md"):
        shutil.copyfile(source, child(root, "vault/99_Templates/" + source.name))
    child(root, "vault/00_Start/Start.md").write_text(
        "# Aku – Second Brain\n\n"
        "Quellen → Wissen, Stories und Stil → Content-Entwürfe → Performance → neue Erkenntnisse.\n\n"
        "- [[Quellenregister]]\n- [[Stilprofil]]\n- [[Kali Society]]\n\n"
        "Das Kundenarchiv liegt als separater Vault in `private-vault`.\n"
        "Vorlagen sind leer. Es wurden keine Accounts abgerufen oder Medien importiert.\n", encoding="utf-8")
    for rel, text in {
        "vault/02_Quellen/Quellenregister.md": "# Quellenregister\n\nErst nach bestätigten Konto-URLs befüllen.\n\n| ID | Plattform | URL | Datum | Dauer | Status | Lücken |\n|---|---|---|---|---|---|---|\n",
        "vault/05_Stil/Stilprofil.md": "# Stilprofil\n\nNoch keine belegten Muster. Pro Muster Beispiele, Gegenbeispiele, Zeitraum und Konfidenz sammeln.\n",
        "vault/08_Kali_Society/Kali Society.md": "# Kali Society\n\nAngebote, Prozesse, Ziele und Entscheidungen mit Quelle und Gültigkeitsdatum erfassen. Keine unbestätigten Angaben.\n",
        "private-vault/Start.md": "# Privates Kundenarchiv\n\nIdentifizierende Kundendaten bleiben hier. Dieser Ordner wird vom Launcher nicht als Arbeitsverzeichnis freigegeben. Das ist keine Betriebssystem-Zugriffssperre.\n",
    }.items():
        child(root, rel).write_text(text, encoding="utf-8")
    save_json(marker, {"version": 1, "created_at": now(), "owner": "Aku",
        "accounts": {"youtube_url": None, "instagram_url": None},
        "drive": {"access_method": None, "selected_folders": [], "verified_read_access": False},
        "processing": {"mode": "unconfigured", "approved_providers": [],
                       "approved_data_classes": [], "audio_review_method": None,
                       "motion_review_method": None},
        "batch": {"pilot_videos": 3, "max_parallel_jobs": 1, "approved_cost_limit_eur": None},
        "sync": {"enabled": False, "provider": None},
        "storage_note": "Arbeitsdaten hier; Programme, Anmeldedaten und App-Sitzungsdaten werden nicht vollständig umgeleitet."})
    save_json(child(root, "system/onboarding.json"), {
        "version": 1, "updated_at": now(), "current_step": "storage",
        "status": "in_progress", "completed_steps": [], "answers": {},
        "sources": [], "open_items": [], "deferred_items": [], "next_question": None,
        "note": "Claude aktualisiert diesen Dialogstand nach jedem Schritt; kein automatischer Importdienst."})
    print("Eingerichtet:", root)
    print("In Obsidian als bestehenden Vault öffnen:", child(root, "vault"))


def run(args, env):
    subprocess.run([str(a) for a in args], check=True, env=env)


def probe(source, env):
    if shutil.which("ffprobe"):
        result = subprocess.run(["ffprobe", "-v", "error", "-show_format", "-show_streams",
                                 "-of", "json", str(source)], check=True, env=env,
                                capture_output=True, text=True)
        value = json.loads(result.stdout)
        if not any(s["codec_type"] == "video" for s in value["streams"]):
            raise ValueError("Quelle enthält keine Videospur.")
        return float(value["format"]["duration"]), any(s["codec_type"] == "audio" for s in value["streams"]), "ffprobe"
    result = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(source)], env=env,
                            capture_output=True, text=True)
    match = re.search(r"Duration: (\d+):(\d+):(\d+(?:\.\d+)?)", result.stderr)
    if not match or "Video:" not in result.stderr:
        raise ValueError("Dauer/Videospur nicht lesbar; ffprobe installieren oder Quelle prüfen.")
    h, m, s = map(float, match.groups())
    return h * 3600 + m * 60 + s, "Audio:" in result.stderr, "ffmpeg-header-rounded"


def digest(path):
    value = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def valid_id(value):
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,99}", value):
        raise ValueError("ID: 1–100 Buchstaben/Ziffern, Unterstriche oder Bindestriche.")
    return value


def safe_output(path, root):
    if path.is_symlink() or not under(path.resolve(), root):
        raise ValueError("Unsicherer Ausgabepfad: " + str(path))
    return path


def grid_valid(rows, duration):
    return len(rows) == math.ceil(duration) and all(
        isinstance(row, dict) and row.get("start") == i and row.get("end") == min(duration, i + 1)
        for i, row in enumerate(rows))


def read_rows(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def artifacts_present(root, job, manifest):
    try:
        frames = list((job / "frames").glob("frame_*.jpg"))
        count = json.loads((job / "frames.done.json").read_text(encoding="utf-8"))["count"]
        clips = json.loads((job / "clips.json").read_text(encoding="utf-8"))
        files = frames + [root / item["path"] for item in clips] + [root / manifest["source_relpath"]]
        if manifest["has_audio"]:
            files.append(job / "audio.wav")
        return (count > 0 and len(frames) == count and len(clips) == math.ceil(manifest["duration_seconds"] / 30)
                and all(under(p.resolve(), root) and p.is_file() and p.stat().st_size > 0 for p in files)
                and grid_valid(read_rows(job / "coverage.jsonl"), manifest["duration_seconds"]))
    except (OSError, ValueError, KeyError, TypeError):
        return False


def prepare(root, source, video_id):
    config(root)
    valid_id(video_id)
    if not shutil.which("ffmpeg"):
        raise ValueError("ffmpeg fehlt im PATH. Siehe docs/SETUP.md.")
    source = Path(source).expanduser().resolve(strict=True)
    if not source.is_file():
        raise ValueError("Quelle ist keine Datei.")
    env = env_for(root)
    duration, has_audio, probe_method = probe(source, env)
    if not math.isfinite(duration) or duration <= 0:
        raise ValueError("Ungültige Dauer.")
    sha = digest(source)
    job = child(root, "work/jobs/" + video_id)
    job.mkdir(parents=True, exist_ok=True)
    manifest_path = child(root, "work/jobs/" + video_id + "/manifest.json")
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if manifest["source_sha256"] != sha:
            raise ValueError("ID gehört bereits zu einem anderen Video. Neue ID wählen.")
        if manifest.get("stage") == "prepared":
            if not artifacts_present(root, job, manifest):
                raise ValueError("Vorbereitete Artefakte fehlen. Job nicht als vollständig behandeln; Original wiederherstellen oder neue Revision vorbereiten.")
            print("Bereits vorbereitet; vorhandene Analyse bleibt erhalten:", job)
            return
    media = child(root, "media/" + video_id)
    media.mkdir(parents=True, exist_ok=True)
    original = child(root, "media/" + video_id + "/source" + source.suffix.lower())
    if original.exists() and digest(original) != sha:
        raise ValueError("Zieldatei enthält andere Daten.")
    if not original.exists():
        stage = original.with_name(original.name + ".partial")
        if stage.is_symlink():
            raise ValueError("Symlink als Kopierziel abgelehnt.")
        shutil.copyfile(source, stage)
        stage.replace(original)
    manifest = {"version": 1, "id": video_id, "source_sha256": sha,
                "source_relpath": str(original.relative_to(root)), "duration_seconds": duration,
                "duration_method": probe_method, "has_audio": has_audio, "stage": "preparing",
                "updated_at": now(), "frame_sampling": "1 fps overview; not motion review"}
    save_json(manifest_path, manifest)
    ff = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-nostdin", "-y"]
    frames = child(root, "work/jobs/" + video_id + "/frames")
    frames.mkdir(exist_ok=True)
    frames_done = child(root, "work/jobs/" + video_id + "/frames.done.json")
    if not frames_done.exists():
        for existing in frames.glob("*"):
            safe_output(existing, root)
        run(ff + ["-i", original, "-vf", "fps=1", "-start_number", "0", "-q:v", "3", frames / "frame_%06d.jpg"], env)
        if not list(frames.glob("frame_*.jpg")):
            run(ff + ["-i", original, "-frames:v", "1", frames / "frame_000000.jpg"], env)
        save_json(frames_done, {"count": len(list(frames.glob("frame_*.jpg"))), "sampling": "fps=1; approximate navigation times"})
    audio = child(root, "work/jobs/" + video_id + "/audio.wav")
    if has_audio and not audio.exists():
        stage = safe_output(audio.with_name("audio.partial.wav"), root)
        run(ff + ["-i", original, "-vn", "-ac", "1", "-ar", "16000", stage], env)
        stage.replace(audio)
    clips = child(root, "work/jobs/" + video_id + "/clips")
    clips.mkdir(exist_ok=True)
    clip_index = []
    for number, start in enumerate(range(0, math.ceil(duration), 30)):
        begin, end = max(0, start - 1), min(duration, start + 31)
        clip = child(root, "work/jobs/" + video_id + "/clips/clip_%05d.mp4" % number)
        if not clip.exists():
            stage = safe_output(clip.with_name(clip.stem + ".partial.mp4"), root)
            run(ff + ["-ss", str(begin), "-i", original, "-t", str(end - begin),
                      "-map", "0:v:0", "-map", "0:a:0?", "-c:v", "libx264", "-crf", "20",
                      "-preset", "fast", "-c:a", "aac", "-movflags", "+faststart", stage], env)
            stage.replace(clip)
        clip_index.append({"path": str(clip.relative_to(root)), "start": begin, "end": end,
                           "target_start": start, "target_end": min(duration, start + 30)})
    save_json(child(root, "work/jobs/" + video_id + "/clips.json"), clip_index)
    coverage = child(root, "work/jobs/" + video_id + "/coverage.jsonl")
    if not coverage.exists():
        stage = safe_output(coverage.with_name("coverage.partial.jsonl"), root)
        with stage.open("w", encoding="utf-8") as f:
            for start in range(math.ceil(duration)):
                row = {"start": start, "end": min(duration, start + 1),
                       **{field: False for field in MODALITIES}, "evidence": {},
                       "speech": "", "on_screen_text": "", "delivery": "", "gesture": "",
                       "editing": "", "hook_role": "", "viewer_effect_hypothesis": "",
                       "gaps": []}
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
        stage.replace(coverage)
    if not grid_valid(read_rows(coverage), duration):
        raise ValueError("Vorhandenes Sekundenprotokoll hat Lücken; Nutzerbefunde erhalten und Zeitraster reparieren, bevor prepared gesetzt wird.")
    if not artifacts_present(root, job, manifest):
        raise ValueError("Vorbereitung enthält fehlende/ungültige Artefakte. Fehler prüfen; bestehende Befunde bleiben erhalten.")
    manifest.update(stage="prepared", updated_at=now())
    save_json(manifest_path, manifest)
    print("Vorbereitet, noch NICHT analysiert:", job)


def check_coverage(root, video_id):
    valid_id(video_id)
    job = child(root, "work/jobs/" + video_id)
    manifest = json.loads((job / "manifest.json").read_text(encoding="utf-8"))
    duration = manifest["duration_seconds"]
    if not isinstance(duration, (int, float)) or not math.isfinite(duration) or duration <= 0:
        raise ValueError("Ungültige Dauer im Manifest.")
    rows = read_rows(job / "coverage.jsonl")
    expected = math.ceil(duration)
    errors, counts = [], {field: 0 for field in MODALITIES}
    if manifest.get("stage") != "prepared":
        errors.append("Vorbereitung unvollständig.")
    if not artifacts_present(root, job, manifest):
        errors.append("Vorbereitete Artefakte fehlen oder Zeitraster ist beschädigt.")
    if len(rows) != expected:
        errors.append("Erwartet %d Sekundenzeilen, erhalten %d." % (expected, len(rows)))
    for i, row in enumerate(rows):
        if not isinstance(row, dict):
            errors.append("Zeile %d ist kein Objekt." % i)
            continue
        if row.get("start") != i or row.get("end") != min(duration, i + 1):
            errors.append("Zeile %d: falsches Zeitintervall oder Reihenfolge." % i)
        if not isinstance(row.get("gaps"), list) or row.get("gaps"):
            errors.append("Zeile %d: offene oder ungültige Lückenliste." % i)
        evidence = row.get("evidence", {})
        if not isinstance(evidence, dict):
            errors.append("Zeile %d: ungültige Evidenz." % i)
            continue
        for field in MODALITIES:
            item = evidence.get(field, {})
            valid_evidence = isinstance(item, dict) and all(
                isinstance(item.get(k), str) and item[k].strip() for k in ("source", "method", "reviewer"))
            if row.get(field) is True and valid_evidence:
                counts[field] += 1
    complete = not errors and all(count == expected for count in counts.values())
    result = {"id": video_id, "status": "documented_complete" if complete else "partial",
              "seconds_expected": expected, "reviewed_counts": counts, "errors": errors,
              "caveat": "Prüft Zeitabdeckung und Dokumentation, nicht die Wahrheit der Sichtung oder fachliche Qualität."}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if complete else 2


def doctor(root):
    config(root)
    result = {"python": sys.version.split()[0], "data_root": str(root),
              "data_root_writable": os.access(root, os.W_OK),
              "tools": {name: shutil.which(name) for name in ("ffmpeg", "ffprobe", "yt-dlp", "claude")},
              "note": "ffmpeg: lokale Vorbereitung; ffprobe: präzisere Metadaten; yt-dlp: optionaler Import. Audio-/Videoverständnis separat einrichten."}
    print(json.dumps(result, ensure_ascii=False, indent=2))


def launch(root):
    config(root)
    exe = shutil.which("claude")
    if not exe:
        raise ValueError("Claude Code fehlt im PATH; siehe offizielle Installationsanleitung.")
    env = env_for(root)
    cmd = [exe]
    for folder in ("vault", "system", "media", "work", "inbox"):
        cmd += ["--add-dir", str(child(root, folder))]
    print("Starte Claude Code im Repository. Kundenarchiv wird nicht hinzugefügt.", flush=True)
    return subprocess.call(cmd, cwd=REPO, env=env)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("init", "doctor", "launch", "prepare", "coverage"):
        p = sub.add_parser(name)
        p.add_argument("--data-root", default=os.getenv("AKU_BRAIN_ROOT"), required=not os.getenv("AKU_BRAIN_ROOT"))
        if name in ("prepare", "coverage"):
            p.add_argument("--id", required=True)
        if name == "prepare":
            p.add_argument("--input", required=True)
    args = parser.parse_args()
    try:
        root = root_path(args.data_root)
        if args.command == "init":
            init(root)
        elif args.command == "doctor":
            doctor(root)
        elif args.command == "prepare":
            prepare(root, args.input, args.id)
        elif args.command == "coverage":
            return check_coverage(root, args.id)
        elif args.command == "launch":
            return launch(root)
        return 0
    except (ValueError, OSError, subprocess.CalledProcessError, KeyError, TypeError) as exc:
        print("Fehler:", exc, file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
