import requests
import requests_mock

def test_api():
    with requests_mock.Mocker() as m:
        m.get(
            "https://jsonplaceholder.typicode.com/posts/1",
            json={"status": "ok"},  # Используем json вместо text
            status_code=200
        )
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        assert response.status_code == 200
        assert response.json()["status"] == "ok"
