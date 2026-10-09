# Travel Exploration Web Application

A Django-based web application for managing and exploring travel destinations, places, and user reviews.

---

## 📋 Prerequisites

Before running this project, make sure you have the following installed on your system:

- **Python** (version 3.10 or higher recommended)
- **pip** (Python package installer)
- **git**

---

## 🚀 Quick Start Guide

Follow these simple step-by-step instructions to get the project running locally.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

*(Note: Navigate into the project directory containing `manage.py` if structured inside a subfolder: `cd backend/travel`)*

---

### 2. Create and Activate a Virtual Environment

It is recommended to use a virtual environment to manage project dependencies cleanly.

#### On Linux / macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### On Windows (Command Prompt):
```cmd
python -m venv venv
venv\Scripts\activate
```

#### On Windows (PowerShell):
```powershell
python -m venv venv
.\venv\Scripts\activate
```

---

### 3. Install Dependencies

Install Django and any required packages:

```bash
pip install django Pillow
```

> *(If a `requirements.txt` file is present, you can run: `pip install -r requirements.txt`)*

---

### 4. Apply Database Migrations

Set up your SQLite database tables by running:

```bash
python manage.py migrate
```

---

### 5. Create a Superuser (Optional)

To access the Django Admin Dashboard (`/admin`), create an administrator account:

```bash
python manage.py createsuperuser
```

Follow the interactive prompts to enter a username, email, and password.

---

### 6. Run the Development Server

Start the local server:

```bash
python manage.py runserver
```

Open your browser and visit:
- **Application:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Admin Panel:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 📁 Project Structure

```text
travel/
├── manage.py             # Django project management CLI tool
├── db.sqlite3            # SQLite database
├── media/                # User uploaded media (images, avatars, etc.)
├── static/               # Static assets (CSS, JS, images)
├── place/                # Core application app (models, views, templates)
└── travel/               # Project configuration (settings, root URLs)
```

---

## 🛠️ Common Commands Quick Reference

| Action | Command |
| :--- | :--- |
| **Activate virtualenv** | `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows) |
| **Run migrations** | `python manage.py migrate` |
| **Create admin user** | `python manage.py createsuperuser` |
| **Start server** | `python manage.py runserver` |
