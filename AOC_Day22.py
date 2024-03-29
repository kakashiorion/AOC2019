input=["cut -1353",
"deal with increment 63",
"cut -716",
"deal with increment 55",
"cut 1364",
"deal with increment 61",
"cut 1723",
"deal into new stack",
"deal with increment 51",
"cut 11",
"deal with increment 65",
"cut -6297",
"deal with increment 69",
"cut -3560",
"deal with increment 20",
"cut 1177",
"deal with increment 29",
"cut 6033",
"deal with increment 3",
"cut -3564",
"deal into new stack",
"cut 6447",
"deal into new stack",
"cut -4030",
"deal with increment 3",
"cut -6511",
"deal with increment 42",
"cut -8748",
"deal with increment 38",
"cut 5816",
"deal with increment 73",
"cut 9892",
"deal with increment 16",
"cut -9815",
"deal with increment 10",
"cut 673",
"deal with increment 12",
"cut 4518",
"deal with increment 52",
"cut 9464",
"deal with increment 68",
"cut 902",
"deal with increment 11",
"deal into new stack",
"deal with increment 45",
"cut -5167",
"deal with increment 68",
"deal into new stack",
"deal with increment 24",
"cut -8945",
"deal into new stack",
"deal with increment 36",
"cut 3195",
"deal with increment 52",
"cut -1494",
"deal with increment 11",
"cut -9658",
"deal into new stack",
"cut -4689",
"deal with increment 34",
"cut -9697",
"deal with increment 39",
"cut -6857",
"deal with increment 19",
"cut -6790",
"deal with increment 59",
"deal into new stack",
"deal with increment 52",
"cut -9354",
"deal with increment 71",
"cut 8815",
"deal with increment 2",
"cut 6618",
"deal with increment 47",
"cut -6746",
"deal into new stack",
"cut 1336",
"deal with increment 53",
"cut 6655",
"deal with increment 17",
"cut 8941",
"deal with increment 25",
"cut -3046",
"deal with increment 14",
"cut -7818",
"deal with increment 25",
"cut 4140",
"deal with increment 60",
"cut 6459",
"deal with increment 27",
"cut -6791",
"deal into new stack",
"cut 3821",
"deal with increment 13",
"cut 3157",
"deal with increment 13",
"cut 8524",
"deal into new stack",
"deal with increment 12",
"cut 5944"]



def newDeck(n):
    deck = []
    for i in range(n):
        deck.append(i)
    return deck

def dealNew(deck):
    deck.reverse()

def dealIncrementN(deck,n,p):
    new = deck.copy()
    i=0
    for x in deck:
        new[i]=x
        i=i+n
        if i>p-1:
            i=i-p
    return new

def cutN(deck,n):
    cut=deck[:n]
    new=deck[n:]
    new=new+cut
    return new

def compute(p):
    for s in input:
        if s[:3]=="cut":
            n=int(s[4:])
            deck = cutN(deck,n)
        elif s[:9]=="deal with":
            n=int(s[20:])
            deck = dealIncrementN(deck,n,p)
        else:
            deck.reverse()

#Part1
# p=10007
# deck = newDeck(p)
# compute(p)
# print(deck)
# print(deck.index(2019))
#Part1 answer: 3589

#Part 2
p=119315717514047
deck = newDeck(p)
for j in range(101741582076661):
    compute(p)

print(deck[2020])

