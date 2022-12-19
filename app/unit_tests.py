from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/he/יטבתה/")
    assert response.status_code == 200
    assert response.json() == {"x":3903203.82722753,"y":3490059.52844124}

    response = client.get("/en/ETANIM")
    assert response.status_code == 200
    assert response.json() == {"x":3906834.0339361,"y":3734246.74323138}
