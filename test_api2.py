# test_api.py
import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"  # Замени на реальный API МТС


def print_test_header(test_name):
    print(f"\n{'=' * 50}")
    print(f"Тест: {test_name}")
    print(f"{'=' * 50}")


def print_test_result(result, response=None):
    if result:
        print("✅ Тест пройден успешно")
    else:
        print("❌ Тест не пройден")

    if response is not None:
        print("\nДетали ответа:")
        print(f"Статус код: {response.status_code}")
        print(f"Ответ сервера: {response.text}")


def test_get_user():
    """Проверка получения данных пользователя"""
    print_test_header("Получение данных пользователя")
    try:
        response = requests.get(f"{BASE_URL}/users/1")
        status_ok = response.status_code == 200
        name_ok = response.json()["name"] == "Leanne Graham"

        print_test_result(status_ok and name_ok, response)
        assert status_ok
        assert name_ok
    except Exception as e:
        print(f"⚠️ Ошибка при выполнении теста: {str(e)}")
        raise


def test_create_post():
    """Проверка создания нового поста"""
    print_test_header("Создание нового поста")
    try:
        data = {
            "title": "Test Post",
            "body": "This is a test post",
            "userId": 1
        }
        response = requests.post(f"{BASE_URL}/posts", json=data)
        status_ok = response.status_code == 201
        id_exists = response.json()["id"] is not None

        print_test_result(status_ok and id_exists, response)
        assert status_ok
        assert id_exists
    except Exception as e:
        print(f"⚠️ Ошибка при выполнении теста: {str(e)}")
        raise


def test_update_post():
    """Проверка обновления существующего поста"""
    print_test_header("Обновление поста")
    try:
        post_id = 1  # ID существующего поста
        updated_data = {
            "title": "Updated Title",
            "body": "Updated body content",
            "userId": 1
        }
        response = requests.put(f"{BASE_URL}/posts/{post_id}", json=updated_data)

        status_ok = response.status_code == 200
        updated_title_ok = response.json()["title"] == updated_data["title"]
        updated_body_ok = response.json()["body"] == updated_data["body"]

        print_test_result(status_ok and updated_title_ok and updated_body_ok, response)
        assert status_ok
        assert updated_title_ok
        assert updated_body_ok
    except Exception as e:
        print(f"⚠️ Ошибка при обновлении поста: {str(e)}")
        raise


if __name__ == "__main__":
    print("Запуск тестов API")
    print(f"Базовый URL: {BASE_URL}\n")

    # Запускаем тесты вручную для демонстрации отчета
    test_get_user()
    test_create_post()
    test_update_post()

    print("\nТестирование завершено")