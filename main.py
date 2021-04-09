import json
import requests
import sys

from flask import Flask
# error: AttributeError: 'Flask' object has no attribute 'render_template'
from flask import render_template

app = Flask(__name__)


# base URL for dnd5e API
BASE_URL = "https://www.dnd5eapi.co"
USER_INPUT = input("What spell would you like to look up: ")


@app.route('/')
def make_api_request(url):
    '''a function that, given a url, makes an API request and returns payload'''
    response = requests.get(url)
    payload = json.loads(response.text)
    # print(response.status_code)
    return payload


def get_all_spells():
    # the output of this is all the spells that we have available
    return make_api_request(BASE_URL + "/api/spells")


def retrieve_user_spell(all_spells):
    matching_spell = list(filter(get_spell_info, all_spells["results"]))
    if len(matching_spell) == 0:
        print("Sorry, we couldn't find that spell.")
    else:
        spell_url = matching_spell[0]["url"]
        return make_api_request(BASE_URL + spell_url)


def get_spell_info(singular_spell_dict):
    if USER_INPUT.lower() in singular_spell_dict["name"].lower():
        return True
    else:
        return False


def print_spell_description(spell):
    if spell:
        print()
        print(spell["desc"][0])
        print()
        print("It is a level", spell["level"], "spell")
        print()
        print("Spell cast time: ", spell["casting_time"])
        print()
        print("Spell range: ", spell["range"])
        print()
        print("Spell duration: ", spell["duration"])


def main():

    final_spell = retrieve_user_spell(get_all_spells())

    print_spell_description(final_spell)

    return app.render_template("base.html")


main()
