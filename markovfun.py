import pykov
import socket
import struct
import numpy as numpy
import itertools
import random
import pprint
import warnings

clients = []
allPossibleTransitions = []
transitionCoefficients = []
straightCoefficients = []
straightChunks = []



def output():
    '''generatedChain = markovChainGen()
    print(len(clients))
    print("Generated Clients")
    for i in clients:
        print("ClientID: " + str(i.id))
        print("Client IP/Port: " + i.ip + ":" + str(i.port))
        print("-----------------------------")
    print("Possible State Changes")
    for x,y in allPossibleTransitions:
        print("Start State: " + x.ip + " || Dest State: " + y.ip)
    print("------------------------------")
    print("Markov Successor Grid\n")
    generatedChain.succ()
    generatedChain'''
    T = markovChainGen()
    for i in T.walk(random.randint(1,100)):
        print(i.ip)

class FauxClient:
    def __init__(self, id, ip, port):
        self.id = id
        self.ip = ip
        self.port = port

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]



def markovChainGen():
    for i in range(random.randint(2, 4)):
        clients.append(FauxClient(i+1, socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff))), random.randint(0, 65565)))

    for i in itertools.product(clients, repeat=2):
        allPossibleTransitions.append(i)

    chunked = numpy.array(list(chunks(allPossibleTransitions, len(clients))))
    #pprint.pprint(chunked)

    for i in range(len(clients)):
        transitionCoefficients.append(numpy.random.dirichlet(numpy.ones(len(clients))*10, size=1))
    #pprint.pprint(transitionCoefficients)
    for i in transitionCoefficients:
        for j in i:
            for k in j:
                straightCoefficients.append(k)

    #print(straightCoefficients)
    for i in chunked:
        for j in i:
            straightChunks.append(j)
    #pprint.pprint(straightChunks)
    straightTuples = list(map(tuple, straightChunks))
    #pprint.pprint(straightTuples)
    chain = dict(zip(straightTuples, straightCoefficients))
    #pprint.pprint(chain)
    T = pykov.Chain(chain)
    return T

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    output()
