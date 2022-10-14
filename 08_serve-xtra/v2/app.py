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
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return "No hablo queso!"

app.run()

'''
Notable new print statement is in line 14
    print("about to print __name__...")

We predict that the terminal will output "about to print /n __main__" Our predictions turned out to be right.

QCC:
* For some reason, Firefox does not exist on this local machine. We were unable to open using Vivaldi. 
* We received the error that this site couldn't be reached. Is this meant to happen? Or is this the result of using Vivaldi?
* Where did the print statement in line 14 go? We don't see it in the terminal.

'''

