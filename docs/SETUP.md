# Einrichtung auf Akus Mac

## Voraussetzungen und Speicherentscheidung

Python 3.9+ genügt für den Adapter; er braucht keine Python-Pakete. FFmpeg ist für Medienaufbereitung nötig, FFprobe für präzisere Metadaten empfohlen. Ohne FFprobe liest der Adapter die gerundete Dauer aus dem FFmpeg-Header und dokumentiert diesen Unterschied. `yt-dlp` ist optional für erlaubte URL-Importe, nicht für vorhandene Originaldateien. Manche URLs brauchen zusätzliche Laufzeiten oder Kontozugriff; aktuelle Anforderungen beim Anbieter prüfen. Obsidian und Claude Code werden separat installiert.

Offizielle Einstiege: [Claude Code](https://code.claude.com/docs/en/setup), [Python](https://www.python.org/downloads/macos/), [FFmpeg](https://ffmpeg.org/download.html), [yt-dlp](https://github.com/yt-dlp/yt-dlp#installation), [Obsidian](https://obsidian.md/download).

Aku wählt einen absoluten Datenpfad außerhalb des Repositories, beispielsweise `/Users/AKUS_BENUTZERNAME/AkuBrain` oder einen Ordner auf seiner externen SSD. Dieser Beispielpfad ist bei ihm zu ersetzen. Die Speicherregel des Paketautors wird nicht als fester Lexar-Pfad an Aku vererbt. Falls Aku ebenfalls nur externe Speicherung will, erst Mount prüfen und alle kontrollierbaren Arbeitsdaten dorthin legen. Das Skript lehnt fehlende `/Volumes/<Name>`-Mounts ab.

## Einmalige Einrichtung

Im Repository:

```bash
python3 -B scripts/brain.py init --data-root '/ABSOLUTER/PFAD/AkuBrain'
python3 -B scripts/brain.py doctor --data-root '/ABSOLUTER/PFAD/AkuBrain'
python3 -B scripts/brain.py launch --data-root '/ABSOLUTER/PFAD/AkuBrain'
```

In der gestarteten Claude-Code-Sitzung `/brain-setup` verwenden. Der Launcher setzt `AKU_BRAIN_ROOT` und aufgabenbezogene Temp-/Cache-Pfade. Er leitet weder alle Betriebssystemdaten noch alle Programmeinstellungen oder Authentifizierungsdaten um. Installation und Modell-Downloads müssen ihre jeweiligen Zielpfade ebenfalls beachten; der Launcher ist keine allgemeine Speicher-Sandbox.

Claude folgt dem [Onboarding-Dialog](ONBOARDING.md) und fragt jeweils nur nach dem nächsten Schritt. Antworten und noch fehlende Materialien werden in `system/onboarding.json` gespeichert. Ein Datenordner wird nicht automatisch mit dem gesamten Drive-Inhalt befüllt: zunächst Umfang wählen und tatsächlichen Zugang prüfen. Video-, Skript-, Drive-, Analytics- und Business-Dateien werden getrennt unter `inbox` bereitgestellt. Inhalte nie in das Starter-Repository hochladen.

In Obsidian „Ordner als Vault öffnen“ wählen und `AkuBrain/vault` öffnen. Community-Plugins und eine Vektordatenbank sind für die erste Version nicht nötig: Markdown, Wikilinks und Suche reichen. `private-vault` ist ein separater, nicht verschachtelter Vault.

## Entscheidungen in system/config.json

| Feld | Bedeutung |
|---|---|
| `accounts.youtube_url`, `accounts.instagram_url` | Von Aku bestätigte Profil-URLs; nicht aus dem Anzeigenamen raten |
| `drive.access_method`, `drive.selected_folders`, `drive.verified_read_access` | Gewählter Importweg, bestätigte Ordner und tatsächlich geprüfter Zugriff; kein automatischer Connector |
| `processing.mode` | `unconfigured`, `local-files-cloud-analysis` oder `local-only` |
| `processing.approved_providers` | Konkrete Anbieter/Wege, denen Aku die betreffenden Inhalte anvertrauen will |
| `processing.approved_data_classes` | Zum Beispiel `public_creator_content`; Kundendaten nicht stillschweigend einschließen |
| `processing.audio_review_method` | Tatsächliches Verfahren zum Hören/Analysieren von Audio |
| `processing.motion_review_method` | Tatsächliches Verfahren zum kontinuierlichen Prüfen von Bewegung |
| `batch.approved_cost_limit_eur` | Vereinbarter Kostenrahmen; null = kein unbegrenzter Batch freigegeben |
| `sync` | Optionaler Sync, standardmäßig deaktiviert |

Die Konfiguration dokumentiert Entscheidungen für den Agenten. Sie erzwingt keine technischen Netzwerk- oder Ausgabenlimits. Vor einem unbeaufsichtigten Betrieb braucht es entsprechende Kontrollen beim Modellanbieter/Worker. Zugangsdaten bleiben im persönlichen Credential-Store oder einer geeigneten lokalen Secret-Verwaltung, nicht in dieser Konfiguration oder Git.

## Der entscheidende Fähigkeitscheck

Claude Code kann Skripte ausführen und je nach Umgebung Bilder auswerten. Das Paket stellt **keine** native Video-/Audio-Inferenz oder Transkription bereit. Beim Setup einen real vorhandenen Weg auswählen:

- **Claude Code plus freigegebener Audio-/Videoanbieter:** Modell/Tool auf kurzen Testclips prüfen, Datenfluss und Kosten festhalten. Ein API-Key allein ist noch kein fertiger Adapter.
- **Lokale Fachmodelle:** Transkription, Audio- und Videoverständnis separat lokal betreiben; Modellgewichte, Hardwarebedarf und Qualität zunächst testen. Cloud-Claude darf geschützte Inhalte dann nicht als Kontext lesen. Ein komplett lokales Gesamtsystem ist zusätzliche Implementierung.
- **Menschliche Sichtung:** Aku hört und sieht Clips und dokumentiert Beobachtungen. Das erlaubt einen ehrlichen Pilot ohne vorgetäuschte Modellfähigkeit.

Wenn nur Transkription und Einzelbilder verfügbar sind, beginnt die Wissensextraktion; Audio-/Bewegungsabdeckung bleibt offen. Der vollständige Anspruch wird dadurch nicht abgesenkt.

## Import und Analyse

Mit einer von Aku bereitgestellten Datei:

```bash
python3 -B scripts/brain.py prepare --data-root '/ABSOLUTER/PFAD/AkuBrain' --id 'yt_VIDEOID' --input '/PFAD/ZUM/ORIGINAL.mp4'
python3 -B scripts/brain.py coverage --data-root '/ABSOLUTER/PFAD/AkuBrain' --id 'yt_VIDEOID'
```

`prepare` lädt nichts herunter. Es kopiert das Original in `media`, erzeugt 1-fps-Bilder in Originalauflösung, überlappende Clips mit vollständiger Bewegungsfolge sowie ggf. 16-kHz-Mono-Audio. Der Clipstart steht in `clips.json`; nicht aus dem Dateinamen auf absolute Zeit schließen. Original/Clips für feine Tonmerkmale verwenden. Bilder, Audio und Clips können deutlich mehr Speicher als das Original benötigen.

Für URL-Importe soll Claude bei Aku ein verfügbares, autorisiertes Importverfahren nutzen und dessen Cache-, Temp- und Ausgabepfade explizit setzen. Katalogimport, Medienimport und Modellanalyse sind getrennte Schritte. Dieses Paket enthält keinen getesteten YouTube-/Instagram-Downloader oder OAuth-Connector. Bei Zugangsfehlern Originaldatei/Export verwenden und die Lücke dokumentieren.

Wiederholte Aufbereitung derselben ID und desselben Originals erhält vorhandene Analysen. Ein anderes Original unter derselben ID wird abgelehnt. Bei unterbrochenem `preparing` werden abgeschlossene Teilprodukte wiederverwendet. Fehlende Dateien eines bereits fertigen Jobs werden als Fehler gemeldet; vorhandene Befunde nicht löschen, sondern Artefakte wiederherstellen oder eine neue Quellenrevision anlegen.

## Optional: Akus Cloud

Zunächst lokale Ablage auf Akus Mac. Später kann sein eigener Server denselben Datenaufbau und Worker übernehmen. Obsidian benötigt weiterhin einen lokal verfügbaren Vault; nur ein Object-Storage-Bucket ist kein direkt öffnungsfähiger Vault. Synchronisierung und verschlüsseltes Backup separat planen, mit Wiederherstellungstest. Nicht mehrere Sync-Systeme gleichzeitig auf dieselben Dateien ansetzen.

Medien und Sekundenprotokolle nicht unnötig auf jedes Gerät synchronisieren. Nur fertige Notizen und ausgewählte Belege in den normalen Vault-Sync aufnehmen. Das private Kundenarchiv bekommt eine eigene Freigabe. Ein Cloud-Worker braucht persistenten Speicher, Accountzugänge, Kostenlimits und Logs; das ist kein bereits enthaltener One-Click-Dienst.

## GitHub-Übergabe

Das Starter-Repository ist auf Wunsch des Paketautors öffentlich zugänglich. Es enthält ausschließlich Code, Arbeitsanweisungen und leere Vorlagen. Nur dieses Repository-Verzeichnis veröffentlichen, nicht den umgebenden Datenordner. `git status` und die tatsächlich zur Veröffentlichung vorgesehenen Dateien prüfen; `.gitignore` allein schützt bereits getrackte Dateien nicht. Keine Kundendaten, Medien, Zugangsdaten oder privaten Skriptinhalte in Commits, Issues oder Actions-Artefakte hochladen. Ako klont dieses Repository oder lädt das ZIP herunter und beginnt mit `/brain-setup`.
