import falcon
from falcon import testing
import pytest

from app.run import api

@pytest.fixture
def client():
    return testing.TestClient(api)

def test_list_images(client):

    response = client.simulate_get('/')

    assert response.status == falcon.HTTP_OK
