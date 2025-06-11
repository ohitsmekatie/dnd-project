# Retrieve data from the DnD API

A simple web application that generates random D&D 5e equipment and magical items using the [D&D 5e API](https://www.dnd5eapi.co/docs/).

## Features

- Single-page Flask application
- Random generation of equipment and magical items from the official D&D 5e API
- Random generation of monster from the official D&D 5e API
- Random first + last name, using the scraped data from the scripts in [this repository](https://github.com/ohitsmekatie/get-data-for-loremore). This is a repository of one-off scripts I wrote in Python to help me more programattically generated the database of content
- JSON display of complete item details


### Next:
- Style the payload
- Style the app
- Access more endpoints, expand the navigation and app

## Prerequisites

- Python 3.x
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/dnd-project.git
cd dnd-project
```

2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the Flask development server:
```bash
python app.py
```

Then open your browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## How It Works

- The application uses Flask to serve a simple web interface
- When the "Give me an n" button is clicked, a random item is fetched from the D&D 5e API or from other data sources explained above


## Dependencies

- [Flask](https://flask.palletsprojects.com/) - Web framework
- [Requests](https://docs.python-requests.org/) - HTTP library for API calls

## API Reference

This project uses the [D&D 5e API](https://www.dnd5eapi.co/docs/) which provides data from the SRD (Systems Reference Document) for Dungeons & Dragons 5th Edition.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.