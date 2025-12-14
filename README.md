Corporate Data Bridge: Legacy-to-Cloud Middleware

Business Case
Large organizations (Banks, Telecoms, Public Sector) often face a "Data Silo" problem. Critical business data is locked in legacy environments (Oracle/PL-SQL) that lack native modern API connectivity.

This Micro-Solution provides a resilient, low-cost bridge to synchronize legacy data with modern SaaS platforms without the overhead of enterprise-level ESB platforms.

Key Features
Decoupled Architecture: Separate modules for Data Extraction, Transformation, and API Delivery.

Resilience Engineering: Custom Python decorators handle network flickers with automated retry logic and exponential backoff.

Data Validation: Integrated validation layer prevents "garbage-in, garbage-out" by filtering malformed records before they hit production APIs.

Corporate Logging: Structured audit trails stored in /logs for easy troubleshooting and compliance monitoring.

CI/CD Ready: Automated testing suite via GitHub Actions to ensure code quality on every push.

🛠️ Tech Stack
Logic: Python 3.13

Data: Pandas (High-speed mapping & cleaning)

Testing: Pytest (Unit Testing)

Environment: Dotenv (Secure configuration)

📂 Project Structure
Plaintext
├── src/
│ ├── middleware.py # Core logic & sync engine
│ ├── utils.py # Resilience decorators & formatting
│ └── setup_mock_db.py # Legacy environment simulator
├── tests/
│ └── test_utils.py # Automated unit tests
├── .github/workflows/ # CI/CD Pipeline configuration
├── .env # Configuration & credentials (ignored by git)
└── requirements.txt # Production dependencies

⚙️ Installation & Usage
Clone & Install Dependencies:

Bash
pip install -r requirements.txt
Configure Environment: Create a .env file in the root directory (see .env.example if available).

Plaintext
DB_PATH=data/legacy_corp.db
API_ENDPOINT=https://httpbin.org/post
MAX_RETRIES=3
Initialize Mock Legacy Database:

Bash
python src/setup_mock_db.py
Execute Sync & Run Tests:

Bash

# Run the middleware

python src/middleware.py

# Run the test suite

python -m pytest
Delivered by the Micro-Solutions Delivery Team Speed. Reliability. Precision.
