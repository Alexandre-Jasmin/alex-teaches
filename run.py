from app import create_app

# create_app function is assumed to be defined in app/__init__.py
# initializes the Flask application with the specified configuration
app = create_app("development")

if __name__ == "__main__":
    app.run()
