# alex-teaches
 Alex Teaches

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