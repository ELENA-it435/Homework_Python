import pytest
import requests

BASE_URL = "https://yougile.com/api-v2"


@pytest.fixture(scope="session")
def auth_headers():
    token = "ВАШ_ТОКЕН_ДОСТУПА"
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }


@pytest.fixture()
def create_project(auth_headers):
    data = {"name": "Temp Test Project"}
    response = requests.post(
        f"{BASE_URL}/projects",
        headers=auth_headers,
        json=data
    )
    assert response.status_code == 200
    project = response.json()

    yield project

    requests.delete(
        f"{BASE_URL}/projects/{project['id']}",
        headers=auth_headers
    )
