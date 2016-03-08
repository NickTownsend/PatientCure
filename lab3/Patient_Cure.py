# Nick Townsend
# Lab 3

ecoliCount = 0
zikaCount = 0
humanCount = 0
raoultellaCount = 0
unknownCount = 0

def select(theType):
    with open(theType) as f:
        sString = f.readlines()
        sString = map(lambda s: s.strip(), sString)
        sString = ''.join(str(e) for e in sString)
        return sString
    
rS = select('C:\\Users\\Nick\\Desktop\\Spring_2016\\lab3\\raoultella.txt')
zS = select('C:\\Users\\Nick\\Desktop\\Spring_2016\\lab3\\zika.txt')
hS = select('C:\\Users\\Nick\\Desktop\\Spring_2016\\lab3\\human.txt')
eS = select('C:\\Users\\Nick\\Desktop\\Spring_2016\\lab3\\ecoli.txt')

seq = { 'ecoli' : eS , 'zika' : zS , 'human' : hS ,
        'raoultella' : rS}

samples = []

with open('C:\\Users\\Nick\\Desktop\\Spring_2016\\lab3\\samples.txt', 'r') as f:
    for line in f:
        temp = line.replace('\n','')
        temp2 = temp.split(': ', 1)[-1]
        samples.append(temp2)

for x in samples:
    if x in eS:
        ecoliCount = ecoliCount + 1
    elif x in zS:
        zikaCount = zikaCount + 1
    elif x in hS:
        humanCount = humanCount + 1
    elif x in rS:
        raoultellaCount = raoultellaCount + 1
    else:
        unknownCount = unknownCount + 1

print "ecoli count : " ,  ecoliCount
print "human count : " , humanCount
print "raoultella count : " , raoultellaCount
print "unknown count : " , unknownCount
print "zika count : "  , zikaCount

print "after examining the data, we should treat for raoultella."














