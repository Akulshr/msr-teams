# Application controller used to parse json data retrieved from the MSR "Security scan completed" webhook event

from flask import Flask, Blueprint, request, abort
import json
import requests
import config

# Define the flask blueprint object
scan = Blueprint('scan', __name__)

# Define the flask route in the msrwebhook applicaiton and allow the POST HTTP method
@scan.route('', methods=['POST'])
def index():
    if request.method == 'POST':
        # capture the json data sent by the MSR webhook and dumps the values for each key as a string
        dtr_data = request.json
        event_type = json.dumps(dtr_data["type"])
        event_createdAt = json.dumps(dtr_data["createdAt"])
        contents_namespace = json.dumps(dtr_data["contents"]["namespace"])
        contents_repository = json.dumps(dtr_data["contents"]["repository"])
        contents_tag = json.dumps(dtr_data["contents"]["tag"])
        contents_imageName =  json.dumps(dtr_data["contents"]["imageName"])
        summary_namespace = json.dumps(dtr_data["contents"]["scanSummary"]["namespace"])
        summary_reponame = json.dumps(dtr_data["contents"]["scanSummary"]["reponame"])
        summary_tag = json.dumps(dtr_data["contents"]["scanSummary"]["tag"])
        summary_critical = json.dumps(dtr_data["contents"]["scanSummary"]["critical"])
        summary_major = json.dumps(dtr_data["contents"]["scanSummary"]["major"])
        summary_minor = json.dumps(dtr_data["contents"]["scanSummary"]["minor"])
        summary_lastscanstatus = json.dumps(dtr_data["contents"]["scanSummary"]["last_scan_status"])
        summary_checkcompletedat = json.dumps(dtr_data["contents"]["scanSummary"]["check_completed_at"])
        summary_shouldrescan = json.dumps(dtr_data["contents"]["scanSummary"]["should_rescan"])
        summary_hasforeignlayers = json.dumps(dtr_data["contents"]["scanSummary"]["has_foreign_layers"])
        event_location = json.dumps(dtr_data["location"])

        # format the text message that will be sent to the Teams channel
        teams_data = {"@context": "https://schema.org/extensions", "@type": "MessageCard", "title": "Image Scan Completed", "text": "Image scan completed for " + contents_imageName + " at " + summary_checkcompletedat.strip('"') + " with "+ summary_critical + " critical warnings, " + summary_major + " major warnings, and " + summary_minor + " minor warnings."}
        teams_url=config.refresh()
        response = requests.post(teams_url, data=json.dumps(teams_data),headers={'Content-Type': 'application/json'})
        return '', 200
    else:
        abort(400)
