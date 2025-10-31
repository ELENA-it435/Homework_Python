import requests

BASE_URL = "https://yougile.com/api-v2"


def test_get_project_positive(auth_headers, create_project):
    project_id = create_project.get("id")
    response = requests.get(
        f"{BASE_URL}/projects/{project_id}",
        headers=auth_headers
    )
    assert response.status_code == 200
    assert response.json().get("id") == project_id


def test_get_project_negative_not_found(auth_headers):
    response = requests.get(
        f"{BASE_URL}/projects/999999999",
        headers=auth_headers
    )
    assert response.status_code == 404
