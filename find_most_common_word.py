# find the most common word

filename = input('Enter file name : ')
if len(filename) < 1:
    filename = 'clown.txt'
hand = open(filename)
di = dict()

for lin in hand:
    # to replace the puctuations with white spaces
    pnct = '!#$%&()*+,-./:;<=>?@[]^_`{|}~'
    lst = list(pnct)

    for p in lst:
        lin = lin.replace(p, ' ')
    # to make all the words lowercase
    lin = lin.lower()
    # to remove the white spaces from the end
    lin = lin.rstrip()
    # to split the lines in to a list of words
    words = lin.split()
    for w in words:
        di[w] = di.get(w, 0) + 1


largestcount = -1
theword = None
for k, v in di.items():
    if v > largestcount:
        largestcount = v
        theword = k


print(theword, largestcount)
