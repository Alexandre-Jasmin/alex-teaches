from flask import Blueprint, jsonify, render_template
from app.services.example_service import ExampleService

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def home():
    service = ExampleService()   # ← create an instance
    return jsonify({"message": service.get_welcome_message()})

@main_bp.route("/status")
def status():
    return render_template(
        "status.html"
    )