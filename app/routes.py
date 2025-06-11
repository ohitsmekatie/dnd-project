from flask import Blueprint, render_template, jsonify
import requests
import random

main = Blueprint('main', __name__)

BASE_URL = "https://www.dnd5eapi.co"

@main.route("/")
def index():
    return render_template("base.html")

# Create function to handle the reusable pieces of fetching data from the API
def fetch_random_resource(resource_type):
    """
    Fetch a random resource from the DnD 5E API. This will be used in other functions that will provide the
    specific resource(like monsters or items).

    """
    try:
        # Handle multiple resource types (like equipment/magic-items)
        if isinstance(resource_type, list):
            resource_type = random.choice(resource_type)

        # Get the list of all resources of a type
        response = requests.get(f"{BASE_URL}/api/{resource_type}")
        response.raise_for_status()
        data = response.json()

        # Select a random item from the results
        resource = random.choice(data["results"])

        # Get the details of that specific resource
        details_response = requests.get(f"{BASE_URL}{resource['url']}")
        details_response.raise_for_status()
        return details_response.json()

    # Error handling
    except Exception as e:
        raise Exception(f"Error fetching {resource_type}: {str(e)}")

@main.route("/random-item")
def random_item():
    try:
        item_details = fetch_random_resource(["equipment", "magic-items"])
        return jsonify(item_details)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@main.route("/random-monster")
def random_monster():
    try:
        monster_details = fetch_random_resource("monsters")
        return jsonify(monster_details)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
