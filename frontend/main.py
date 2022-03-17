from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

apiserver = "localhost:8000"

def get_asset(assetid):
    url = "http://" + apiserver + "/asset/" + assetid
    print(url)
    asset = requests.get(url)
    asset_data = json.loads(asset.text)
    return asset_data['data']


@app.route('/checkin/<asset_id>')
def index(asset_id):
    asset_data = get_asset(asset_id)
    return render_template('checkin.html')

@app.route('/code-check')
def codecheck():
    return render_template('code-check.html')
    

@app.route('/code-enter')
def codeenter():
    return render_template('code-enter.html')
