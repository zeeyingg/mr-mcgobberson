"""
rEvERzE: Ziying Jian, Vivian Graeber, Raven (Ruiwen) Tang
SoftDev
K05 -- bitstream / randomly print a devo AND corresponding ducky, given a text file
2022-09-29
time spent: 0.6 hrs
"""
"""
DISCO:
* Sorting a list of lists will reorder the elements alphabetically, in the order of the elements. So, in this case, infoStrings is sorted by the period of each devo first, then the devo's name, and lastly, if necessary, the ducky's name.
* choice and randrange are different in that choice randomly selects an element of a list, while randrange generates a random integer. We needed to use randrange here because we wanted to ensure that the index of the devo name and the index of the ducky name corresponded (the ducky generated was in fact the generated devo's ducky).
* Our algorithm should still work even if there are duplicates in devo names or ducky names, because we don't require the devo names or ducky names to be keys in our dictionary. Instead, we use the period as the key, and the names are not overridden - they maintian their separation as different elements of the value lists.
QCC:
* Why is there a new line character at the end of our krewes.txt content, even though the file only shows as one line?
* What are some alternative ways of organizing a dictionary for this task? Are there other characteristics that can be used for the keys (here, we needed to hard code the periods in, and our code is not robust for a situation where we don't know the potential periods in advance)?
* Is there a way to keep the devo and ducky names together in our dictionary?
OPS:
* Open the text file.
* Remove extraneous characters from the end of the text file.
* Split the text by "@@@" --> store in a list.
* Split that list by "$$$" (each devo's info should be in its own list within this list, with period, name, and ducky in separate elements).
* Set up a dictionary, with keys for each period and empty lists for the values.
* Iterate through the list of information, and check the first element (period) of each inner list. Add the other two elements (devo name and ducky name) to the corresponding key in the dictionary.
* Generate a random period.
* Generate a random pair for that period.
* Print the devo name, ducky name, and period.
"""
import random

info = open("krewes.txt", "r")
fullText = info.read()
fullText = fullText[:-4] #removes new line character (\n) and @@@ at the end
infoChunks = fullText.split("@@@") #splits into period/name/ducky
infoStrings = []
for i in infoChunks:
    infoStrings.append(i.split("$$$")) #splits into more specific info
krewes = {2:[], 7:[], 8:[]}
for i in infoStrings:
    #populates lists in krewes dictionary
    #each pair of devos and duckies is grouped together in a list
    pairs = [i[1], i[2]]
    if(i[0] == "2"):
        krewes[2].append(pairs)
    elif(i[0] == "7"):
        krewes[7].append(pairs)
    else:
        krewes[8].append(pairs)
pd_list = list(krewes.keys()) #creates a list of the keys in the dictionary
pd = random.choice(pd_list)#randomly selects a period
pair = random.choice(krewes[pd])#randomly selects a devo and ducky pair from the period
print(pair[0] + " and " + pair[1] + " from pd " + str(pd))
info.close()