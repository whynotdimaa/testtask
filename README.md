
# 🚀 Django REST API Project

Це бекенд-додаток на базі **Django REST Framework**, повністю готовий до розробки та розгортання за допомогою **Docker**.

## 🛠 Технологічний стек
* **Framework:** Django 5.x & Django REST Framework
* **Database:** PostgreSQL (або SQLite залежно від налаштувань)
* **Documentation:** Swagger (drf-spectacular)
* **Containerization:** Docker & Docker Compose

---

## 📖 Документація API (Swagger)

Після запуску проєкту документація генерується автоматично. Ви можете протестувати всі ендпоінти прямо в браузері:

* **Swagger UI**: [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/) — інтерактивний інтерфейс для тестування запитів.
* **ReDoc**: [http://localhost:8000/api/redoc/](http://localhost:8000/api/redoc/) — чиста документація для читання.
* **Schema**: [http://localhost:8000/api/schema/](http://localhost:8000/api/schema/) — OpenAPI файл у форматі YAML.

---
📮 Тестування через Postman
У корені проєкту знаходиться папка /postman (або відповідний JSON-файл), яка містить готову колекцію запитів для швидкого старту:

Імпорт: Відкрийте Postman та імпортуйте файл колекції.

Середовище: Налаштуйте base_url як http://localhost:8000/api/.

Запити: Колекція містить приклади для авторизації, отримання списків та створення нових записів.
## 🐳 Запуск через Docker (Рекомендовано)

Найшвидший спосіб підняти проєкт у контейнерах.

### 1. Збірка та запуск
Виконайте команду в корені проєкту:
```bash
docker-compose up --build
```

### 2. Робота з базою даних (Міграції)
Використовуйте ці команди для налаштування структури БД:
```bash
# Створення нових файлів міграцій (якщо змінили models.py)
docker-compose exec web python manage.py makemigrations

# Застосування міграцій до бази даних
docker-compose exec web python manage.py migrate
```

### 3. Створення адміністратора
Щоб отримати доступ до адмін-панелі (`/admin`), створіть суперкористувача:
```bash
docker-compose exec web python manage.py createsuperuser
```

---

## 💻 Локальний запуск (без Docker)

1.  **Активуйте віртуальне середовище та встановіть залежності:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Запустіть сервер:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```

---

## 📝 Корисні команди Docker Compose

* **Зупинка проєкту:** `docker-compose down`
* **Перегляд логів у реальному часі:** `docker-compose logs -f`
* **Перезапуск контейнерів:** `docker-compose restart`
