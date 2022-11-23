"""
Crocs (Fang Chen, Ziying Jian)
Softdev
K20 -- A RESTful Journey Skyward
2022-11-22
time spent: .7 hr
"""

from flask import Flask, render_template
from urllib.request import urlopen
import json

app = Flask(__name__)

@app.route('/')
def display():
  key = open('key_qrcode_monkey.txt', 'r').read()  # reads the key
  # print(key)
  url = f"https://qrcode-monkey.p.rapidapi.com/qr/custom/{key}" #  url format
  # print(url)
  data = urlopen(url)  # open the url and then using json.load to convert the page to a json file
  print(data)
  return render_template('main.html', url=data)

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
