# 🛡️ VirusTotal File Scanner

![Logo](/assets/logo.png)

- A local Python-based graphical application to scan files using with the free [VirusTotal Public API v3](https://www.virustotal.com/) 
  - and display scan results, hash values, and detection details.

<br>

---

<br>

## 🎯 Features

- 📁 Upload and scan local files
- 🔐 Auto-generate hashes: **MD5**, **SHA-1**, **SHA-256**, **SHA-512**
- 🌍 Language switcher: English / German
- 🌗 Light / Dark mode toggle
- 🧾 Export full scan result as `.json`
- ℹ️ Info popup (localized)
- 🔗 GitHub button (custom link)

<br>

---

<br>

## 🧰 Technologies Used

- `Tkinter` – native Python GUI
- `requests` – for VirusTotal API access
- `hashlib` – to calculate file hashes
- `webbrowser` – to open GitHub link

<br>

---

<br>

## 🔑 API Key Setup

To use the VirusTotal API, you need a **free personal API key**.

<br>

---

<br>

### How to get your API key:

1. Register at HERE ► [VIRUSTOTAL](https://www.virustotal.com/gui/join-us)
2. Go to your **profile > API key**
3. Copy the key and paste it into `config.py` like this:

```yarn
config.py
API_KEY = "YOUR_API_KEY_HERE"
```

> ⚠️ Make sure the `config.py` file is in the same folder as `app.py`.

<br>

---

<br>

## 🚀 How to Run

```yarn
pip install requests
python app.py
```

<br>

---

<br>

## 📂 File Structure

```yarn
project/
├── pyarmor_runtime_000000  # Deleting this directory will break the functionality of app.py
├── app.py              	# Main GUI application
├── config.py           	# Contains your VirusTotal API key
├── README.md           	# Project documentation
```

<br>

---

<br>

## 📤 Export

You can export scan results including hash values and metadata by clicking  
**Export Result as JSON** after a successful scan.

<br>

---

<br>

## 📌 Notes

- This tool does **not store or share any files or results** except with VirusTotal.
- The API is rate-limited for free accounts – consider upgrading for higher usage.

```yarn
Request rate	4 lookups / min
Daily quota	    500 lookups / day
Monthly quota	15.5 K lookups / month
```

<br>

---

<br>

## 🔗 GitHub

[bylickilabs GitHub Repository](https://github.com/bylickilabs)

<br>

---

<br>

## 📜 License

MIT License [LICENSE](LICENSE)

<br>

---

<br>

### 🔐 Application Protection Notice

- After several days of dedicated development work, I have taken the decision to protect this application against unauthorized use, 
  - duplication, or modification. The `app.py` file has therefore been secured accordingly.

> Please understand that this protection is solely intended to preserve the application's integrity and to honor the time and creativity invested in its development.

<br>

---

<br>

📩 For legitimate inquiries regarding reuse or integration, feel free to contact me.  
Thank you for your understanding and respect!