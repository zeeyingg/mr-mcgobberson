"""
Blue Haired Gals With Pronouns: Jasmine Yuen, Talia Hsia, Ziying Jian
SoftDev
K19 - Flask app that uses session capabilites to allow user to login and logout
2022-11-03
time spent:
"""

from flask import Flask
from flask import render_template
from flask import request
from flask import session

app = Flask(__name__)

username = "ziying"
password = "john"

def authenticate(user, passw):
    return (user == username and passw == password)

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    return render_template( 'login.html' )

@app.route("/login", methods=['GET', 'POST'])
def response_template():
    if authenticate(request.args['username'], request.args['password']):
        return render_template('response.html', functional="WORKS!")
    return render_template('response.html', functional="DOESN'T WORK =()")

# @app.route('/logout')
# def logout():
#     # remove the username from the session if it's there
#     session.pop('username', None)
#     return redirect(url_for('index'))

if __name__ == "__main__":
    app.debug = True
    app.run()
