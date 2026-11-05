# SIMULATOR-X Sprint Status

## Sprint 0 — Foundation
- Python package layout and project metadata.
- Environment template and Git ignore rules.
- Termux installation and quick-start instructions in README.
- Localhost-only default bind configuration.

## Sprint 1 — API foundation
- FastAPI application and `/health` endpoint.
- SQLAlchemy engine/session setup and SQLite schema initialization.
- `run.py` development entry point.
- API smoke-test coverage for health endpoint.

## Sprint 2 — Virtual test profiles
- Create, list, retrieve, update and delete synthetic profiles.
- Activate/deactivate profile state.
- Pydantic input validation and SQLite persistence.
- Explicit `TEST-IMSI-` and `TEST-ICCID-` identifiers.
- API tests cover CRUD, activation, not-found and validation cases.

## Planned
- Sprint 3: isolated APDU command simulator.
- Sprint 4: simulated network scenarios.
- Sprint 5: browser dashboard.
- Sprint 6: integration and QA.
- Sprint 7: packaging and handover.

## Verification
Source files have been committed to GitHub. The test suite has not yet been executed on the target Android/Termux device. Run `pip install -e ".[dev]"` and `pytest` before client acceptance.

## Security boundary
This is an offline simulator using synthetic test identifiers. It does not clone live SIM credentials, perform carrier authentication, intercept OTPs, or register a subscriber on a mobile network.
