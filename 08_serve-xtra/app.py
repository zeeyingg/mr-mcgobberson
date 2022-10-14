'''
ZIMZIM(mermann Telegram) Ziying Jian, Maya Nelson, Ivan Yeung
SoftDev
K08 -- Flask
2022-10-06
time spent: 1 hr
'''

'''
DISCOS:
- In order to have information displayed on a webpage, use HTML markers wrapped in Strings. 
For instance, we figured out that in order to create a line break, you must used "<br>", not "\n"
- In a module, there must only be one return statement culminating all the information to be displayed on the webpage.

QCC:
- What does debug do?
- Why doesn't the page display the result of multiple functions? 
- Is printing the __name__ necessary?
'''

import random

from csv import reader

jobs = []
weight = []

with open('occupations.csv','r') as file:
    contents = reader(file)
    count = 0
    rcount = 0
    for row in contents: #get the amount of rows to ignore the last line
        rcount +=1
    file.seek(0) # resets reader back to beginning
    for row in contents:
        if count != 0 and count != rcount-1:
            jobs.append(row[0])
            weight.append(int(float(row[1])*10)) #typecasts as float rather than string, then coverts to int
        count+=1
    
        
#print(random.choices(jobs, weights = weight)) #random.choices takes weight into account for each value
    
from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route

def hello_world():
    print(__name__)
    teamName = "<h3>" + "ZIMZIM(mermann Telegram): Ziying Jian, Ivan Yeung, Maya Nelson" + "</h3>" + "<br>"
    print("teamName printed")
    selectedOccup = "Selected occupation: " + random.choices(jobs, weights = weight)[0] 
     #Prints the only element in the list
    print("selectedOccup printed")
    listJobs = "<br>" + "List of jobs: " + str(jobs) 
    print("listJobs printed")
    return teamName + selectedOccup + listJobs

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()