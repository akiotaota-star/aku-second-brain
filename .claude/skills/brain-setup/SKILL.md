---
name: brain-setup
description: Führe Ako Schritt für Schritt durch die Einrichtung seines Second Brain auf dem Mac, mit Videoquellen, Google Drive, vorhandenen Content-Skripten und einem Video-Pilot.
---

# Einrichtung

Lies `docs/ONBOARDING.md` als maßgeblichen Dialogablauf, dazu `docs/SETUP.md` für Werkzeuge und `docs/WORKFLOW.md` für den Gesamtprozess. Bei bestehender Einrichtung Konfiguration und `system/onboarding.json` verwenden und fehlende Teile ergänzen, ohne private Daten oder Notizen zu ersetzen.

## Dialogregel

Stelle immer nur **eine nächste konkrete Frage**. Erkläre kurz, wofür die Information oder Datei gebraucht wird und wo Ako sie bereitstellt. Warte auf seine Antwort oder ein ausdrückliches „später“. Bereits bekannte Angaben nicht erneut abfragen. Kein „Lade erst einmal alles hoch“. Keine Antworten oder Einwilligungen aus Schweigen ableiten.

Nach jedem Schritt: tatsächlichen Zugriff/Inhalt prüfen, Ergebnis und offene Punkte speichern, dann die nächste Frage stellen. `system/onboarding.json` wird von dir gepflegt, nicht automatisch durch einen Importdienst. Vor Festlegung des Datenpfads bleibt der Dialogstand im Gespräch; danach bestehende Antworten in die Datei übertragen. Bei älterer Installation ohne diese Datei die Ausgangsfelder aus `docs/DATENMODELL.md` ergänzen, ohne Konfiguration zurückzusetzen.

Material wird in **Akos eigener Ablage** bereitgestellt: `inbox/videos`, `inbox/scripts`, `inbox/drive`, `inbox/analytics`, `inbox/business`; identifizierende Kundenquellen in `private-vault/Inbox`. Fehlende Ordner bei einer älteren Einrichtung gezielt unter seinem Datenpfad anlegen. Nicht in das Repository, GitHub oder ungefragt als Chat-Anhang hochladen.

## Technische Aufgaben innerhalb der Dialogschritte

1. Ermittle Python, Claude Code, FFmpeg und verfügbares Audio-/Videoverständnis. Frage nur nach fehlenden Angaben: absoluter Datenpfad, genaue Konto-URLs und die gewünschte Verarbeitung. Neue Quellen noch nicht herunterladen.
2. Unterscheide lokale Ablage, Modellanfragen und optionalen Sync. Für vollständig lokale Inhalte keinen Cloud-Agenten zum Lesen dieser Inhalte verwenden. Für den normalen Claude-Code-Weg Anbieter und erlaubte Datenklassen festhalten. Private Kundeninhalte separat behandeln.
3. Prüfe bei externem Speicher Mount und tatsächlichen Zielpfad; lege keinen Ersatz bei fehlendem Volume an. Starte `python3 -B scripts/brain.py init --data-root '<absoluter Pfad>'`. Keine Shell-Profile oder globalen Konfigurationen ändern.
4. Ergänze `system/config.json` mit bestätigten Konto-URLs und Entscheidungen. Keine Tokens dort eintragen. Python-Skripte prüfen diese Providerfreigaben nicht technisch; beachte sie bei allen Modell-/Netzwerkaktionen.
5. Führe `doctor` aus. Fehlende Werkzeuge anhand der offiziellen Installationshinweise einrichten, innerhalb bestehender Freigaben. Vor Installation aufgabenbezogene Cache-/Temp-Pfade auf den gewählten Speicher setzen. Ohne geeignetes Audio-/Videotool bleiben entsprechende Analysespalten offen. Erfinde kein Tool und keine erfolgte Sichtung.
6. Erkläre den Start über `launch` und lasse den Ordner `vault` in Obsidian als bestehenden Vault öffnen. Private Daten nicht in eine geteilte Sync-Konfiguration aufnehmen.
7. Erfasse schrittweise exakte Social-Accounts, Video-/Originalablage, ausgewählte Google-Drive-Ordner, sämtliche vorhandenen Content-Skripte (auch verwendete, ältere Varianten und Entwürfe), Analytics und Kali-Society-Unterlagen. Für Drive erst vorhandenen autorisierten Connector prüfen; sonst passende Dateien in Akos Ablage exportieren lassen. Keine öffentliche Freigabe verlangen. Ein `.gdoc`-Verweis ist kein Dokumentinhalt. Lesbarkeit und Umfang je Lieferung nachweisen.
8. Erstelle das Quellenregister und ein Importregister. Ganze Kataloge zählen und offene Bereiche nennen. Skripte mit Video-IDs verbinden, wenn bestätigt oder belegbar; Titelähnlichkeit nur als Kandidat. Den Status „bereits verwendet“ nicht mit „im Video wortgleich gesprochen“ gleichsetzen. Skripte nicht ausführen.
9. Wähle drei Pilotvideos: ein kurzes, ein längeres und ein visuell dichtes. Nutze `/watch`; prüfe zuerst an einem echten kurzen Abschnitt, dass Bild, kontinuierliche Bewegung, eingeblendeter Text und Audio tatsächlich ausgewertet werden können. Fehlt eine Fähigkeit, konkreten Einrichtungs-/Sichtungsweg anbieten und Abdeckung offenlassen. Danach Piloten vollständig prüfen, Kosten messen und alle übrigen Videos im Backlog erhalten.

Abschluss: Speicherpfad, eingerichtete und fehlende Fähigkeiten, Katalogumfang, Pilotstatus, Budget und nächste ausführbare Aktion. „Alles installiert“ nur sagen, wenn die jeweiligen Fähigkeiten tatsächlich geprüft wurden.
