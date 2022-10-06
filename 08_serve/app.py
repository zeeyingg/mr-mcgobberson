
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
    
        
print(random.choices(jobs, weights = weight)) #random.choices takes weight into account for each value
