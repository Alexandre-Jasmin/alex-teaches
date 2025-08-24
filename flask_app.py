# Copyright (c) 2024 Alexandre Jasmin All rights reserved.
from flask import Flask, request, render_template, redirect, url_for, session, flash
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.secret_key = os.urandom(24)

app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', 'True') == 'True'
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')

mail = Mail(app)

@app.route('/')
@app.route('/home')
@app.route('/accueil')
def index():
    # Accueil
    return render_template(
        "index.html",
    )

@app.errorhandler(Exception)
def handle_error(error):
    error_code = getattr(error, 'code', 500)
    return render_template('error.html', error_code=error_code), error_code

if __name__ == '__main__':
    app.run(debug=True, port=8000)
