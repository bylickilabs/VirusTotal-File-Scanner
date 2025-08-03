# 📘 Documentation (English)

## Overview

This application securely scans local files using the VirusTotal API.  
It combines a user-friendly GUI with the power of over 70 antivirus engines – without requiring local AV software installation.

## Key Features

- Local hashing of files (MD5, SHA1, SHA256, SHA512)
- Automated query to VirusTotal
- Language switcher (EN/DE)
- Export formats: JSON
- Progress display, status icons, file size display

## System Requirements

- Operating System: Windows 10/11
- Python: ≥ 3.8
- Internet connection for API lookups

## Configuration

- API key must be entered in `config.py`
- Sample configuration provided in `config.py.example`

## Security

- No file is stored or modified
- `app.py` is protected against unauthorized modification
- No sensitive data is shared with third parties

## License

Released under the MIT License. Use at your own risk.
[LICENSE](LICENSE)