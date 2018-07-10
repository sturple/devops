from flask import Flask, render_template, json, url_for
import os


@app.route("/")
def hello():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "data", "data.json")
    data = json.load(open(json_url))
    return 'hello'

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)