'''
ZEM ZEM :: Maya Nelson, Ziying Jian, Elizabeth Paperno
SoftDev
K04 -- Creating a dictionary of crews
2022-09-22
time spent: 0.5 hours
'''

'''
DISCO:
* To import a statement, use from... import...
* randint() is an imported function to generate a random integer
* The conditions for randint() are both inclusive
* Random number should be 2, 7, or 8

QCC:
* How do we get the full names of all thinkerens in all periods?
* Is devolist a list? Are multiple values contained in a key:value pair a list?
* What are  other ways trios randomly generated values?

OPS SUMMARY:
A dictionary holds a key:value pair. Because their are multiple values held, we need to first access
the key before accessing a value. Random generate an index and access a random key. After acessing
the key, you'll be able to access a list of values. Store that list of values to a variable, and then
randomly generate an index contained in the list. Using the index, return the specific value of the list.
'''

from random import randint

krewes = {2:["NICHOLAS",  "ANTHONY",  "BRIAN",  "SAMUEL",  "JULIA",  "YUSHA",  "CORINA",  "CRAIG",  "FANG MIN",  "JEFF",  "KONSTANTIN",  "AARON",  "VIVIAN",  "AYMAN",  "TALIA",  "FAIZA",  "ZIYING",  "YUK KWAN",  "DANIEL",  "WEICHEN",  "MAYA",  "ELIZABETH",  "ANDREW",  "VANSH",  "JONATHAN",  "ABID",  "WILLIAM",  "HUI",  "ANSON",  "KEVIN",  "DANIEL",  "IVAN",  "JASMINE",  "JEFFREY"],
 7:["DIANA",  "DAVID",  "SAM",  "PRATTAY",  "ANNA",  "JING YI",  "ADEN",  "EMERSON",  "RUSSELL",  "JACOB",  "WILLIAM",  "NADA",  "SAMANTHA",  "IAN",  "MARC",  "ANJINI",  "JEREMY",  "LAUREN",  "KEVIN",  "RAVINDRA",  "SADI",  "EMILY",  "GITAE",  "MAY",  "MAHIR",  "VIVIAN",  "GABRIEL",  "BRIANNA",  "JUN HONG",  "JOSEPH",  "MATTHEW",  "JAMES",  "THOMAS",  "NICOLE",  "Karen"], 
 8:["ALEKSANDRA",  "NAKIB",  "AMEER",  "HENRY",  "DONALD",  "YAT LONG",  "SEBASTIAN",  "DAVID",  "YUKI",  "SHAFIUL",  "DANIEL",  "SELENA",  "JOSEPH",  "SHINJI",  "RYAN",  "APRIL",  "ERICA",  "JIAN HONG",  "VERIT",  "JOSHUA",  "WILSON",  "AAHAN",  "GORDON",  "JUSTIN",  "MAYA",  "FAIYAZ",  "SHREYA",  "ERIC",  "JEFFERY",  "BRIAN",  "KEVIN",  "SAMSON",  "BRIAN",  "HARRY",  "wanying"]
 }


def selectDevo():
    randomCrew = randint(0,2)
    if randomCrew == 0:
        randomCrew = 7
    elif randomCrew == 1:
        randomCrew = 8
    devoList = krewes[randomCrew]

    randomDevo = randint(0,len(devoList)-1)
    return devoList[randomDevo]

for i in range(10):
    print(selectDevo())
