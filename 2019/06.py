from copy import copy
from helper import read_data

def decoder(line):
    a, b = line.split(')')
    return (a, b)

class Planet(object):
    def __init__(self, name):
        self.name = name
        self.subplanets = []
        self.parent = None
        self.s = None
        self.prev = None

    def add(self, subplanet):
        self.subplanets.append(subplanet)
        subplanet.parent = self

    def sum(self, prev=0):
        if self.s is None:
            self.prev = prev
            s = prev
            for p in self.subplanets:
                s += p.sum(prev=prev+1)
            self.s = s
        return self.s

def generate_orbits(olist):
    d = dict()

    for o, s in olist:
       if o not in d:
            d[o] = Planet(o)
       if s not in d:
            d[s] = Planet(s)
       d[o].add(d[s])
    return d

def root(d):
    for name, planet in d.items():
       if planet.parent is None:
          return planet


def update_max(p1, p2):
    if p1.prev > p2.prev:
       return p1.parent, p2
    else:
       return p1, p2.parent

def dist(orbit_data, p1n, p2n):
    root(orbit_data).sum()
    return _dist(orbit_data[p1n].parent, orbit_data[p2n].parent)


def _dist(p1, p2):
    if p1 == p2:
       return 0
    else:
       p1, p2 = update_max(p1, p2)
       return 1 + _dist(p1, p2)

if __name__ == '__main__':
    orbits = read_data('06.txt', converter=decoder)
    test_data = [('COM','B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F'), ('D', 'I'), ('B', 'G'), ('G', 'H'), ('E', 'J'), ('J', 'K'), ('K', 'L')]
    test_center = generate_orbits(test_data)
    #print test_center.sum()
    orbits = generate_orbits(orbits)
    print root(orbits).sum()
    test_data2 = copy(test_data)
    test_data2.extend([('K', 'YOU'), ('I', 'SAN')])
    test_center2 = generate_orbits(test_data2)
    #print dist(test_center2, 'YOU', 'SAN')
    print dist(orbits, 'YOU', 'SAN')
