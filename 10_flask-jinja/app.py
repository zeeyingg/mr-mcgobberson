'''
ZIMZIM(mermann Telegram) Ziying Jian, Maya Nelson, Ivan Yeung
SoftDev
K02 -- flask-jinja
2022-10-13
time spent: .6 hr
'''

'''
PREDICTIONS:
Q0. We think that we won't be able to access the webpage because the render_template seems to be part of the route.
Q1. We think that the URL that the page will use to load will be the same as the other app.py files that we have run: http://127.0.0.1:5000
Q2. We think the first argument will be the html file that will be shown when we use the URL from flask when running the program.
The second parameter might be part of the address of the URL like the files that we requested in the static folder from 09.
The final parameter is a variable used to replace the variable holders({}) in the f string structures inside the html file.


DISCOS:
Q0.
Q1. The URL for the html page in the templates directory is actually http://127.0.0.1:5000/my_foist_template
Q2. The first argument is the html file that this program will render. 
The second argument will be the name of the tab when accessing model_tmplt.html after running app.py.
The third argument gives the f string in model_tmplt.html the variable it uses.

- Both fire fox and Vivaldi return a page with:
{% for item in collection %} {{ item }}
{% endfor %}
when opening the html file from the file directory.
- Opening the model_tmplt.html file on local machine does not replace the variables in the f string.
-When opening an html file from the directory on local machine, it will not have https. 
Instead it will have file followed by the route to the html from machine.
- When we ran the program, the url directed us to a webpage with "No hablo queso"
- When we use the url 'http://127.0.0.1:5000/my_foist_template', we get the webpage with the html of model_templt.
The webpage shows the the elements of the list coll and there is a breakline after each element.
- When model_templt is rendered, the f string is computed and the variables are replaced.


QCC:
- When we ran the app.py program in class, the link that was returned was not able to direct us to a working webpage.

'''

from flask import Flask, render_template #Q0: What will happen if you remove render_template from this line? (log your prediction before you pull the trigger...)
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"

coll = [0,1,1,2,3,5,8]

@app.route("/my_foist_template") #Q1: Can all of your teammates confidently predict the URL to use to load this page?
def test_tmplt():
    return render_template( 'model_tmplt.html', foo="fooooo", collection=coll) #Q2: What is the significance of each argument? Simplest, most concise answer best.

if __name__ == "__main__":
    app.debug = True
    app.run()
