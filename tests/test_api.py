from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_scrape_endpoint_success():
    response = client.post("/scrape", json={"url": "https://www.google.com/recaptcha/api2/demo"})
    assert response.status_code == 200

