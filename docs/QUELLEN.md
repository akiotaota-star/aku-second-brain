# Technische Quellen und Grenzen

Für die Paketkonzeption am 02.11.2026 geprüft. Konkrete Accountverfügbarkeit und Modellfähigkeiten müssen bei Aku getestet werden.

- [Claude Code – Skills](https://code.claude.com/docs/en/skills): Projekt-Skills unter `.claude/skills`. Dieses Paket richtet sich an lokale Terminal-Sitzungen; Cloud-/Cowork-Sitzungen haben teils andere Ladewege.
- [Claude Code – Setup](https://code.claude.com/docs/en/setup): Installation und Laufzeitvoraussetzungen.
- [Claude Code – Security](https://code.claude.com/docs/en/security) und [Data usage](https://code.claude.com/docs/en/data-usage): Berechtigungen und Verarbeitung durch Modellanbieter. Lokale Dateiverarbeitung ist kein Versprechen vollständig lokaler Inferenz.
- [Obsidian – Datenspeicherung](https://help.obsidian.md/Files+and+folders/How+Obsidian+stores+data): Vault als lokaler Ordner mit Markdown-Dateien; externe Änderungen werden übernommen.
- [YouTube Analytics – Zeitdimensionen](https://developers.google.com/youtube/analytics/dimensions#elapsedVideoTimeRatio): Retention mit 100 relativen Punkten; keine allgemeine Sekundengenauigkeit.
- [Instagram Platform – Insights](https://developers.facebook.com/docs/instagram-platform/insights/): Einstieg für die spätere Integration. Die Meta-Seite war während der Konzeption nicht abrufbar. Berechtigungen, Kontotypen, verfügbare Metriken und Fristen werden daher ausdrücklich nicht als aktuell verifiziert behauptet.

Der persönliche Watch-Skill des Paketautors wurde auf Übertragbarkeit geprüft. Seine fest eingebauten Speicherpfade und seine begrenzte Frameauswahl werden nicht übernommen. Der Python-Adapter und die Projekt-Skills hier wurden eigenständig geschrieben; es werden keine Upstream-Skripte oder persönlichen Konfigurationsdateien verteilt.

Dies ist ein Installations- und Arbeitsablaufpaket mit funktionsfähigem lokalem Adapter, kein fertig integriertes Social-Media-Archivsystem. Keine Accounts, echten Videos oder Kundeninformationen wurden für seine Erstellung importiert.
