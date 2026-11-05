import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from simulator_x.database.db import Base, get_db
from simulator_x.main import create_app
@pytest.fixture
def client():
    engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
    TestingSession = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    Base.metadata.create_all(bind=engine)
    def override_db():
        db = TestingSession()
        try: yield db
        finally: db.close()
    app = create_app(); app.dependency_overrides[get_db] = override_db
    with TestClient(app) as test_client: yield test_client
    app.dependency_overrides.clear(); Base.metadata.drop_all(bind=engine)
def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200 and response.json()["status"] == "ok"
def test_profile_crud_and_activation(client):
    response = client.post("/api/v1/profiles", json={"profile_name":"Lab profile", "operator_name":"Example operator", "country_code":"ZZ"})
    assert response.status_code == 201
    item = response.json(); pid = item["id"]
    assert item["test_imsi"].startswith("TEST-IMSI-") and item["test_iccid"].startswith("TEST-ICCID-")
    assert item["active"] is False
    assert client.get(f"/api/v1/profiles/{pid}").status_code == 200
    changed = client.put(f"/api/v1/profiles/{pid}", json={"profile_name":"Updated lab"})
    assert changed.status_code == 200 and changed.json()["profile_name"] == "Updated lab"
    activated = client.patch(f"/api/v1/profiles/{pid}/status", json={"active":True})
    assert activated.status_code == 200 and activated.json()["active"] is True
    assert client.get("/api/v1/profiles").status_code == 200
    assert client.delete(f"/api/v1/profiles/{pid}").status_code == 204
    assert client.get(f"/api/v1/profiles/{pid}").status_code == 404
def test_validation_rejects_bad_profile(client):
    response = client.post("/api/v1/profiles", json={"profile_name":"x", "operator_name":"Example", "country_code":"bad"})
    assert response.status_code == 422
