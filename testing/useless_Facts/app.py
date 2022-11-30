import json
import requests
from flask import Flask, render_template
import jinja2

app = Flask(__name__)

@app.route('/')
def display():
    url = "https://uselessfacts.jsph.pl/random.json"
    data = json.loads(requests.get(url).text)
    return render_template("index.html", fact=data['text'])

if __name__ == "__main__":
    app.debug = True
    app.run()