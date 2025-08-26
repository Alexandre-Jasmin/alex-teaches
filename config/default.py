import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    #SECRET_KEY = os.getenv("SECRET_KEY", "fallback-key")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER=os.getenv("MAIL_SERVER")
    MAIL_PORT=os.getenv("MAIL_PORT")
    MAIL_USE_TLS=os.getenv("MAIL_USE_TLS")
    MAIL_USERNAME=os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD")
