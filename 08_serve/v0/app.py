'''
ZIMZIM(mermann Telegram) Ziying Jian, Maya Nelson, Ivan Yeung
SoftDev
K08 -- Flask
2022-10-04
time spent:
'''

from flask import Flask
app = Flask(__name__) #Creates a Flask application called __name__

@app.route("/") #This is a route
def hello_world():
    print(__name__) #Prints "__main__" in the terminal
    return "No hablo queso!"  #Prints "No hablo queso" in th website

app.run()  #run() runs the function

'''
NOTABLES:
* When we replaced __name__ with 'foo', we didn't receive an error and the "No hablo queso" was still printed!
In the terminal, we received this: Serving Flask app 'foo'

PREDICTIONS:
* The name of the Flask application is printed in the terminal.

QCC:
* How is hello_world() being run using run()? Does run() run all the functions in the file?
* What do the underscores denote in __name__?
* Running app.py on my personal machine doesn't create a hyperlink (but still opens if pasted in browser!)
* What does the above DISCO mean?!
* As a programmer, how can we judge when to name the app and when to insert this special Python variable?
'''
