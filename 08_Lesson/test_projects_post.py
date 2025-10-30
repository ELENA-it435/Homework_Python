import requests

BASE_URL = "https://yougile.com/api-v2"


def test_create_project_positive(auth_headers):
    data = {"name": "New API Project"}
    response = requests.post(
        f"{BASE_URL}/projects",
        headers=auth_headers,
        json=data
    )
    assert response.status_code == 200
    assert response.json().get("id") is not None
    assert response.json().get("name") == data["name"]


def test_create_project_negative_no_name(auth_headers):
    data = {}
    response = requests.post(
        f"{BASE_URL}/projects",
        headers=auth_headers,
        json=data
    )
    assert response.status_code == 422
