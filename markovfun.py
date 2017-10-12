import pykov
import socket
import struct
import numpy
import itertools

from random import *

T = pykov.Chain()

class FauxClient:
    def __init__(self, id, ip, port):
        self.id = id
        self.ip = ip
        self.port = port


clients = []
for i in range(random.randint(1, 4)):
    clients.append(FauxClient(i+1, socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff))), random.randint(0, 65565)))

allPossibleTransitions = []
iterables = [clients, clients]
for i in itertools.product(*iterables):
    allPossibleTransitions.append(i)

relationalTransitions = []
selfTransitions = []
sRT = []
#sRT stands for sorted relational tarnsitions

for x,y in allPossibleTransitions:
    if x == y:
        selfTransitions.append((x,y))
    else:
        relationalTransitions.append((x,y))

for x,y in relationalTransitions:
    for a,b in relationalTransitions:
        if (a,b) == (y,x):
            sRT.append(([x,y], [a,b]))

#this can be really improved! make it not have duplicates while it's populating sRT
for i in sRT:
    for i in sRT:
        for j in sRT:
            if (i[0],i[1]) == (j[0],j[1]) and i != j:
                sRT.remove(j)
            if (i[0],i[1]) == (j[1], j[0]) and i != j:
                sRT.remove(j)

# so now we have a populated list of all the relational transitions, in the state that [[[a,b], [b,a]],[[a,c],[c,a]],...]

def markovBuilder():
    for x,y in sRT:
        chanceMatcher = np.random.dirichlet(np.ones(len(clients)), size=1)
        T.update({(x,y): })
