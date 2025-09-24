import pytest
from flaskapp import app

@pytest.fixture()
def client():
    return app.test_client()

def test_home(client):
    response = client.get('/')
    assert b"Rick Astley" in response.data

def test_add(client):
    response = client.get('/add?a=3&b=5')
    assert b"3 + 5 = 8" in response.data

def test_sub(client):
    response = client.get('/sub?a=8&b=3')
    assert b"8 - 3 = 5" in response.data

def test_reverse(client):
    response = client.get('/reverse?q=jill')
    assert b"llij" in response.data