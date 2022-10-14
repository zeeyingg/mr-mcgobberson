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
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()

'''
NOTABLES:
* Line 18 is added
    if __name__ == "__main__":
* Line 14 is changed
`   print("the __name__ of this module is... ")

PREDICTIONS:
* We predict this file will run because it is NOT imported
* Also, from our past results, we've found that __name__ is printed out as __main__, so this conditional is true
`       
OUR PREDICTION WAS RIGHT!!!

QCC:
* What will happen if the file is not true? What happens if the name is changed?
* What is the purpose of having this line?
* What is a module? Why is it important in Flask?
* What does debug even do?

'''