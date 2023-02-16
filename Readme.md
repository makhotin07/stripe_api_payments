# Проект с оплатой 

### Django + Postgres + Docker + Stripe

## Клонировать проект

    $ cd project_stripe_docker

    $ cd infra

Вам нужно самостоятельно в папке infra создать файл .env
по примеру EXAMPLE.env, при необходимости сгенерировать новый SECRET_KEY django,
указать Stripe Public и Secret ключи из личного аккаута: https://dashboard.stripe.com/test/dashboard





    $ docker-compose up


* Миграции происходят автоматически 
* Товары добавляются автоматически 
* SuperUser создается автоматически
* Карта для тест оплаты 

    
    $ 4242 4242 4242 4242 
    10/32 
    789

<br>
сайт доступен по ссылке http://127.0.0.1:8000/

Чтобы просмотреть Админ Панель логин:пароль
<br>

        admin:admin

