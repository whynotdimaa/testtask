# Travel Planner API

A RESTful API for managing travel projects and places built with Django REST Framework.

## Requirements

- Python 3.12+
- pip

## Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd travelpl
```

2. Create and activate virtual environment:
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install django djangorestframework requests
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the server:
```bash
python manage.py runserver
```

API is available at `http://127.0.0.1:8000/api/`

---

## Endpoints

### Projects

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/api/project/` | List all projects |
| POST | `/api/project/` | Create a project |
| GET | `/api/project/{id}/` | Get a single project |
| PATCH | `/api/project/{id}/` | Update a project |
| DELETE | `/api/project/{id}/` | Delete a project |

### Places

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/api/project/{id}/places/` | List places for a project |
| GET | `/api/project/{id}/places/{place_id}/` | Get a single place |
| POST | `/api/place/` | Add a place to a project |
| PATCH | `/api/place/{id}/` | Update a place |
| DELETE | `/api/place/{id}/` | Delete a place |

---

## Example Requests

### Create a project with places
```json
POST /api/project/
{
    "name": "Paris Trip",
    "description": "My dream trip to Paris",
    "start_date": "2026-06-01",
    "places": [
        {
            "external_id": 129452,
            "notes": "Must see this painting"
        }
    ]
}
```

### Add a place to existing project
```json
POST /api/place/
{
    "project": 1,
    "external_id": 129453,
    "notes": "Amazing sculpture"
}
```

### Mark place as visited
```json
PATCH /api/place/{id}/
{
    "is_visited": true
}
```

---

## Business Logic

- A project can have **minimum 1, maximum 10 places**
- A project **cannot be deleted** if any of its places are marked as visited
- A place **cannot be deleted** if it is marked as visited
- The same place **cannot be added** to the same project twice
- When **all places** in a project are visited, the project is automatically marked as completed
- Places are validated against the **Art Institute of Chicago API** before being stored

## Third-party API

This project uses the [Art Institute of Chicago API](https://api.artic.edu/docs/) to validate places.