from flask import Flask
from flask import request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    base_grant_url = request.args.get('base_grant_url')
    user_continue_url = request.args.get('user_continue_url')
    node_mac = request.args.get('node_mac')
    client_ip = request.args.get('client_ip')
    client_mac = request.args.get('client_mac')
    return redirect(base_grant_url + "?continue_url=https://www.dattics.com/&duration=2592000", code=302)