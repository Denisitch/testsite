# Тестовый сайт
Это мой тестовый новостной сайт

### Настройка проекта

Создайте `.env` файл в корне репозитория:

```bash
cp .env.conf .env
```

Внесите при необходимости корректировки в переменные окружения.

### Сборка образов и запуск контейнеров

В корне репозитория выполните команду:

```bash
docker-compose up --build
```

### Остановка контейнеров

Для остановки контейнеров выполните команду:

```bash
docker-compose stop
```

### Инициализация проекта

Команды выполняются внутри контейнера приложения:

```bash
docker-compose exec app bash
```
#### Применение миграций:

```bash
python manage.py migrate
```
#### Добавление фикстур:

```bash
python manage.py loaddata _initial_data.json

```

#### Сборка статики:

```bash
python manage.py collectstatic
```

#### Создание суперпользователя

```bash
python manage.py createsuperuser
```

Проект доступен по адресу http://0.0.0.0:8000