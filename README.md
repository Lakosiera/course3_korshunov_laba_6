# Лаба 6. Разработка RESTful API

## Задание

-[ ] Создайте RESTful API с использованием Django Rest Framework, которое предоставляет доступ к данным вашего приложения. 
-[ ] API должно поддерживать операции CRUD (создание, чтение, обновление, удаление).

### Требования:

- [x] БД должна содержать не менее 3 связанных таблиц.
- [ ] В API должна быть реализована обязательная аутентификация. 
- [ ] Документация по использованию API должна быть оформлена с помощью Swagger. 


### Варианты

> *7.* API для кредитного банка (кредиты, вклады).

## Первичная Настрока базы данных для Django

> Выполнять **после** запуска Docker контейнера 

[Инструкция по миграции](server/МОГРАЦИЯ.md)

## Docker

### Сборка Docker образа из Dockerfile

```sh
docker compose build
```

### Запуск Docker композа

```sh
# будет выводит информацию в консоль
docker compose up
```

или

```sh
# запустит контенер без консоли
docker compose up -d
```

### Остановка Docker композа

```sh
# остановит контенер
docker compose down
```

### Зайти в оболочку контейнера

```sh
# зайти в комендную обалочку контенера
docker exec -it container_name sh
# docker exec -it laba-6-django sh
```

или

```sh
# зайти в комендную обалочку контенера через композ
docker compose exec service_name sh
# docker compose exec laba-6-django sh
```

## Настрока Django без Docker

### Настрока Питона

Сохраняем список всех установлинных в питон пакетов

```sh
pip freeze > requirements.txt
```

Устанавливаем в питон список пакетов

```sh
pip install -r requirements.txt
```

### Как создать новый серер

```sh
django-admin startproject server 
```

### Как создать модуль

```sh
python manage.py startapp module_name
```

### Кака запустить джанго

```sh
cd server

python manage.py runserver
```

### Джанго проверка

[http://127.0.0.1:8005/](http://127.0.0.1:8005/)

