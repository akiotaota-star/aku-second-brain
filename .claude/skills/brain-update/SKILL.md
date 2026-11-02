---
name: brain-update
description: Gleiche Akus Quellenkatalog ab, arbeite neue und unvollständige Videos ab und ergänze datierte Analytics sowie belegte Änderungen in Kali Society.
---

# Aktualisieren

Lies `docs/WORKFLOW.md`. Verwende bestehende Konto-, Budget- und Providerfreigaben.

1. Quellenregister und letzten Checkpoint lesen. Veröffentlichungs-ID plus Plattform deduplizieren. Importfehler, fehlende Seiten und nicht mehr zugängliche Quellen sichtbar lassen. Quellen nicht aufgrund einer fehlenden API-Antwort löschen.
2. Neue Quellen registrieren. Vor Medienimport Umfang und Budget prüfen; Pilot oder freigegebenen Batch fortsetzen. Unvollständige Jobs zuerst auf fehlende Modalitäten prüfen, nicht unnötig komplett neu erzeugen.
3. `/watch` je Quelle anwenden. Ganze Kataloge in wiederaufnehmbare Jobs teilen. Auf neue Nutzerkorrekturen achten, handgeschriebene Notizen erhalten.
4. Aktuelle Analytics aus tatsächlich verfügbaren Kontozugängen/Exports ergänzen: Zeitpunkt, Berichtszeitraum, Maßeinheit, Definition, Plattform-ID, Alter seit Veröffentlichung und Datenquelle. Fehlende Metriken = null/unavailable, niemals null als 0 darstellen. Unterschiedliche Formate und Plattformdefinitionen nicht zusammenrechnen.
5. Neue Business-Quellen erfassen: Angebote, Prozesse, Community-Fragen, Ergebnisse und Entscheidungen. Kundenidentitäten bleiben im separaten privaten Vault; übertragbare Erkenntnisse nur in freigegebener anonymisierter Form verlinken.
   Ausgewählte Drive-Quellen und neue/geänderte Content-Skripte anhand Datei-ID, Änderungsdatum und Inhalts-Hash abgleichen. Originalfassungen und Quellenlinks erhalten; Skript-Video-Zuordnungen bestätigen und Abweichungen von der tatsächlichen Aufnahme getrennt dokumentieren. Kein gesamtes Drive-Konto ohne festgelegten Umfang einlesen.
6. Review erstellen: neue und offene Quellen, wiederholte Muster und Gegenbeispiele, mögliche Content-Experimente, nicht belegte Annahmen. Keine Kausalität aus Views ableiten.

Kein Hintergrundlauf ohne eingerichteten Scheduler. Für spätere Automatisierung Trigger, Laufumgebung, Budget und Fehlerbenachrichtigung mit Aku festlegen. Code und Daten bleiben getrennt; GitHub Actions verarbeitet keine privaten Medien als vermeintlichen Gratisrechner.
