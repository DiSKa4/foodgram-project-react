![example workflow](https://github.com/DiSKa4/foodgram-project-react/actions/workflows/main.yml/badge.svg)

# Дипломная работа Foodgram

## Описание
Проект Foodgram - сервис для публикации кулинарных рецептов.
На этом сервисе пользователи могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

84.201.162.42


## Админка:

    login: xoz9in
    password: qwerty12345

## Возможности сервиса:

   Регистрация пользователей.
   
   Создание, Изменение, Удаление рецептов.
   
   Добавление рецептов в избранное и простмотр всех избранных рецептов.
    
   Фильтрация рецептов по тегам.
   
   Подписка на авторов и просмотр рецептов определенного автора.
   
   Добавление рецептов и формирование списка покупок для их приготовления.

## Шаблон наполнения env-файла:

    DB_NAME='postgres' # имя базы данных


    POSTGRES_USER='postgres' # логин для подключения к базе данных


    POSTGRES_PASSWORD='postgres' # пароль для подключения к БД


    DB_HOST='db' # название сервиса (контейнера)


    DB_PORT='5432' # порт для подключения к БД


## Запуск проекта:

### Запустите доккер:

    sudo docker-compose up


### Соберите статические файлы:

    sudo docker-compose exec backend python manage.py collectstatic --noinput

### Примените миграции:

    sudo docker-compose exec backend python manage.py migrate --noinput

### Создать суперпользователя Django:

    sudo docker-compose exec backend python manage.py createsuperuser



## Автор проекта:
Андрей Алексеевич
