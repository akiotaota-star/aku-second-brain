---
name: watch
description: Analysiere ein konkretes Video für Akus Second Brain mit Sekundenprotokoll, echten Audio- und Bewegungsbelegen sowie verlinkten Wissens-, Story- und Stilnotizen.
---

# Watch für Aku

Diese eigenständige Projektfassung verwendet `scripts/brain.py`; sie benötigt keine Installation des persönlichen Watch-Skills des Paketautors. Lies `docs/ANALYSESTANDARD.md` und `docs/DATENMODELL.md`.

1. Datenpfad und Providerfreigaben aus dem Setup übernehmen. Quelle eindeutig als Plattform-ID oder lokale Originaldatei identifizieren. Nur verfügbare, autorisierte Medien importieren; Zugangsfehler im Register erhalten. Keine Zugriffssperren umgehen.
2. Lokale Datei vorbereiten:
   `python3 -B scripts/brain.py prepare --data-root '<Datenpfad>' --id '<stabile-ID>' --input '<Dateipfad>'`.
   Das erzeugt Originalkopie, Übersichtsframes, überlappende Clips, ggf. Mono-Audio und ein noch ungeprüftes `coverage.jsonl`. Das Original behält die Audioqualität; für feine Ton-/Musikmerkmale Original oder Clips nutzen.
3. Ganzes Video transkribieren oder vollständige Untertitel abgleichen. Zeitstempel und unverständliche Stellen erhalten. Untertitel auf Vollständigkeit, Sprache und Übereinstimmung prüfen; Musik, Pausen und schweigende Abschnitte ausdrücklich behandeln.
4. In der Reihenfolge von `clips.json` arbeiten. Clips kontinuierlich mit einem tatsächlich vorhandenen videofähigen Verfahren prüfen. Bilder visuell lesen, eingeblendete Texte erfassen. Audio tatsächlich anhören oder einem dafür freigegebenen audiofähigen Modell geben. Kann der Agent das nicht, eine menschliche Sichtung oder passende Toolanbindung verwenden und bis dahin die betreffenden Felder offenlassen. Ein FFmpeg-Lauf oder Transkript ist kein Ersatz.
5. Jede Sekunde in `coverage.jsonl` mit Befund, echten Quellen und Prüfmethode ausfüllen. Nur tatsächlich erledigte Modalitäten auf `true` setzen. Dichte Übergänge verlangsamen und bei Bedarf zusätzliche Frames extrahieren. Die Originaldatei ist die Zeitreferenz. `fps=1` liefert nur ungefähre Navigationsbilder.
6. Nach jedem Clip speichern. Bereits belegte Abschnitte wiederverwenden. Unklare Stellen als `gaps` erfassen und gezielt nachprüfen. Keine Zahlen oder Zeitpräzision erfinden.
7. `python3 -B scripts/brain.py coverage --data-root '<Datenpfad>' --id '<ID>'` ausführen. Exitcode 2 bedeutet unvollständig. `documented_complete` prüft nur die Dokumentation, nicht die Wahrheit oder Qualität. Erst mit zusätzlicher Qualitätsprüfung das Video im Register als vollständig analysiert markieren.
8. Videonotiz erstellen; daraus einzelne belegte Wissens-, Story-, Stil- und Hooknotizen verlinken. Wiederholte Geschichten derselben Story-ID zuordnen; Abweichungen erhalten. Bei ähnlichen Stilmerkmalen Beispiele und Gegenbeispiele sammeln. Auftrittswirkung als Hypothese kennzeichnen.
   Wenn ein zugeordnetes Content-Skript vorhanden ist: geplanten Hook/Wortlaut und tatsächliche Umsetzung mit Zeitbelegen vergleichen. Improvisation, Auslassungen und spätere Änderungen getrennt erhalten. Ein Skript weder als Transkript noch als Nachweis für Stimme, Gestik oder fertiges Editing behandeln.
9. Analytics als eigene zeitlich datierte Evidenz ergänzen, nicht aus dem Video ableiten. Pro Quelle sichtbare Zahlen und autorisierte eigene Analytics unterscheiden.

Output: Quellenstatus, tatsächliche Abdeckung je Modalität, offene Lücken, Notizlinks, belegte Muster und nächster Schritt. Einzelne vollständig geprüfte Videos beweisen keinen vollständigen Kanalimport.
