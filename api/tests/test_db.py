from sqlalchemy import select

from viajei_api.models import User


def test_create_user(session):
    new_user = User("joao@test.test", "senha123")

    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.email == "joao@test.test"))

    breakpoint()

    assert user.email == "joao"
