import pytest # pyright: ignore[reportMissingImports]
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello(client):
    response = client.get('/')
    assert response.data == b"Hello World from Flask app!"
    assert response.status_code == 200