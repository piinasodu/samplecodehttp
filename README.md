# API Automation & HAR Replay Toolkit

A Python-based automation toolkit for parsing HAR files and emulating API workflows with browser-like TLS fingerprinting.

This project demonstrates:

- HAR file parsing
- API request reconstruction
- Session & cookie persistence
- Proxy support
- User-agent spoofing
- TLS fingerprint impersonation (via curl_cffi)
- Async & multithreaded request execution
- Structured logging and error handling

---

## 🔧 Features

- Extract API requests from `.har` files
- Replay API flows programmatically
- Support for:
  - requests
  - httpx (async)
  - curl_cffi (browser TLS impersonation)
- Proxy rotation support
- Modular reusable HTTP client
- Logging + retry handling
- HTTP/2 support

---

## 📂 Project Structure

.
├── har_parser.py
├── api_client.py
├── requirements.txt
└── README.md


---

## 📦 Installation

```bash
git clone https://github.com/yourusername/api-automation-toolkit.git
cd api-automation-toolkit
pip install -r requirements.txt

Network traffic reproduction

