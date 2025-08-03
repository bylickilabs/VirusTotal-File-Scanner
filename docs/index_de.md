# 📘 Dokumentation (Deutsch)

## Übersicht

Diese Anwendung dient dem sicheren lokalen Scannen von Dateien mithilfe der VirusTotal API.  
Sie kombiniert die Einfachheit einer GUI mit der Leistungsfähigkeit von über 70 Antiviren-Engines – ohne lokale Installation eines AV-Produkts.

## Hauptfunktionen

- Lokales Hashing von Dateien (MD5, SHA1, SHA256, SHA512)
- Automatisierte Abfrage bei VirusTotal
- Sprache umschaltbar (DE/EN)
- Exportformate: JSON
- Fortschrittsanzeige, Statussymbole, Dateigröße-Anzeige

## Systemanforderungen

- Betriebssystem: Windows 10/11
- Python: ≥ 3.8
- Internetverbindung für API-Abfragen

## Konfiguration

- API-Schlüssel muss in `config.py` eingetragen werden.
- Beispielkonfiguration in `config.py.example`

## Sicherheit

- Keine Datei wird gespeichert oder verändert.
- Die Datei `app.py` ist vor Manipulation geschützt.
- Es werden keine sensitiven Daten mit Dritten geteilt.

## Lizenz

Veröffentlicht unter der MIT-Lizenz. Nutzung auf eigene Verantwortung.
[LICENSE](LICENSE)