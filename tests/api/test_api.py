import requests
import requests_mock

def test_api_is_working():
    with requests_mock.Mocker() as m:
        m.get("https://jsonplaceholder.typicode.com/posts/1, text='{"status": "ok"}', status_code=200)
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        assert response.status_code == 200
test_api_is_working()
