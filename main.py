# dig into user_input global variable


import json
import requests
import sys

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


# base URL for dnd5e API
BASE_URL = "https://www.dnd5eapi.co"
# USER_INPUT = input("What spell would you like to look up: ")


# This is the 'homepage' route template we created previously.
@app.route('/')
def hello(name=None):
    return render_template('base.html', name='Alison')

# Here we are creating a route to handle the form request and return the `results` template
# Note that we have to explicitly allow POST requests, since they aren't handled
# by the `@app.route()` function by default


@app.route('/results', methods=['POST'])
def returnResults():
    if request.method == 'POST':
        USER_INPUT = request.form["requestedSpell"]
        final_spell = retrieve_user_spell(get_all_spells())
        return render_template("results.html", result=final_spell)


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
    # TODO: look into lambda function for this case
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


# def print_spell_description(spell):
#     if spell:
#         print()
#         print(spell["desc"][0])
#         print()
#         print("It is a level", spell["level"], "spell")
#         print()
#         print("Spell cast time: ", spell["casting_time"])
#         print()
#         print("Spell range: ", spell["range"])
#         print()
#         print("Spell duration: ", spell["duration"])


# final_spell = retrieve_user_spell(get_all_spells())
# print_spell_description(final_spell)
