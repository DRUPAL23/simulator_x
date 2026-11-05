# SIMULATOR-X

Offline Android/Termux SIM-behaviour test harness using synthetic data only.

## Scope
SIMULATOR-X models selected SIM-like profile metadata and protocol behaviour inside an isolated software sandbox. It does not replace Android's physical SIM, register with a carrier, clone live subscriber credentials, intercept OTPs, or bypass cellular authentication.

## Sprints
- Sprint 0: repository foundation, architecture, configuration and Termux setup.
- Sprint 1: FastAPI application, SQLite initialization, health endpoint and smoke tests.
- Sprint 2: synthetic virtual-profile CRUD, activation state, validation and tests.
- Sprint 3 (planned): isolated APDU command simulator.
- Sprint 4 (planned): simulated network scenarios.
- Sprint 5 (planned): browser dashboard.

## Quick start (Termux)
```bash
pkg update && pkg upgrade -y
pkg install python git -y
git clone https://github.com/DRUPAL23/simulator_x.git
cd simulator_x
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env
pytest
python run.py
```
Open `http://127.0.0.1:8000/docs` on the Android device.

## Data safety
Use generated test-only identifiers. Never enter IMSI, ICCID, Ki, OPc, PIN/PUK or other secrets from a real subscriber SIM. Bind the development API to `127.0.0.1` by default.

## Development status
The repository is being populated with Sprint 0 foundation and Sprint 1/2 implementation files. Validate on the target Android/Termux device before client acceptance.