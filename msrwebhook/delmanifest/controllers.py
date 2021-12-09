# Application controller used to parse json data retrieved from the MSR "Manifest deleted on repository	" webhook event

from flask import Flask, Blueprint, request, abort
import json
import requests
import config

# Define the flask blueprint object
delmanifest = Blueprint('delmanifest', __name__)

# Define the flask route in the msrwebhook applicaiton and allow the POST HTTP method
@delmanifest.route('', methods=['POST'])
def index():
    if request.method == 'POST':
        # capture the json data sent by the MSR webhook and dumps the values for each key as a string
        dtr_data = request.json
        event_type = json.dumps(dtr_data["type"])
        event_createdAt = json.dumps(dtr_data["createdAt"])
        contents_namespace = json.dumps(dtr_data["contents"]["namespace"])
        contents_repository = json.dumps(dtr_data["contents"]["repository"])
        contents_digest = json.dumps(dtr_data["contents"]["digest"])
        contents_imageName =  json.dumps(dtr_data["contents"]["imageName"])
        contents_os = json.dumps(dtr_data["contents"]["os"])
        contents_architecture = json.dumps(dtr_data["contents"]["architecture"])
        contents_author = json.dumps(dtr_data["contents"]["author"])
        contents_deletedAt = json.dumps(dtr_data["contents"]["deletedAt"])
        event_location = json.dumps(dtr_data["location"])

        # format the text message that will be sent to the Teams channel
        teams_data = {"@context": "https://schema.org/extensions", "@type": "MessageCard", "title": "Manifest Deleted", "text": "User " + contents_author.strip('"') + " deleted manifest " + contents_imageName + " at " + contents_deletedAt.strip('"')}
        teams_url=config.refresh()
        response = requests.post(teams_url, data=json.dumps(teams_data),headers={'Content-Type': 'application/json'})
        return '', 200
    else:
        abort(400)
