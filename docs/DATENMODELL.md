# Datenmodell

## Quellen und Notizen

IDs: `yt_<video-id>`, `ig_<media-id>` und `local_<stabile-id>`. Benutzernamen oder Titel nicht als eindeutigen Schlüssel verwenden. IDs erlauben Buchstaben, Ziffern, Unterstriche und Bindestriche. Für geänderte Originale eine neue Revision mit Verweis auf den Vorgänger anlegen.

Markdown bleibt die lesbare Schicht. Große Sekundenprotokolle liegen in `work/jobs/<id>`; sie sind trotz des Ordnernamens dauerhaft relevante Analysebelege und werden nicht pauschal als Cache gelöscht. Löschbare Caches liegen ausschließlich unter `work/cache` und temporäre Daten unter `work/tmp`.

Jede Aussage hat `source_id`, `start`, `end`, `claim_type`, `confidence`, `reviewed_at` und nach Möglichkeit einen genauen Beleg. Keine erfundene numerische Konfidenz. Nutzbare Kategorien: `observed`, `speaker_claim`, `interpretation`, `metric`, `unknown`. Wikilinks verbinden die Notizen. Für Originale außerhalb des Vault relative Dateilinks verwenden und in Akus Obsidian testen; öffentliche URLs mit Zeitstempel ergänzen, soweit die Plattform das unterstützt.

Das leere `sources: []` der Vorlagen wird beim Erfassen durch belegte Einträge ersetzt. Formbeispiel mit noch offenen Werten:

```yaml
sources:
  - source_id: null
    start: null
    end: null
    claim_type: unknown
    confidence: unknown
    reviewed_at: null
    evidence: null
```

Bei nicht zeitbasierten Dokumenten statt Videozeiten eine genaue Dokument-/Abschnittsreferenz unter `evidence` angeben und die Zeitfelder null lassen.

## Sekundenprotokoll

`coverage.jsonl` enthält exakt eine Zeile je Intervall `[n, min(n+1, Videodauer))`, aufsteigend ohne Lücken oder Duplikate. Für 2,4 Sekunden sind es drei Zeilen. Die `prepare`-Funktion legt sie mit ungeprüften Modalitäten an.

Beispiel für die **Form**, keine echte Analyse:

```json
{"start":0,"end":1,"transcript_reviewed":false,"visual_reviewed":false,"motion_reviewed":false,"audio_reviewed":false,"evidence":{},"speech":"","on_screen_text":"","delivery":"","gesture":"","editing":"","hook_role":"","viewer_effect_hypothesis":"","gaps":[]}
```

Je geprüftem Feld enthält `evidence.<Feldname>` ein Objekt:

```json
{"source":"work/jobs/QUELLEN_ID/clips/clip_00000.mp4, 0.0–1.0 s","method":"tatsächlich verwendetes Sichtungsverfahren","reviewer":"menschliche Prüferkennung oder Modell/Version mit Lauf-ID"}
```

Die Felder bedeuten:

| Feld | Wann true? |
|---|---|
| `transcript_reviewed` | Gesprochener Inhalt im Intervall überprüft, oder überprüft keine Sprache vorhanden |
| `visual_reviewed` | Bildinhalt und relevanter eingeblendeter Text überprüft |
| `motion_reviewed` | Kontinuierlicher Verlauf, Gestik und Schnitt geprüft |
| `audio_reviewed` | Tatsächliches Audio geprüft, oder anhand der Quelle nachgewiesen keine Audiospur vorhanden |

Auch „keine Sprache“, „kein Text“ und „keine Audiospur“ brauchen einen tatsächlichen Befund. Ohne Audiospur kann ein dokumentierter technischer Nachweis `audio_reviewed` erfüllen; Stille in vorhandener Audiospur braucht eine Prüfung. Audio-/Transkript-Felder nicht pauschal auf true setzen. `gaps` enthält offene Probleme als Liste. Bei unverständlicher Sprache bleibt die inhaltliche Lücke sichtbar, auch wenn das Audio angehört wurde.

Der Validator prüft Raster, boolesche Flags, nichtleere Evidenzfelder und vorhandene vorbereitete Dateien. Er kann nicht beweisen, dass ein Modell einen Clip tatsächlich gesehen hat oder dass eine Quellenreferenz den behaupteten Inhalt stützt. `documented_complete` ist deshalb kein Qualitätszertifikat. Ein Qualitätsreview muss Belege, Befunde, Auslassungen und wichtige Übergänge prüfen.

## Performance-Snapshot

JSON oder CSV, bevorzugt eine Zeile pro Metrik:

```json
{"source_id":"yt_VIDEOID","platform":"youtube","captured_at":null,"published_at":null,"window_start":null,"window_end":null,"metric":"views","value":null,"unit":"count","definition":null,"evidence_source":null,"availability":"not_collected"}
```

Zeitpunkte als ISO 8601 mit Zeitzone. Definition und Zeitraum erhalten. Bei Retention die tatsächlichen relativen Zeitpunkte speichern; nie künstlich sekundengenaue Daten durch Interpolation als gemessen ausgeben. Snapshot-Dateien anhängen statt alte Werte zu überschreiben. Rohdatenzugänge und API-Schlüssel gehören nicht in Belege.

## Private Kundenakte

Stabile private Kunden-ID, freigegebene Identität/Kontaktdaten, Ziele, Gesprächsbelege, Entscheidungen, offene Aufgaben, relevante Ergebnisse und Datenstand. Zugang zum privaten Vault und Verarbeitung durch einen Anbieter getrennt entscheiden. Der Content-Vault erhält nur tatsächlich freigegebene oder ausreichend anonymisierte Erkenntnisse; die Zuordnung bleibt privat.

## Dialogstand und Materialeingang

`system/onboarding.json` hält den Einrichtungsdialog fest. Claude pflegt diese Datei nach jedem Schritt; die CLI erzeugt nur den Anfangszustand. Bei älteren Installationen fehlende Felder ergänzen, vorhandene Antworten erhalten:

```json
{"version":1,"updated_at":null,"current_step":"storage","status":"in_progress","completed_steps":[],"answers":{},"sources":[],"open_items":[],"deferred_items":[],"next_question":null}
```

`answers` enthält bestätigte Entscheidungen pro Schritt, `sources` die tatsächlich bereitgestellten Materialien mit Kategorie, Datei-/Ordnerkennung, Zugriffsstatus und lokalem Pfad. `open_items` und `deferred_items` unterscheiden fehlende von ausdrücklich verschobenen Angaben. Keine Credentials speichern. Details stehen im Importregister; nicht den ganzen Dokumentinhalt in den Dialogstand kopieren.

Materialeingänge liegen unter `inbox/videos`, `inbox/scripts`, `inbox/drive`, `inbox/analytics` und `inbox/business`. Der Agent erstellt daraus Quellen- und Wissensnotizen im Vault. Content-Skripte mit `templates/Skript.md` erfassen: stabile Dokument-ID, Version/Änderungsdatum, Hash, Verwendung und belegte Videozuordnung. Entwürfe und publizierte Umsetzung bleiben verschiedene Quellen.
