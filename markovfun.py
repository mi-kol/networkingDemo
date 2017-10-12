import pykov
import socket
import struct
import numpy
import itertools
import random
import click

@click.command()
@click.option('--walk', default=1, help="Number of times you want to walk.")
def walker(walk):
    click.echo(markovChainGen().walk(walk))

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
    clients = []
    allPossibleTransitions = []
    transitionCoefficients = []
    straightCoefficients = []
    straightChunks = []
    for i in range(random.randint(1, 4)):
        clients.append(FauxClient(i+1, socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff))), random.randint(0, 65565)))

    for i in itertools.product(clients, repeat=2):
        allPossibleTransitions.append(i)

    chunked = numpy.array(list(chunks(allPossibleTransitions, 4)))

    for i in range(len(clients)):
        transitionCoefficients.append(numpy.random.dirichlet(np.ones(len(clients))*10, size=1))

    for i in transitionCoefficients:
        for j in i:
            for k in j:
                straightCoefficients.append(k)

    for i in chunked:
        for j in i:
            straightChunks.append(j)

    straightTuples = list(map(tuple, straightChunks))
    chain = dict(zip(straightTuples, straightCoefficients))
    T = pykov.Chain(chain)
    return T
