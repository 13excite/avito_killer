# Описание

## Запускаем венв
```
python -m venv env
```
## Ставим зависимости
```
pip install -r requirements.txt
```

## Запускаем инит(в проекте уже есть ./migrations)
```
python manage.py db init
```
## Запускаем миграцию
```
python manage.py db migrate
```
## Применяем обновления
```
python manage.py db upgrade
```
