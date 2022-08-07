# Исходный код для курсовой работы №4

### 1) Описание проекта
- Установка зависимостей
```shell
pip install -r requirements.txt

pip install -r requirements.dev.txt
```

### 2) Запуск проекта

### Bash (Linux/MACOS)
```shell
export FLASK_APP=run.py
export FLASK_ENV='development'
flask run --port=25000 
```

### CMD (Windows)
```shell
set FLASK_APP=run.py
set FLASK_ENV=development
flask run
```

### PowerShell (Windows)
```shell
$env:FLASK_APP = "run"
$env:FLASK_ENV = "development"
flask run --port=25000 
```

### ПОСЛЕ ЗАПУСКА ПРОЕКТА ЗАПУСТИТЬ ПУНКТ 3.
### 3) - Создание моделей (очистит БД и создаст все модели, указанные в импорте)
```shell
python create_tables.py
```

- Загрузка данных в базу
```shell
python load_fixture.py
```
Скрпит читает файл fixtures.json и загружает данные в базу. Если данные уже загружены - выводит соответсвующее сообщение.

## Запуск тестов
```shell
pytest
```

