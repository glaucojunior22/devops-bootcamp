from fastapi import status
from fastapi.testclient import TestClient

from app.main import TASKS, app


def test_list_tasks_status_code():
    client = TestClient(app)
    res = client.get("/tasks")
    assert res.status_code == status.HTTP_200_OK


def test_list_tasks_response_type():
    client = TestClient(app)
    res = client.get("/tasks")
    assert res.headers["Content-Type"] == "application/json"


def test_list_tasks_response_is_list():
    client = TestClient(app)
    res = client.get("/tasks")
    assert isinstance(res.json(), list)


def test_list_tasks_response_with_items():
    TASKS.append(
        {
            "id": "123",
            "title": "buy milk",
            "description": "buy some raw milk on bakery",
        }
    )
    client = TestClient(app)
    res = client.get("/tasks")
    assert "id" in res.json().pop()
    TASKS.clear()
