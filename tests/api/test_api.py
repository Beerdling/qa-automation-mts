import requests

def test_api_is_working():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    print("Статус код:", response.status_code)  # Проверяем статус
    assert response.status_code == 200, "API сломался!"
    print("API работает")

test_api_is_working()
