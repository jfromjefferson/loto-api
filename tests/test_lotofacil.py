import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

"""
Test scenarios for the GET /lotofacil/random route.:

game_count less than 1.
game_count greater than 50.
Valid game_count.
"""


def test_lotofacil_random_game_count_less_than_1():
    response = client.get("/lotofacil/random", params={"game_count": 0})

    assert response.status_code == 400
    assert response.json() == {"detail": "Game count must be greater than 0 and less or equal to 50"}


def test_lotofacil_random_game_count_greater_than_50():
    response = client.get("/lotofacil/random", params={"game_count": 51})

    assert response.status_code == 400
    assert response.json() == {"detail": "Game count must be greater than 0 and less or equal to 50"}


def test_lotofacil_random_valid_game_count():
    response = client.get("/lotofacil/random", params={"game_count": 5})

    data = response.json()

    assert response.status_code == 200
    assert len(data) == 5

    for game in data:
        assert "game" in game
        assert "numbers" in game
        assert "mirror" in game
        assert len(game["numbers"]) == 15
        assert len(game["mirror"]) == 15


def test_lotofacil_random_internal_server_error():
    with pytest.raises(Exception):
        response = client.get("/lotofacil/random", params={"game_count": 5})

        assert response.status_code == 500
