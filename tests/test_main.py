from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add():
    response = client.post("/add", data={"a": 3.0, "b": 5.0})
    assert response.status_code == 200
    assert "Result: 8" in response.text
