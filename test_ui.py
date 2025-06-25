# test_ui.py
import logging
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


# Настройка логгера ДО всех остальных операций
def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Файловый обработчик
    file_handler = logging.FileHandler(
        filename="ui_test_report.log",
        mode="w",  # Перезаписывать файл каждый раз
        encoding="utf-8"
    )
    file_handler.setFormatter(
        logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    )

    # Консольный обработчик
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(
        logging.Formatter('%(levelname)s - %(message)s')
    )

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


setup_logging()  # Инициализация при импорте модуля


@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-insecure-localhost')
    options.add_argument('--disable-web-security')
    options.add_argument('--disable-extensions')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Отключает DevTools логгирование

    service = webdriver.ChromeService()
    service.creationflags = 0x08000000  # Отключает наследование handles

    driver = webdriver.Chrome(options=options, service=service)
    yield driver
    driver.quit()


def test_login(browser):
    """Тест авторизации"""
    logging.info("Начало теста авторизации")
    try:
        browser.get("https://demoqa.com/login")
        logging.info("Открыта страница авторизации")

        # Тестовые данные
        browser.find_element(By.ID, "userName").send_keys("test_user")
        browser.find_element(By.ID, "password").send_keys("P@ssw0rd!")
        browser.find_element(By.ID, "login").click()

        assert "Profile" in browser.page_source
        logging.info("Тест пройден успешно")
    except Exception as e:
        logging.error(f"Ошибка в тесте: {str(e)}", exc_info=True)
        raise