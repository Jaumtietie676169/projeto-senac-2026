from http import HTTPStatus


def test_create_user(client):

    response = client.post(
        "/users/",
        json={
            "email": "joao@example.com",
            "password": "secret",
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "email": "joao@example.com",
        "id": 1,
    }


def test_root_deve_retornar_ok_e_ola_mundo(client):

    # Act / When
    response = client.get("/")

    # Assert / Then
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Bem vindo!"}


def test_read_users(client):

    response = client.get("/users/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": [
            {
                "email": "joao@example.com",
                "id": 1,
            }
        ]
    }


def test_delete_user(client):
    # When
    response = client.delete("/users/1")

    # Then
    response.status_code = HTTPStatus.OK
    response.json() == {"message': 'User deleted!"}
