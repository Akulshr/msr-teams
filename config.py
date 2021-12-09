# Configuration module used to create and modify the TinyDB instance used track the teams Application URL

#from flask import Flask, render_template, request
#import datetime
from tinydb import TinyDB, Query, where
import json

# Set the default URL that will be displayed in the msrwebhook main endpoint. This will be replaced by the user when configuring the teams Applicaiton URL
tmpurl = '<Enter Microsoft Teams Incoming Webhook URL>'

# Define the location of the db.json file used by TinyDB. Recommendation is to create a persistent volume and mount it to "/database"
db = TinyDB('/tmp/db.json')
searchdata = Query()

# Initialize the database with tmpurl if it does not already exist
if len(db) == 0:
  db.insert({'id':1, 'teamsurl':tmpurl})

# Primary function used to pull the value of the teams Applicaiton URL from the database and return it as "teams_url"
def refresh():
    teamsdbdata = db.search(searchdata.id == 1)
    teams_url = json.dumps(teamsdbdata[0]["teamsurl"]).strip('"')
    return teams_url
