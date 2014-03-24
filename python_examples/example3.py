"""
My Python spin on this:
http://burakkanber.com/blog/machine-learning-genetic-algorithms-part-1-javascript/
"""

from optparse import OptionParser
import random
import string
import sys
import time


class Chromosome(object):
    def __init__(self, code=''):
        self.code = code
        self.cost = 9999

    def random(self, length):
        self.code = ''.join(random.choice(string.printable) for x in xrange(length))

    def mate(self, chromosome):
        child1 = ''
        child2 = ''
        for c1, c2, i in zip(self.code, chromosome.code, xrange(len(self.code))):
            if i % 2 == 0:
                child1 += c1
                child2 += c2
            else:
                child1 += c2
                child2 += c1
        return [Chromosome(child1), Chromosome(child2)]

    def mutate(self, chance):
        if chance < random.random():
            return
        index_to_change = random.randint(0, len(self.code) - 1)
        up_or_down = random.randint(-1, 1)
        new_code = ''
        for i in xrange(0, len(self.code)):
            if i == index_to_change:
                try:
                    new_code += string.printable[string.printable.index(self.code[i]) + up_or_down]
                except IndexError:
                    new_code += string.printable[string.printable.index(self.code[i]) - 1]
            else:
                new_code += self.code[i]
        self.code = new_code

    def calculate_cost(self, compare_to):
        total = 0
        for c1, c2 in zip(self.code, compare_to):
            total += abs(string.printable.index(c1) - string.printable.index(c2))
        self.cost = total


class Population(object):
    def __init__(self, goal='hello', size=20):
        self.goal = goal
        self.generation_number = 0
        self.members = []
        for i in xrange(size):
            c = Chromosome()
            c.random(len(goal))
            c.calculate_cost(self.goal)
            self.members.append(c)
        self.members.sort(key=lambda x: x.cost)

    def display(self):
        print 'generation: ' + str(self.generation_number)
        for m in self.members:
            print m.code + ' (' + str(m.cost) + ')'

    def generation(self):
        for m in self.members:
            if m.code == self.goal:
                self.display()
                return True
        children = self.members[0].mate(self.members[1])
        self.members = self.members[:-2] + children
        for m in self.members:
            m.mutate(0.5)
            m.calculate_cost(self.goal)
        self.members.sort(key=lambda x: x.cost)
        self.display()
        self.generation_number += 1
        return False


def main(message, population_size):
    p = Population(message, population_size)
    p.display()
    while not p.generation():
        time.sleep(0.01)

if __name__ == '__main__':
    usage = "usage: %prog [options]"
    parser = OptionParser(usage)
    parser.add_option("-m", "--message", type="string", dest="message",
                      default='hello', help="message to evolve to")
    parser.add_option("-p", "--population_size", type="int", dest="population_size",
                      default=20, help="population size")
    (options, args) = parser.parse_args()
    sys.exit(main(options.message, options.population_size))
