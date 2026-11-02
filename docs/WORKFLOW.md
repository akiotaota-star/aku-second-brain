# Gesamtablauf: vom Archiv zum nutzbaren Gedächtnis

## 1. Quelleninventar bei Aku

Vor dem Inventar führt Claude den [Onboarding-Dialog](ONBOARDING.md): pro Schritt eine konkrete Frage, Antworten und Lieferungen prüfen, Fortschritt speichern. Google Drive und sämtliche vorhandenen Content-Skripte gehören ausdrücklich zum Bestand, auch ältere bereits verwendete Fassungen. Ausgewählte Drive-Dateien über einen verfügbaren autorisierten Zugang oder lokale Exporte erfassen. Dateikennung, Version, Originalquelle und Importstatus erhalten. Eine `.gdoc`-Verknüpfung allein enthält keinen auswertbaren Dokumenttext.

YouTube-Kanal und Instagram-Profil über bestätigte URLs zuordnen. Alle verfügbaren Videos, Shorts, Reels und sonstigen gewünschten Beiträge mit Plattform-ID inventarisieren, bevor eine Stichprobe zum Pilot gewählt wird. Paginierung, Zeitbereich, Inventurdatum und nicht zugängliche Inhalte festhalten. „Alle“ bedeutet alle Quellen des dokumentierten Katalogs; private, gelöschte oder abgelaufene Inhalte können nur über Akus eigene Originale/Exporte ergänzt werden.

Pro Quelle: ID, URL, Titel, Veröffentlichungsdatum, Format, Dauer, Status, Importweg und letzter Fehler. Medien erst in Akus Umgebung abrufen. Dasselbe Video auf zwei Plattformen erhält zwei Veröffentlichungsdatensätze mit verknüpfter gemeinsamer Medien-/Story-ID. Die Views werden nicht zusammengeworfen.

## 2. Drei Pilotvideos, danach vollständiger Backlog

Ein kurzes, ein langes und ein visuell dichtes Video prüfen. Zeit, Speicher und tatsächliche Modellkosten messen. Den gesamten Katalog anhand der Dauer auf Aufwand hochrechnen; Schätzungen als solche markieren. Das Pilotpaket dient zum Prüfen des Ablaufs. Danach werden alle registrierten Videos in fortsetzbaren Batches bearbeitet, auch schwach performende.

Jobzustände: `registered → imported → prepared → reviewing → documented_complete → quality_checked`. Daneben `partial`, `blocked_access`, `failed`. `brain.py` implementiert Vorbereitung und Dokumentationsprüfung; Registerzustände und Freigabe nach Qualitätsprüfung pflegt Claude. Unverarbeitete Daten bleiben im Backlog sichtbar.

## 3. Watch: Inhalt, Auftreten und Schnitt

Pro Video vollständiges Transkript, Sekundenprotokoll und zusammenhängende Bild-/Audio-Sichtung. Erst echte Belege, dann Interpretation. Ein verwertbares Videoergebnis enthält:

- Wissen und Aussagen, getrennt nach überprüfbarem Fakt, Akus eigener Aussage und Interpretation.
- Stories: Kernereignis, Pointe, Konflikt/Wandel, verschiedene Erzählfassungen, offene Widersprüche.
- Redeart: Vokabular, Satzbau, Wiederholungen, Pausen, Tempo, Betonung, Lautstärke und Tonhöhenverlauf, soweit tatsächlich geprüft.
- Auftreten: sichtbare Handbewegungen, Blickrichtung, Körperhaltung, Timing zur Sprache. Keine Charakterdiagnosen.
- Hook: genauer Wortlaut/Visual, Zeitfenster, Versprechen, offene Frage, Payoff und CTA.
- Editing: Schnitte, Einblendungen, Typografie, Caption-Timing, B-Roll, Zooms, Übergänge, Musik und Sounddesign.
- Zuschauerwirkung: klar markierte Hypothesen; Kommentare und Analytics als getrennte Evidenz.

Maßgeblich ist der [Analysestandard](ANALYSESTANDARD.md). Ein 60-Minuten-Video hat 3.600 Sekundenintervalle, auch wenn die Zusammenfassung nur eine Seite lang ist. Ein 1-fps-Raster allein sieht keine kurze Einblendung zwischen den Bildern.

## 4. Aus Quellen verknüpftes Wissen machen

Content-Skripte sind eigene Quellen. Die Zuordnung zu einer Veröffentlichung bestätigen oder als Kandidat markieren. Geplanten Hook, Argumentation und CTA mit dem tatsächlich gesprochenen Wortlaut und der visuellen Umsetzung vergleichen. Ein altes Skript nicht nachträglich an das Video anpassen; Unterschiede als eigene Beobachtungen erhalten. Nicht verwendete Entwürfe sind Ideenquellen und keine Belege für Akos bisherigen Auftritt.

