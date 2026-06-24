from http import HTTPStatus

from fastapi.testclient import TestClient

from viajei_api.app import app


def test_create_user():
    client = TestClient(app)

    response = client.post(
        "/auth/",
        json={
            "email": "alice@example.com",
            "password": "secret",
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "email": "alice@example.com",
        "id": 1,
    }


def test_root_deve_retornar_ok_e_ola_mundo():
    # Arrange / Given
    client = TestClient(app)

    # Act / When
    response = client.get("/")

    # Assert / Then
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Bem vindo!"}
