'''
ZIMZIM(mermann Telegram) Ziying Jian, Maya Nelson, Ivan Yeung
SoftDev
K09 -- Some Things Never Change
2022-10-011
time spent: 0.5 hr
'''

# DEMO 
# basics of /static folder

from flask import Flask
app = Flask(__name__) 

@app.route("/")       
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
