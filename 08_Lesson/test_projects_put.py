import requests

BASE_URL = "https://yougile.com/api-v2"


def test_update_project_positive(auth_headers, create_project):
    project_id = create_project["id"]
    new_name = "Updated Project Name"
    response = requests.put(
        f"{BASE_URL}/projects/{project_id}",
        headers=auth_headers,
        json={"name": new_name},
    )
    assert response.status_code == 200
    assert response.json()["name"] == new_name


def test_update_project_negative_invalid_id(auth_headers):
    response = requests.put(
        f"{BASE_URL}/projects/invalid_id",
        headers=auth_headers,
        json={"name": "Invalid Update"},
    )
    assert response.status_code == 404
