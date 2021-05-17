from starlette.testclient import TestClient
from app.database import SessionLocal
from main import app



client = TestClient(app)

db = SessionLocal()

def test_main_status_code():
    response = client.get("/")
    assert response.status_code == 200

def test_main_reponse_json():
    response = client.get("/")
    assert response.json() == {'pagina': 'inicial'}

def test_read_breeds():
    response = client.get("breed/all")
    assert response.status_code == 200

def test_create_breeds():
    response = client.get("/breed/create")
    assert response.status_code == 200

def test_delete_breeds():
    response = client.get("/breed/delete")
    assert response.status_code == 200

def test_update_breeds():
    response = client.get("/breed/update")
    assert response.status_code == 200

def test_location_breeds():
    response = client.get("/location/Thailand")
    assert response.status_code == 200

def test_body_breeds():
    response = client.get("/body/Fit")
    assert response.status_code == 200

def test_coat_breeds():
    response = client.get("/coat/Long-haired")
    assert response.status_code == 200

def test_pattern_breeds():
    response = client.get("/pattern/Solid")
    assert response.status_code == 200

