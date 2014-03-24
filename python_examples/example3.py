import sys
import string
import random
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
        for x in xrange(size):
                c = Chromosome()
                c.random(len(goal))
                self.members.append(c)

    def display(self):
        print 'generation: ' + str(self.generation_number)
        for m in self.members:
            print m.code + ' (' + str(m.cost) + ')'

    def generation(self):
        (x.calculate_cost(self.goal) for x in self.members)
        self.display()
        self.members.sort(key=lambda x: x.cost)
        children = self.members[0].mate(self.members[1]);
        self.members = self.members[:-2] + children
        for m in self.members:
            m.mutate(0.5)
            m.calculate_cost(self.goal)
            if m.code == self.goal:
                self.members.sort(key=lambda x: x.cost)
                self.display()
                return True

        self.generation_number += 1
        time.sleep(0.01)
        self.generation()


def main():
    p = Population()
    p.generation()

if __name__ == '__main__':
    sys.exit(main())
