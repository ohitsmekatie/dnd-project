# dnd-project

Lil side project playing around with the DnD 5e API 

http://www.dnd5eapi.co/docs/


To run locally:
 - Install virtualenv, if you haven't already `sudo python3 -m pip install virtualenv`
 - Create the virtual environment (Should only need to be run once, the first time you run the project locally) `python3 -m venv venv`
 - Activate the virtual env from within the project directory `~/projects/dnd-project/ venv/bin/activate`
 - Install flask in the virtual env `pip install Flask`
 - Install requests module `pip install requests`
 - Run flask! `FLASK_APP=main.py FLASK_ENV=development flask run` Note: the `development` flag enables file watching and automatic reloading on file changes wheeeee!
