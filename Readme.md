# Тестовое задание Django + Stripe API 

<p align="center">
    <img src="https://img.shields.io/badge/Python-3.9-blue" alt="Python Version"/>
    <img src="https://img.shields.io/badge/Django-3.2.8-brightgreen" alt="Django Version"/>
    <img src="https://img.shields.io/badge/Django%20Rest%20Framework-3.12.4-green" alt="Django Rest Framework Version"/>
    <img src="https://img.shields.io/badge/Docker-20.10.8-blue" alt="Docker Version"/>
    <img src="https://img.shields.io/badge/Docker--Compose-1.29.2-blue" alt="Docker-Compose Version"/>
    <img src="https://img.shields.io/badge/Stripe-API-orange" alt="Stripe API"/>
</p>




## Описание

Приветствую! В данном репозитории представлено тестовое задание "Django + Stripe API", в котором реализован пример использования Django в связке с Stripe API для обработки платежей.

## Используемые технологии

- Python 3.9
- Django 3.2.8
- Django Rest Framework 3.12.4
- Docker 20.10.8
- Docker Compose 1.29.2
- Stripe API

## Подготовка

Для успешного запуска проекта, выполните следующие шаги:

1. **Регистрация на сайте Stripe:** Перейдите на [https://stripe.com](https://stripe.com) и зарегистрируйтесь. Получите Publishable key и Secret key.

2. **Клонирование репозитория:** Склонируйте данный репозиторий с помощью команды:
   ```
   git clone <название репозитория>
   ```

3. **Создание файла .env:** В корневой папке проекта (`TaskStrip`) создайте файл `.env` и добавьте следующие переменные:
   ```
   SECRET_KEY=<любой набор символов>
   STRIPE_PUBLIC_KEY=<Ваш Publishable key с сайта stripe.com>
   STRIPE_SECRET_KEY=<Ваш Secret key с сайта stripe.com>
   ```

## Запуск проекта с использованием Docker

1. **Запуск контейнеров Docker:** В корневой папке проекта выполните следующую команду:
   ```bash
   docker-compose up
   ```

2. **Создание миграций и загрузка тестовых данных:** В новом терминале, в корневой папке проекта, выполните следующие команды:
   ```bash
   docker-compose exec web python manage.py makemigrations
   docker-compose exec web python manage.py migrate
   docker-compose exec web python manage.py loaddata items.json
   ```

## Запуск проекта без использования Docker



1. **Активация виртуального окружения:** В корневой папке проекта выполните следующую команду:
   - **Для Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **Для macOS и Linux:**
     ```bash
     source venv/bin/activate
     ```

2. **Установка зависимостей:** В корневой папке проекта выполните следующую команду:
   ```bash
   pip install -r requirements.txt
   ```

3. **Создание миграций и загрузка тестовых данных:** В корневой папке проекта выполните следующие команды:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py loaddata items.json
   ```

4. **Запуск сервера Django:** В корневой папке проекта выполните следующую команду:
   ```bash
   python manage.py runserver
   ```

## Доступ к административной панели

- Если вы загрузили тестовые данные, перейдите по адресу [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) и используйте логин `admin` и пароль `admin`.
- Если вы не загрузили тестовые данные, создайте суперпользователя Django с помощью следующей команды:
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

## Примеры некоторых запросов API

- Получение Stripe Session Id:
  ```
  GET /buy/1/
  ```

- Получение данных о предмете:
  ```
  GET /item/3/
  ```

**Примечание:** Для тестирования платежей используйте следующие номера карт:
- 4242 4242 4242 4242
- 4000 0000 0000 3220
- 4000 0000 0000 9995

#### Автор

Никита Махотин - [https://github.com/makhotin07](https://github.com/makhotin07)

---

🌟 Приятного использования проекта! Если у вас возникнут вопросы, не стесняйтесь обращаться ко мне.
