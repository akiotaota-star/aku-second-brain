# Analysestandard für Akus Second Brain

Dieses Dokument definiert die gewünschte Qualität der Analyse. Es ist kein Nachweis, dass ein Video bereits angesehen oder eine technische Fähigkeit bereits getestet wurde. Das Starterpaket enthält keine echten Videos, Instagram-Inhalte, Kundeninformationen oder privaten Vault-Daten. Diese entstehen erst in Akus eingerichteter Umgebung.

## 1. Zuerst ein Quellenregister anlegen

Aku trägt die tatsächlichen URLs und Kennungen seiner YouTube- und Instagram-Accounts ein. Gleichlautende Namen reichen nicht zur eindeutigen Zuordnung. Das Quellenregister erfasst zunächst alle auffindbaren Videos und Reels innerhalb des festgelegten Umfangs, bevor die Einzelanalyse beginnt.

Für jede Quelle festhalten:

- Plattform, stabile Inhalts-ID, URL, Titel beziehungsweise Beschreibung.
- Veröffentlichungszeit, Dauer, Format und Zeitpunkt der Erfassung.
- Verfügbarkeit des Originals, der Untertitel und gegebenenfalls eigener Exporte.
- Bearbeitungsstatus: entdeckt, bereit zur Vorbereitung, vorbereitet, in Analyse, teilweise geprüft, geprüft oder blockiert.
- Grund für fehlende Inhalte, etwa gelöscht, privat, Zugriff fehlt oder Export fehlt.
- Verknüpfung zu lokalem Medienobjekt, Analyse und Kennzahlenschnappschüssen.

Ein öffentlich sichtbarer Katalog ist nicht automatisch vollständig. Eigene Originaldateien und Account-Exporte können zusätzliche Quellen liefern. Bereits gelöschte oder unzugängliche Inhalte werden als Lücke dokumentiert. Keine Zugangssperren umgehen und keine fehlenden Videos rekonstruieren. Gleiche Plattform-ID nicht erneut als neue Quelle anlegen. Crossposts über eine gemeinsame Werk-ID verbinden; unterschiedliche Fassungen getrennt erhalten.

## 2. Vorbereitung ist noch keine Sichtung

Die vorgesehene Vorbereitung erzeugt eine Übersicht mit einem Bild pro Sekunde, Videoclips von ungefähr 30 Sekunden mit der vollen Bewegungssequenz, eine Audiodatei und ein Prüfprotokoll in `coverage.jsonl`. Die tatsächlich vorhandenen Dateien und deren Eigenschaften müssen nach jedem Lauf geprüft werden. Ein erwartetes Dateiformat beweist weder erfolgreiche Extraktion noch eine abgeschlossene Analyse.

Die Einzelbilder dienen der Orientierung und dem Lesen sichtbarer Details. Schnelle Schnitte, sehr kurze Texteinblendungen oder Gesten zwischen zwei Bildern können fehlen. Bewegungen deshalb anhand der Videoclips prüfen, bei Bedarf langsamer und mit zusätzlichen Zwischenbildern. Übergänge an Clipgrenzen auf beiden Seiten kontrollieren. Ein tatsächlich beschädigter oder fehlender Abschnitt bleibt offen.

Vor der Auswertung festhalten, welches Werkzeug Bilder sehen, Videos abspielen und Audio verarbeiten kann. Unterstützt die aktuelle Claude-Code-Umgebung nur Bilder und Text, sind Ton- und Bewegungsprüfung damit nicht erledigt. Dann einen von Aku freigegebenen geeigneten Prüfweg verwenden oder die betreffenden Felder offen lassen. Dateien auf seinem Mac zu speichern bedeutet nicht automatisch, dass ein verwendeter Cloud-Modellanbieter keine Inhalte erhält; der gewählte Analyseweg muss dazu passen.

## 3. Ein Zeitraster für jede Sekunde

Für die gesamte gemessene Dauer gilt ein lückenloses Raster: `[0, 1)`, `[1, 2)` und so weiter. Das letzte Intervall endet an der tatsächlichen Videodauer und kann kürzer sein. Eine längere Beobachtung darf mehrere Intervalle abdecken, braucht aber genaue Grenzen. Keine künstliche Millisekundenpräzision aus groben Untertiteln ableiten.

Pro Intervall prüfen und mit Zeitbelegen erfassen:

