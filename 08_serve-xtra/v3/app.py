'''
ZIMZIM(mermann Telegram) Ziying Jian, Maya Nelson, Ivan Yeung
SoftDev
K08 -- Flask
2022-10-04
time spent:
'''

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return "No hablo queso!"

app.debug = True
app.run()

'''
NOTABLES:
* Line 18 is newly added and NOTABLE

PREDICTIONS:
* We predict that in the terminal, the debug mode will be set to ON.

Our predictions were right, but we also got some other information from the terminal.
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 441-963-763

QCC:
* What is app.debug? What does setting it True do?
* What is the Debugger PIN?
'''
