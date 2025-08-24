# Alex Teaches

## Deploying a Web App

### 1. Web
- Add a new web app
  - Manual Configuration
  - Select the latest Python version

### 2. Console (Bash)
```bash
mkvirtualenv myvirtualenv --python=/usr/bin/python3.10
git clone my-app.git
cd my-app
pip install -r requirements.txt
import sys
path = '/home/username/my-app'
if path not in sys.path:
    sys.path.append(path)
from flask_app import app as application

cd my-app
git pull origin main
