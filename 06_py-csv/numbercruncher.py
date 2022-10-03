'''
rEvERzE: Vivian Graeber, Ziying Jian, Raven (Ruiwen) Tang
SoftDev
K06 -- StI/O: Divine Your Destiny! / parse Python CSV file to build dictionary
2022-10-02
time spent: 1.3 hrs
'''

'''
DISCO:
* random.choices selects from a given list of elements based on the specified given list of percentage
* random.choices returns a list of elements, even if it's only one (but can return more)
* rsplit starts splitting a String according to a given character from the right
and can take an additional argument for the maximum number of splits you would like it to perform
* Although more limited than Java, there are multiple data types in Python, i.e. int, float
* random.choices can take in the weights parameter, but random.choice cannot

QCC:
* What would be the best way to test that the results of our script are correctly corresponding
to the percentages?
* Does random.choice return a different data type since it cannot output multiple choices?
* Is it possible to add multiple things to a dicitonary at the same time?
* What purpose does Total and Total percentage serve in the script?

HOW THIS SCRIPT WORKS:
1) Open and read occupations.csv
2) Clean up extraneous lines, pieces of information, and line breaks so that each
job and percentage are stored in a String list
4) Creates a dictionary with one key-value pair for Occupations and one key-value
pair for Percentage
5) Splits the job and percentage values from the right at the first comma
6) Stores independent values in the dictonary after cleaning up quotation marks and
typecasting percentages into float values
7) Randomly chooses occupation based on corresponding percentage
8) Returns title of occupation

'''

import random

info = open("occupations.csv", "r")
fullText = info.read() #creates a string called fullText
fullText = fullText[21:-12] #removes first "Job Class Percentage" and last line

jobClassList = fullText.split("\n") #separates string by each line
jobClassDictionary = {"Occupation":[], "Percentage":[]} #creates dictionary
for i in jobClassList:
    jobAndPercentage = i.rsplit(",", 1) #splits from the right once
    jobString = jobAndPercentage[0] #job title is stored
    if jobString[0] == '"': #checks for quotation marks in the job title
        jobString = jobString[1:-1] #removes quotes, exclusive
    percentageString = jobAndPercentage[1] #percentage of workforce in job is stored
    jobClassDictionary["Occupation"].append(jobString) #appended
    jobClassDictionary["Percentage"].append(float(percentageString)) #appended

def returnOccupation():
    returnJob = random.choices(jobClassDictionary["Occupation"], weights=jobClassDictionary["Percentage"]) #selects random job based on percentage, attributed to weight
    #this works because we imported random
    return returnJob[0] #creates String

for i in range(100):
    print(returnOccupation())
