# Тестовый проект для стажировки QA Automation в МТС

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://python.org)
[![Pytest](https://img.shields.io/badge/Pytest-тестирование-green)](https://docs.pytest.org)
[![Selenium](https://img.shields.io/badge/Selenium-Web%20Testing-orange)](https://selenium.dev)

## 🚀 Технологический стек
- **Язык**: Python 3.11
- **Фреймворки**: Pytest, Selenium WebDriver
- **Дополнительно**: Page Object Model, API-тестирование (requests)
- **CI/CD**: GitHub Actions (пример в папке .github/workflows)

```markdown
## 📂 Структура проекта
.
├── .github/
│ └── workflows/ # Автоматизированные тесты CI/CD
├── tests/
│ ├── web/ # Веб-тесты (Selenium)
│ ├── api/ # API-тесты (requests)
│ └── auth/ # Тесты авторизации
├── utils/ # Вспомогательные утилиты
├── requirements.txt # Зависимости
└── README.md

## ⚙️ Установка и запуск
```bash
# 1. Клонирование репозитория
git clone https://github.com/Beerdling/qa-automation-mts.git

# 2. Установка зависимостей
pip install -r requirements.txt

# 3. Запуск тестов
pytest tests/ --alluredir=reports
