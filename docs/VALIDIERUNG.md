# Validierung des Starter-Pakets

Geprüft am 02.11.2026 auf macOS. Keine echten Videos, Instagram-Inhalte, Accountzugänge oder Kundendaten verwendet.

## Erfolgreich geprüft

Sieben automatisierte Tests mit Python 3.9 und FFmpeg:

1. Erneute Einrichtung erhält vorhandene Notizen und Konfiguration.
2. Datenpfade innerhalb/oberhalb des Repositories und fehlende externe Volumes werden abgelehnt.
3. Ein nichtleerer fremder Ordner wird nicht zur Datenablage umfunktioniert.
4. Symlinks können die geprüften Ausgabeziele nicht aus dem Datenordner herauslenken.
5. Ungeprüfte oder unbelegte Modalitätsflags bleiben unvollständig.
6. Falsche Zeitintervalle, offene Lücken und fehlende Artefakte verhindern dokumentierte Vollständigkeit.
7. Ein synthetisch erzeugtes 2,2-Sekunden-Video wird mit Audio, Frames, Clip und Sekundenprotokoll vorbereitet. Erneuter Lauf erhält das Protokoll; gelöschtes Audio wird erkannt.

Zusätzlich: vier Projekt-Skills mit dem Skill-Validator geprüft; YAML-Frontmatter der zehn Vorlagen geparst; lokale Dokumentlinks geprüft. Eine unabhängige Agentenprüfung fand vier Fehlerfälle, die vor Abschluss behoben wurden: fehlender Volume-Mount, unzureichende Artefaktprüfung, nicht atomarer Protokollschreibvorgang und ungeschützte FFmpeg-Zwischenziele.

Die Erweiterung um den geführten Dialog, Google-Drive-Material, Content-Skripte, Eingangsordner und gespeicherten Onboarding-Stand wurde am selben Tag ergänzt. Danach bestanden die sieben Tests erneut. Der Dialog ist eine geprüfte Arbeitsanweisung, keine bereits in Akos Claude-Code-Umgebung ausgeführte Einrichtung; Drive-Zugriff und tatsächliche Audio-/Videoanalyse bleiben Teil seines Piloten.

## Nicht als getestet ausgeben

- Live-Import von YouTube oder Instagram, OAuth, API-Quoten und konkrete Kontoberechtigungen.
- Ausführung der Skills in Akus Claude-Code-Sitzung oder Öffnen des Vaults in seiner Obsidian-Installation.
- Modelle für Transkription, Tonfall, OCR und kontinuierliches Videoverständnis.
- Fachliche Genauigkeit einer realen Videoanalyse, Zuschauerwirkung oder Stilübertragung.
- FFprobe-Verarbeitung: Der Medien-Test nutzte den dokumentierten FFmpeg-Fallback.
- Große Archive, lange Videos, Cloud-Worker, automatische Synchronisierung und Backup-Wiederherstellung.

Diese Punkte sind Teil des bei Aku durchzuführenden Piloten. Der Adapter ist getestet; das vollständige spätere System noch nicht.

## Tests auf Akus Rechner wiederholen

Einen genehmigten existierenden Scratch-Ordner außerhalb des Repositories angeben. Ohne `AKU_TEST_ROOT` wird kein Standard-Temp-Verzeichnis gewählt.

```bash
AKU_TEST_ROOT='/ABSOLUTER/PFAD/AkuBrain/work/tmp' \
TMPDIR='/ABSOLUTER/PFAD/AkuBrain/work/tmp' \
PYTHONDONTWRITEBYTECODE=1 \
python3 -B -m unittest discover -s tests -v
```

FFmpeg muss im PATH sein; sonst wird der Medientest explizit übersprungen. Die übrigen Tests benötigen keine zusätzlichen Python-Pakete. Sie verwenden ausschließlich künstliche Daten und bereinigen ihre eigenen temporären Verzeichnisse.
