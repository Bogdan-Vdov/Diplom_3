# Diplom_3

## Автотесты для UI Stellar Burgers

Этот проект содержит только настоящие автоматизированные UI-тесты для веб-приложения Stellar Burgers. Используется паттерн Page Object.

### Требования

- Python 3.7+
- Google Chrome
- Mozilla Firefox

### Установка зависимостей

```bash
pip install -r requirements.txt
```

### Запуск тестов

Для проверки основной функциональности:

```bash
pytest tests/test_main_functionality.py
```

Для проверки функциональности ленты заказов:

```bash
pytest tests/test_order_feed.py
```

Для проверки авторизации:

```bash
pytest tests/test_auth.py
```

Для проверки функциональности заказов:

```bash
pytest tests/test_orders.py
```

Для запуска всех тестов в браузерах (требует установленных браузеров):

```bash
pytest
```

Если браузеры не установлены, можно запустить:

```bash
pytest tests/test_example.py
```

Также можно использовать скрипт для запуска тестов:

```bash
python run_tests.py
```

### Генерация Allure-отчета

После тестов можно сгенерировать Allure-отчет:

```bash
allure serve allure-results
```

### Структура проекта

- `pages/` - Page Object'ы
  - `components/` - Компоненты
- `tests/` - Тесты
  - `test_main_functionality.py` - Основная функциональность
  - `test_order_feed.py` - Лента заказов
  - `test_auth.py` - Авторизация
  - `test_orders.py` - Заказы
- `requirements.txt` - Зависимости
- `pytest.ini` - Конфигурация
- `run_tests.py` - Скрипт для запуска тестов

### Возможные проблемы

Если тесты не запускаются:
1. Установите браузеры Google Chrome и Mozilla Firefox
2. Проверьте права на запуск браузеров
3. Проверьте антивирус/брандмауэр