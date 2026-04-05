
# Тестовое задание на стажировку QA 

## Описание
Это набор автоматизированных тестов для API микросервиса объявлений Avito Internship.  
Тесты покрывают следующие ручки:
- Создание объявления
- Получение объявления по ID
- Получение всех объявлений по sellerID
- Получение статистики по itemID

### Требования

- Python==3.14.3
- pytest==7.4.3
- requests==2.31.0
- flake8==7.3.0
- faker==30.0.0

### Установка

1) Склонировать репозиторий

```bash
git clone https://github.com/flying-ghost/qa-test-avito.git
```

2) Установить зависимости:

```bash
pip install -r requirements.txt
```

### Запуск тестов

Запустить все тесты:

```bash
pytest -v tests/
```

### Запуск конкретного теста

```bash
pytest -v tests/get_statistic/test_get_statistics.py
```

### Для запуска линтера

```bash
flake8 --exclude=venv tests/
```

Реализовано для стажировки Avito Internship
Контакт Tg: @enflammer_anxiente