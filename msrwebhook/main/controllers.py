# Application controller used to configure the teams Application URL for the MSR Webhook integration with teams

from flask import Flask, Blueprint, render_template, request
#from tinydb import TinyDB, Query, where
from tinydb import where
import json
#import datetime
import config

# Define the flask blueprint object
main = Blueprint('main', __name__)

# Define the flask main route in the msrwebhook applicaiton and allow the GET and POST HTTP methods
@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # capture the user input provided in the flask template
        urlupdate=request.form['teams_url']
        # update the TinyDB instance with the user provided teams Application URL
        config.db.update({'teamsurl':urlupdate}, where('id') == 1)
        # use the refresh function in the config module to display the new teams Application URL
        teams_url=config.refresh()
        return render_template('index.html', teams_url=teams_url)
    if request.method == 'GET':
        # use the refresh function in the config module to display the new teams Application URL
        teams_url=config.refresh()
        return render_template('index.html', teams_url=teams_url)