Eine Videonotiz verlinkt Transcript, Medien, Zeitprotokoll und Erkenntnisse. Ein Wissenseintrag enthält einen klaren Claim statt einer Kopie der gesamten Zusammenfassung. Stories bekommen stabile IDs; verschiedene Videos können dieselbe Story belegen. Stilnotizen enthalten Beispiele, Gegenbeispiele, Zeitraum und Konfidenz. Neuere Entwicklungen ersetzen ältere Muster nicht rückwirkend.

Bei späteren Fragen sucht Claude zunächst diese kleinen Notizen. Nur die relevanten Originalbelege werden nachgeladen. So wird das Archiv nutzbar, ohne bei jeder Frage tausende Frames erneut zu verarbeiten.

## 5. Performance als eigene Datenreihe

Öffentliche Zahlen und eigene Analytics getrennt speichern. Pro Snapshot: Plattform, Video-ID, Erfassungszeitpunkt, Veröffentlichungsalter, Berichtszeitraum, Metrikname, Einheit, Wert, Definition und Quelle. Verfügbare Größen können Views, Watchtime, Retention, Reichweite, Likes, Saves, Shares oder Klicks sein; Verfügbarkeit hängt vom Konto und Zugriff ab.

Nicht verfügbare Werte bleiben null mit Grund. Ein heute erfasster Lifetime-Wert ist kein rekonstruierter Wert vom siebten Tag. Künftige Tag-1-/Tag-7-/Tag-30-Snapshots können nach eingerichteter Zeitplanung gesammelt werden. Formate, Länge, Alter und Plattform beim Vergleich berücksichtigen. Eigene YouTube-Analytics benötigen Autorisierung. Instagram-Zugangsweg und verfügbare Kennzahlen beim Setup aktuell prüfen; dieses Paket behauptet keine überprüfte Instagram-API-Integration.

„Dieser Hook hatte mehr Views“ ist eine Beobachtung über das Video. „Diese Handbewegung verursachte die höheren Views“ ist damit nicht belegt. Experimente entsprechend als Hypothesen planen.

## 6. Kali Society und Kundenwissen

Zusätzlich zu Social Content: bestätigte Angebote, Positionierung, Abläufe, Community-Themen, Ziele, Entscheidungen und freigegebene Gesprächsnotizen erfassen. Jede Notiz hat Quelle, Datum und Gültigkeit. Veraltete Preise oder Angebote sichtbar als überholt markieren.

Identifizierende Kundenakten, Kontakte, konkrete Gesprächsdetails und private Zuordnungen liegen in `private-vault`. Öffentliche Case Studies sind erst nach entsprechender Freigabe Content-Quellen. Allgemeine Learnings aus Kundenarbeit werden als anonymisierte Muster verlinkt; Namen oder Fallgeschichten nicht automatisch veröffentlichbar machen. Ein Namenswechsel allein garantiert keine Anonymität.

## 7. Alltagsnutzung und Aktualisierung

Beispielaufträge:

- „Welche meiner Geschichten passen zu diesem Thema? Zeige mir die Originalstellen.“
- „Entwirf drei Hooks und ein Skript in meinem belegten Stil; markiere kreative Ergänzungen.“
- „Erstelle ein Editing-Briefing mit Referenzstellen aus meinem Archiv.“
- „Welche Annahmen zu unseren Angeboten sind veraltet?“
- „Was können wir aus den jüngsten Reels lernen, unter Berücksichtigung ihres Alters?“

`/brain-update` ergänzt neue Quellen und Kennzahlen; `/brain-use` sucht, erfasst oder entwirft. Ein wöchentlicher Review ist zunächst ein manuell gestarteter Workflow. Dauerhafte Planung erst bei Aku einrichten, inklusive Kostenrahmen, Fehlerbehandlung und ruhiger Benachrichtigung bei unverändertem Zustand.

## Abnahme vor dem kompletten Archiv

Alle drei Pilotvideos haben belegte Sichtung oder ausdrücklich benannte Lücken. Mindestens eine Story, ein Stilmerkmal und eine Business-Erkenntnis sind mit Originalquelle auffindbar. Eine Antwort kann vom Claim zur relevanten Videosekunde zurückverfolgt werden. Ein unterbrochener Job lässt sich fortsetzen. Ein Restore-Test zeigt, dass Vault und relevante Quellen aus dem Backup wiederherstellbar sind. Keine realen Inhalte liegen im Repository.
