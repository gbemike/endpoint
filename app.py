from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route("/api", methods = ["GET"])
def endpoint():
    # The endpoint should take two GET request query parameters
    slack_name = request.args.get('slack_name', 'Gbemike Olowe')
    track = request.args.get('track', 'backend')

    response = {
        'slack_name':slack_name,
        'current_day': datetime.datetime.today().strftime('%A'),
        'utc_time': datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        'track':track,
        'github_file_url': ,
        'github_repo_url':'https://github.com/gbemike/endpoint',
        'status_code':100
    }

    return response