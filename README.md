# 🌉 Corporate Data Bridge: Legacy-to-Cloud Middleware

[![Python CI/CD Pipeline](https://github.com/micro-solutions-team/micro-middleware-sync/actions/workflows/python-app.yml/badge.svg)](https://github.com/micro-solutions-team/micro-middleware-sync/actions)
![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

## 💼 Business Case
Large organizations (Banks, Telecoms, Public Sector) often face a **"Data Silo"** problem. Critical business data is locked in legacy environments (Oracle/PL-SQL) that lack native modern API connectivity. 

This **Micro-Solution** provides a resilient, low-cost bridge to synchronize legacy data with modern SaaS platforms without the overhead and complexity of enterprise-level ESB platforms.



---

## ✨ Key Features
* **Decoupled Architecture:** Separate modules for Data Extraction, Transformation, and API Delivery.
* **Resilience Engineering:** Custom Python decorators handle network flickers with automated retry logic and exponential backoff.
* **Data Validation:** Integrated validation layer prevents "garbage-in, garbage-out" by filtering malformed records before they hit production APIs.
* **Corporate Logging:** Structured audit trails stored in `/logs` for easy troubleshooting and compliance monitoring.
* **CI/CD Ready:** Automated testing suite via GitHub Actions to ensure code quality on every push.

---

## 🛠️ Tech Stack
* **Logic:** `Python 3.13`
* **Data Processing:** `Pandas` (High-speed mapping & cleaning)
* **Testing:** `Pytest` (Unit Testing)
* **Configuration:** `Dotenv` (Secure environment management)

---

## 📂 Project Structure
```text
├── src/
│   ├── middleware.py      # Core logic & sync engine
│   ├── utils.py           # Resilience decorators & formatting logic
│   └── setup_mock_db.py   # Legacy environment simulator (SQLite)
├── tests/
│   └── test_utils.py      # Automated unit tests
├── .github/workflows/     # CI/CD Pipeline (GitHub Actions)
├── .env                   # Configuration & credentials (GIT IGNORED)
└── requirements.txt       # Production dependencies
