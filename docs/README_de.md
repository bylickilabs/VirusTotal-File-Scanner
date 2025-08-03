# 🛡️ VirusTotal File Scanner

![Logo](/assets/logo.png)

Eine lokale, Python-basierte grafische Anwendung zur Analyse von Dateien mit der kostenlosen [VirusTotal Public API v3](https://www.virustotal.com/)  
– inklusive Anzeige von Scan-Ergebnissen, Hash-Werten und Erkennungsdetails.

<br>

---

<br>

## 🎯 Funktionen

- 📁 Lokale Dateien hochladen und scannen  
- 🔐 Automatische Hash-Berechnung: **MD5**, **SHA-1**, **SHA-256**, **SHA-512**  
- 🌍 Sprachumschalter: Englisch / Deutsch  
- 🌗 Light- / Darkmode-Umschaltung  
- 🧾 Export des vollständigen Scan-Ergebnisses als `.json`  
- ℹ️ Info-Popup (mehrsprachig)  
- 🔗 GitHub-Button (individuell verlinkt)  

<br>

---

<br>

## 🧰 Verwendete Technologien

- `Tkinter` – native Python-GUI  
- `requests` – für die Kommunikation mit der VirusTotal API  
- `hashlib` – zur Berechnung der Hash-Werte  
- `webbrowser` – zum Öffnen des GitHub-Links  

<br>

---

<br>

## 🔑 API-Schlüssel einrichten

Zur Nutzung der VirusTotal API wird ein **kostenloser persönlicher API-Key** benötigt.

<br>

---

<br>

### So erhalten Sie Ihren API-Schlüssel:

1. Registrieren Sie sich hier ► [VIRUSTOTAL](https://www.virustotal.com/gui/join-us)  
2. Öffnen Sie **Profil > API Key**  
3. Kopieren Sie den Schlüssel und fügen Sie ihn in die Datei `config.py` ein:

```yarn
config.py
API_KEY = "DEIN_API_KEY_HIER"
```

> ⚠️ Achten Sie darauf, dass sich die Datei `config.py` im selben Verzeichnis wie `app.py` befindet.

<br>

---

<br>

## 🚀 Anwendung starten

```bash
pip install requests
python app.py
```

<br>

---

<br>

## 📂 Projektstruktur

```yarn
project/
├── pyarmor_runtime_000000  # Das Löschen dieses Verzeichnisses führt zum Funktionsverlust von app.py
├── app.py                  # Hauptanwendung (GUI)
├── config.py               # Enthält deinen VirusTotal API-Schlüssel
├── README.md               # Projektdokumentation
```

<br>

---

<br>

## 📤 Exportfunktion

Nach einem erfolgreichen Scan kannst du das Ergebnis inklusive Hash-Werten und Metadaten exportieren –  
einfach auf **Ergebnis als JSON exportieren** klicken.

<br>

---

<br>

## 📌 Hinweise

- Diese Anwendung **speichert oder teilt keine Dateien oder Ergebnisse**, mit Ausnahme der Übertragung an VirusTotal.  
- Die kostenlose API ist rate-limitiert – für höhere Nutzung ist ein Upgrade empfehlenswert.

```yarn
Anfrage-Limit:   4 Abfragen / Minute  
Tageslimit:      500 Abfragen / Tag  
Monatskontingent: 15.500 Abfragen / Monat  
```

<br>

---

<br>

## 🔗 GitHub

[bylickilabs GitHub Repository](https://github.com/bylickilabs)

<br>

---

<br>

## 📜 Lizenz

MIT-Lizenz [LICENSE](LICENSE)

<br>

---

<br>

### 🔐 Hinweis zum Anwendungsschutz

> Nach mehreren Tagen intensiver Entwicklungsarbeit habe ich die Entscheidung getroffen, diese Anwendung gegen unautorisierte Nutzung,  
  - Duplizierung oder Modifikation zu schützen. Die Datei `app.py` wurde entsprechend abgesichert.

> Dieser Schutz dient ausschließlich dem Erhalt der Integrität der Anwendung, und soll die investierte Zeit sowie die kreative Leistung würdigen.

<br>

---

<br>

📩 Bei berechtigten Anfragen zur Weiterverwendung oder Integration nehmen Sie gerne Kontakt mit mir auf.  
Vielen Dank für Ihr Verständnis und Ihren Respekt!
