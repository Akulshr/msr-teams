# Application controller used to parse json data retrieved from the MSR "Image promoted from repository" webhook event

from flask import Flask, Blueprint, request, abort
import json
import requests
import config

# Define the flask blueprint object
promote = Blueprint('promote', __name__)

# Define the flask route in the msrwebhook applicaiton and allow the POST HTTP method
@promote.route('', methods=['POST'])
def index():
    if request.method == 'POST':
        # capture the json data sent by the MSR webhook and dumps the values for each key as a string
        dtr_data = request.json
        event_type = json.dumps(dtr_data["type"])
        event_createdAt = json.dumps(dtr_data["createdAt"])
        contents_promotionPolicyID = json.dumps(dtr_data["contents"]["promotionPolicyID"])
        contents_digest = json.dumps(dtr_data["contents"]["digest"])
        contents_sourceRepository = json.dumps(dtr_data["contents"]["sourceRepository"])
        contents_sourceTag = json.dumps(dtr_data["contents"]["sourceTag"])
        contents_targetRepository = json.dumps(dtr_data["contents"]["targetRepository"])
        contents_targetTag = json.dumps(dtr_data["contents"]["targetTag"])
        contents_promotedAt = json.dumps(dtr_data["contents"]["promotedAt"])
        event_location = json.dumps(dtr_data["location"])

        # format the text message that will be sent to the Teams channel
        teams_data = {"@context": "https://schema.org/extensions", "@type": "MessageCard", "title": "Image Promoted", "text": "Promoted image " + contents_sourceRepository + ":" + contents_sourceTag + " to " + contents_targetRepository + " with tag " + contents_targetTag + " at " + contents_promotedAt.strip('"')}
        teams_url=config.refresh()
        response = requests.post(teams_url, data=json.dumps(teams_data),headers={'Content-Type': 'application/json'})
        return '', 200
    else:
        abort(400)
