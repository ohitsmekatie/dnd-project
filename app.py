from flask import Flask, render_template, jsonify
import requests
import random

app = Flask(__name__) 

BASE_URL = "https://www.dnd5eapi.co"  # Root URL, not /api

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/random-item")
def random_item():
    try:
        # Valid top-level categories for random selection
        categories = ["equipment", "magic-items"]
        category = random.choice(categories)

        # Get list of items in the category
        response = requests.get(f"{BASE_URL}/api/{category}")
        response.raise_for_status()
        data = response.json()

        # Pick a random item from the results
        item = random.choice(data["results"])

        # Get full details using the item's URL
        detail_url = f"{BASE_URL}{item['url']}"
        item_details_response = requests.get(detail_url)
        item_details_response.raise_for_status()
        item_details = item_details_response.json()

        return jsonify(item_details)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
