import requests

BASE_URL = "https://yougile.com/api-v2"


def test_create_project_positive(auth_headers):
    data = {"name": "New API Project"}
    response = requests.post(f"{BASE_URL}/projects", headers=auth_headers, json=data)
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["name"] == data["name"]


def test_create_project_negative_no_name(auth_headers):
    data = {}
    response = requests.post(f"{BASE_URL}/projects", headers=auth_headers, json=data)
    assert response.status_code in [400, 422]