| Bereich | Was dokumentiert wird |
| --- | --- |
| Aussage | Gesprochener Inhalt, Geschichte, Behauptung, Beispiel oder Handlungsaufforderung |
| Redeweise | Wortwahl, Satzbau, Tempo, Pausen und wiederkehrende Formulierungen |
| Hörbarer Vortrag | Betonung, Lautstärkeverlauf, Sprechmelodie, Lachen und andere tatsächlich gehörte Merkmale |
| Bild und Gestik | Körperhaltung, Handbewegung, Blickrichtung, Bewegung im Bild und sichtbare Reaktionen |
| Text und Gestaltung | Wortlaut sichtbarer Texte, Platzierung, Hervorhebung und Zeitpunkt der Einblendung |
| Schnitt und Ton | Schnitt, Zoom, B-Roll, Übergang, Musik, Soundeffekt und ihr zeitliches Zusammenspiel |
| Dramaturgie | Hook, Versprechen, Kontext, Spannung, Auflösung, Beleg oder CTA |

Nicht jede Sekunde benötigt eine neue Interpretation. Eine unveränderte Szene kann als zusammenhängender Zeitraum beschrieben werden. Das Prüfprotokoll muss trotzdem erkennen lassen, welche Intervalle tatsächlich untersucht wurden.

## 4. Sprache, Ton und Bewegung getrennt belegen

Untertitel und Transkripte gegen das verfügbare Audio prüfen, insbesondere Namen, Zahlen, Verneinungen und wichtige Zitate. Unverständliche Passagen markieren. Automatische Untertitel sind eine Ausgangsbasis und kein fehlerfreier Originaltext.

Ein Transkript kann Wortwahl zeigen. Es belegt keine hörbare Betonung, tatsächliche Lautstärke oder Sprechmelodie. Solche Angaben brauchen Audioevidenz. Wenn ein Abschnitt nachweislich still ist, diese Prüfung dokumentieren; Stille nicht aus einem leeren Transkript ableiten.

Ein Standbild kann eine Handposition zeigen. Es belegt keinen vollständigen Bewegungsverlauf. Aussagen wie „hebt die Hand beim Schlüsselwort und senkt sie danach“ brauchen die entsprechende Sequenz. Aus sichtbarer Haltung keine sichere innere Absicht oder Emotion ableiten.

## 5. Coverage-Protokoll und Abschluss

Die Felder `transcript_reviewed`, `visual_reviewed`, `motion_reviewed` und `audio_reviewed` werden nur nach der jeweiligen Prüfung gesetzt. Sie bedeuten:

- `transcript_reviewed`: Sprachinhalt im Intervall geprüft; vorhandene Unsicherheiten dokumentiert. Bei nachgewiesener Sprachlosigkeit ist diese Feststellung der Befund.
- `visual_reviewed`: Sichtbarer Inhalt und relevante Texte geprüft.
- `motion_reviewed`: Der Bewegungsverlauf des Intervalls einschließlich relevanter Übergänge geprüft.
- `audio_reviewed`: Das tatsächliche Audio geprüft; fehlende Tonspur oder Stille als geprüften Befund festgehalten.
- `evidence`: Nachprüfbare Verweise auf Quelle, Intervall, verwendete Datei beziehungsweise Clip und den zugehörigen Befund. Festhalten, welcher Mensch oder welches geeignete Werkzeug die Prüfung durchgeführt hat.

„Datei erzeugt“, „Transkript vorhanden“ und „Frame-Liste gelesen“ reichen zum Setzen dieser Felder nicht aus. Eine Unsicherheit kann trotz erfolgter Prüfung bestehen und muss erhalten bleiben. Ist ein Prüfweg technisch nicht verfügbar, bleibt das betreffende Feld offen.

Der Coverage-Validator prüft die formale Abdeckung und die erforderlichen Angaben. Er kann nicht beweisen, dass ein Mensch oder Modell wirklich hingesehen oder richtig interpretiert hat. Der Analyseabschluss braucht deshalb sowohl ein vollständiges Protokoll als auch nachvollziehbare Befunde. Lücken werden konkret mit Zeitbereich und Ursache gemeldet. Ein teilweise analysiertes Video darf bereits nützliche Notizen liefern, trägt aber den Status „teilweise geprüft“.

## 6. Performance und Zuschauerwirkung

