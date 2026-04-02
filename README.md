# ⚔ Shinori — Slay Your Tasks, One by One

A Jujutsu Kaisen-themed Django todo app.

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run migrations
```bash
python manage.py migrate
```

### 3. (Optional) Create a superuser for the admin panel
```bash
python manage.py createsuperuser
```

### 4. Run the dev server
```bash
python manage.py runserver
```

Then open **http://127.0.0.1:8000** in your browser.

---

## Pages & Features

| URL | Page |
|---|---|
| `/` | Dashboard — stats + quick add |
| `/tasks/` | My Tasks — full list with filters & search |
| `/priorities/` | Priorities — grouped by High / Medium / Low |
| `/register/` | Register a new warrior |
| `/login/` | Login |
| `/admin/` | Django admin panel |

## How it works

- **Register** with your name + email (email is used as username; password is auto-set to `email_shinori` — change this in `views.py` for production)
- **Add tasks** via the modal (press `N` anywhere as a shortcut)
- **Slay** a task by clicking its circle — it moves to the Slayed section with strikethrough
- **Delete** tasks with the ✕ button
- **Priority dots**: 🔴 High, 🟣 Medium, 🟢 Low
- **Search** tasks from the My Tasks page
- **Expand** a task item to see its description and due date

## Production notes
- Change `SECRET_KEY` in `settings.py`
- Set `DEBUG = False`
- Configure a proper database (PostgreSQL recommended)
- Use a real password hashing flow for registration
