"""
My Python spin on this:
http://burakkanber.com/blog/machine-learning-genetic-algorithms-in-javascript-part-2/
"""

import sys
import random
from elements import elements


class Chromosome(object):
    def __init__(self, members):
        self.members = members
        self.weight = 0
        self.value = 0
        self.max_weight = 1000
        self.mutation_rate = 0.7
        self.score = 0
        for element in self.members:
            if not self.members[element].get('active') is None:
                self.members[element]['active'] = int(round(random.random()))
        self.mutate()
        self.calc_score()

    def mutate(self):
        if self.mutation_rate < random.random():
            return
        element = self.members.keys()[random.randint(0, len(self.members.keys()) - 1)]
        self.members[element]['active'] = 0 if self.members[element]['active'] else 1

    def calc_score(self):
        self.value = 0
        self.weight = 0
        self.score = 0
        for element in self.members:
            if self.members[element]['active']:
                self.value += self.members[element]['value']
                self.weight += self.members[element]['weight']
        self.score = self.value
        if self.weight > self.max_weight:
            self.score -= (self.weight - self.max_weight) * 50
        return self.score

    def crossover(self, other):
        child1 = {}
        child2 = {}
        i = 0
        for element in elements:
            if i % 2 == 0:
                child1[element] = self.members[element]
                child2[element] = other.members[element]
            else:
                child2[element] = self.members[element]
                child1[element] = other.members[element]
            i += 1
        child1 = Chromosome(child1)
        child2 = Chromosome(child2)
        return [child1, child2]


def main():
    c1 = Chromosome(elements)

if __name__ == '__main__':
    sys.exit(main())
