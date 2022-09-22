'''
ZEM ZEM :: Maya Nelson, Ziying Jian, Elizabeth Paperno
SoftDev
K04 -- Creating a dictionary of crews
2022-09-22
time spent: <elapsed time in hours, rounded to nearest tenth>
'''

'''
DISCO:
* To import a statement, use from... import...
* randint() helps you 

QCC:
* How do we get the full names of all thinkerens in all periods?

OPS SUMMARY:
'''

from random import randint

krewes = {2:['a', 'b', 'c'], 7:['d', 'e', 'f'], 8:['g', 'h', 'i']}

def selectDevo():
    randomCrew = randint(0,2)
    return randomCrew

print(selectDevo())