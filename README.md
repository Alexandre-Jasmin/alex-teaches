# alex-teaches

1. Web -> Add a new web app
    a. Manual Configuration
    b. Latest Python version

2. Console -> Bash
    a. mkvirtualenv myvirtualenv --python/usr/bin/python3.10
    b. git clone my-app.git
    c. cd my-app
    d. pip install -r requirements.txt

3. Web -> Source code
    a. copy /home/username/my-app
    b. WSGI file
        import sys
        path = '/home/username/my-app'
        if path not in sys.path:
            sys.path.append(path)
        from flask_app import app as application

4. Files
    a. copy /home/username/.virtualenvs/myvirtuenv
    b, Web -> Env -> paste

Reload and enjoy

# updating process
1. cd my-app
2. git pull origin main

# Structure

alex-teaches/
│
├── app/
│   ├── __init__.py          # App factory + OOP FlaskApp class
│   ├── routes/              # API routes (Blueprints)
│   │   ├── __init__.py
│   │   └── main.py
│   ├── services/            # Business logic
│   │   └── example_service.py
│   ├── models/              # Database models
│   │   └── __init__.py
│   ├── extensions.py        # Extensions (db, login_manager, etc.)
│   └── utils/               # Helpers/utilities
│       └── __init__.py
│
├── config/                  # Different configs (Dev, Test, Prod)
│   ├── __init__.py
│   ├── default.py
│   ├── development.py
│   ├── production.py
│   └── testing.py
│
├── tests/                   # Unit tests
│   └── test_main.py
│
├── .env                     # Environment variables
├── requirements.txt         # Dependencies
├── run.py                   # Entry point
