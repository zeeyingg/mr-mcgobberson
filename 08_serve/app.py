'''
ZIMZIM(mermann Telegram) Ziying Jian, Maya Nelson, Ivan Yeung
SoftDev
K08 -- Flask
2022-10-04
time spent:
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
    return "Selected occupation: " + random.choices(jobs, weights = weight)[0] #Prints the only element in the list

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()