Kennzahlen getrennt von der Inhaltsanalyse speichern: Plattform, Inhalts-ID, Messwert, Einheit, Quelle, Erfassungszeit und Bezugszeitraum. Fehlende Werte sind unbekannt, nicht die Zahl 0; in JSON `null` mit einem Grund verwenden. Spätere Messungen als neue Schnappschüsse ergänzen.

Öffentliche Views können ein Signal für Reichweite sein. Zuschauerbindung, Wiedergabedauer, Impressionen, Klickrate oder Conversions benötigen entsprechende Daten aus Akus Konten beziehungsweise Exporten und sind nicht für jedes Format gleichermaßen verfügbar. Ein sekündliches Analyseraster erzeugt keine sekündlichen Analytics. Die tatsächliche Auflösung der gelieferten Kennzahlen erhalten.

Vergleiche nur mit erkennbarem Kontext durchführen: Plattform, Format, Länge, Veröffentlichungsalter und, soweit bekannt, bezahlte Verbreitung. Mehr Views beweisen nicht, dass eine bestimmte Handbewegung oder ein bestimmter Hook die Ursache war.

Jeder Befund unterscheidet:

1. **Beobachtung:** Was hörbar oder sichtbar passiert; mit Zeitbeleg.
2. **Messwert:** Was die dokumentierte Kennzahlenquelle zeigt.
3. **Interpretation:** Welche Wirkung plausibel erscheint und worauf diese Einschätzung beruht.
4. **Experiment:** Welche gezielte Variation die Vermutung künftig überprüfbar macht.

Zuschauerkommentare als einzelne Rückmeldungen kennzeichnen. Sie repräsentieren nicht automatisch die gesamte Zuschauerschaft.

## 7. Vom Video zum verknüpften Wissen

Die Videoanalyse bleibt die Quelle. Daraus entstehen separate, verlinkte Notizen für Geschichten, Wissen, Redestil, Hooks, Editing-Muster und Kali Society. Jede abgeleitete Aussage verweist mindestens auf Inhalts-ID und Zeitbereich. Belegte Beobachtungen, Akus eigene Aussagen und Interpretationen dürfen nicht unmarkiert ineinander übergehen.

Wiederkehrende Geschichten erhalten eine gemeinsame Story-ID. In einer Story-Notiz stehen die Kernerzählung und alle belegten Varianten. Neue Details ergänzen, abweichende Zeitangaben oder widersprüchliche Fassungen sichtbar lassen. Keine glatte Biografie aus widersprüchlichen Videos erfinden. Ein lediglich ähnliches Motiv reicht nicht, um zwei Geschichten zusammenzuführen.

Ein Stilprofil entsteht aus mehreren belegten Beispielen und beschreibt auch Ausnahmen oder Veränderungen über die Zeit. Ein einzelner Hook ist ein Beispiel, noch keine allgemeine Regel. Jede Zusammenfassung nennt den untersuchten Umfang.

Kundenwissen getrennt von öffentlichen Content-Notizen pflegen. Nur von Aku bereitgestellte oder für diesen Arbeitsbereich freigegebene Informationen aufnehmen. Zuständigkeiten, vereinbarte Ziele, Entscheidungen und nächste Schritte mit Quelle und Datum erfassen. Private Kundenangaben nicht automatisch in Content-Ideen oder öffentlich teilbare Dokumente übernehmen. Diese Notizen und ihre Quellen gehören nicht in das GitHub-Starterpaket.

## 8. Start und laufende Pflege

Zuerst auf Akus Mac drei unterschiedliche eigene Inhalte als Pilot bearbeiten, etwa ein kurzes Reel, ein längeres Gespräch und ein stark geschnittenes Video. Prüfen, ob Audio, Bewegung, eingeblendete Texte, Quellenlinks und Coverage praktisch funktionieren. Speicherbedarf, Bearbeitungsdauer und gegebenenfalls Modellkosten messen. Anschließend den vollständigen Quellenkatalog in fortsetzbaren Chargen abarbeiten; eine Priorisierung ändert nicht den vereinbarten Gesamtumfang.

Neue Inhalte später demselben Verfahren zuführen. Änderungen an Analysen versioniert oder nachvollziehbar ergänzen. Kennzahlen regelmäßig nach Akus Bedarf aktualisieren. Rohmedien erst nach einer ausdrücklich festgelegten Aufbewahrungsregel entfernen; Belege und Wiederauffindbarkeit müssen dabei erhalten bleiben.
