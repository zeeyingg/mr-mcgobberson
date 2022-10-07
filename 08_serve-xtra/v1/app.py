'''
ZIMZIM(mermann Telegram) Ziying Jian, Maya Nelson, Ivan Yueng
SoftDev
K08 -- Flask
2022-10-04
time spent:
'''

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()

'''
DISCO: 
* The Flask application name is not printed, so we predict that the terminal will not output "__main__"
* Our prediction turned out to be wrong -- the Flask application name was still printed 
    Serving Flask app 'app'

QCC:
* Why is the __name__ 'app' and not "__main__"?
'''

