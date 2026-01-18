import pytest
from main import app as flask_app 

@pytest.fixture
def client():
    with flask_app.test_client() as client:
        yield client

def test_exam_page(client):
    res = client.get("/exam/assign")
    assert res.status_code == 200