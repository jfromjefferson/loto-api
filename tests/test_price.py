from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_valid_price():
    response = client.get("/price", params={"game_id": 1, "game_count": 1})

    assert response.status_code == 200
    assert response.json() == {"price": 3.00}


def test_invalid_price():
    response = client.get("/price", params={"game_id": 2, "game_count": 1})

    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid game id"}
