from app import create_app

# Change "development" -> "production" in deployment
app = create_app("development")

if __name__ == "__main__":
    app.run()
