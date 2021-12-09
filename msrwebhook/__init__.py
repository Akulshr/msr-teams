# Import Flask and all the API endpoints for the msrwebhook application

from flask import Flask
from msrwebhook.main.controllers import main
from msrwebhook.addmanifest.controllers import addmanifest
from msrwebhook.delete.controllers import delete
from msrwebhook.delmanifest.controllers import delmanifest
from msrwebhook.promote.controllers import promote
from msrwebhook.push.controllers import push
from msrwebhook.scan.controllers import scan
from msrwebhook.scanfail.controllers import scanfail

app = Flask(__name__)

# Regiser all the api endpoints for the application and define the associated URL prefix 
app.register_blueprint(main, url_prefix='/')
app.register_blueprint(addmanifest, url_prefix='/addmanifest')
app.register_blueprint(delete, url_prefix='/delete')
app.register_blueprint(delmanifest, url_prefix='/delmanifest')
app.register_blueprint(promote, url_prefix='/promote')
app.register_blueprint(push, url_prefix='/push')
app.register_blueprint(scan, url_prefix='/scan')
app.register_blueprint(scanfail, url_prefix='/scanfail')
