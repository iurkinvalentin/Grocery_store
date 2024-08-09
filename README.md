# Django Grocery Store Application

## Описание

Этот проект представляет собой приложение для продуктового магазина, разработанное на Django. Оно позволяет управлять категориями и подкатегориями товаров, добавлять и редактировать продукты, а также работать с корзиной пользователя, включая добавление и удаление товаров.

## Основные функции

- **Управление категориями и подкатегориями**: Административный интерфейс для создания, редактирования и удаления категорий и подкатегорий товаров.
- **Управление продуктами**: Административный интерфейс для создания, редактирования и удаления продуктов с поддержкой изображений в разных размерах.
- **Корзина пользователя**: Функционал для добавления товаров в корзину, изменения их количества и удаления.
- **API для работы с корзиной и продуктами**: Эндпоинты для взаимодействия с корзиной и получения списка продуктов с пагинацией.

## Установка

1. **Клонируйте репозиторий:**

   ```bash
   git clone https://github.com/iurkinvalentin/grocery_store.git
   cd grocery_store

Создайте виртуальное окружение и активируйте его:
python -m venv venv
source venv/bin/activate  # для Windows: venv\Scripts\activate
Установите зависимости:
pip install -r requirements.txt
Примените миграции:
python manage.py migrate
Создайте суперпользователя для доступа к админке:
python manage.py createsuperuser
Запустите сервер:
python manage.py runserver
Перейдите в админку и создайте категории, подкатегории и продукты:
Админка доступна по адресу: http://127.0.0.1:8000/admin/

Django
Django REST Framework
SQLite (по умолчанию)

# Примеры запросов для API

## Список категорий с подкатегориями

**Запрос:**

GET /api/categories/ HTTP/1.1  
Host: 127.0.0.1:8000

**Ответ:**

{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "name": "Фрукты",
            "slug": "fruits",
            "image": "/media/fruits.jpg",
            "subcategories": [
                {
                    "name": "Цитрусовые",
                    "slug": "citrus",
                    "image": "/media/citrus.jpg",
                    "parent_category": 1
                }
            ]
        },
        {
            "name": "Овощи",
            "slug": "vegetables",
            "image": "/media/vegetables.jpg",
            "subcategories": []
        }
    ]
}

## Список продуктов

**Запрос:**

GET /api/products/ HTTP/1.1  
Host: 127.0.0.1:8000

**Ответ:**

{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "name": "Апельсины",
            "slug": "apelsiny",
            "price": "50.00",
            "category": "Фрукты",
            "subcategory": "Цитрусовые",
            "images": {
                "small": "/media/small/apelsiny.jpg",
                "medium": "/media/medium/apelsiny.jpg",
                "large": "/media/large/apelsiny.jpg"
            }
        }
    ]
}

## Корзина пользователя

**Запрос на получение содержимого корзины:**

GET /api/basket/ HTTP/1.1  
Host: 127.0.0.1:8000

**Ответ для непустой корзины:**

{
    "items": [
        "Апельсины",
        "Яблоки"
    ],
    "total_quantity": 5,
    "total_price": 250.00
}

**Ответ для пустой корзины:**

{
    "message": "Корзина пуста"
}

**Запрос на очистку корзины:**

DELETE /api/basket/ HTTP/1.1  
Host: 127.0.0.1:8000

**Ответ:**

{
    "status": "Корзина пуста"
}

## Элементы корзины

**Запрос на добавление продукта в корзину:**

POST /api/basket/item/ HTTP/1.1  
Host: 127.0.0.1:8000  
Content-Type: application/json

{
    "product_id": 1,
    "quantity": 3
}

**Ответ:**

{
    "id": 1,
    "product": {
        "name": "Апельсины",
        "slug": "apelsiny",
        "price": "50.00",
        "category": "Фрукты",
        "subcategory": "Цитрусовые",
        "images": {
            "small": "/media/small/apelsiny.jpg",
            "medium": "/media/medium/apelsiny.jpg",
            "large": "/media/large/apelsiny.jpg"
        }
    },
    "quantity": 3
}

**Запрос на изменение количества продукта в корзине:**

PATCH /api/basket/item/ HTTP/1.1  
Host: 127.0.0.1:8000  
Content-Type: application/json

{
    "product_id": 1,
    "quantity": 5
}

**Ответ:**

{
    "id": 1,
    "product": {
        "name": "Апельсины",
        "slug": "apelsiny",
        "price": "50.00",
        "category": "Фрукты",
        "subcategory": "Цитрусовые",
        "images": {
            "small": "/media/small/apelsiny.jpg",
            "medium": "/media/medium/apelsiny.jpg",
            "large": "/media/large/apelsiny.jpg"
        }
    },
    "quantity": 5
}

**Запрос на удаление продукта из корзины:**

DELETE /api/basket/item/ HTTP/1.1  
Host: 127.0.0.1:8000  
Content-Type: application/json

{
    "product_id": 1
}

**Ответ:**

{
    "message": "Продукт удален из корзины"
}
