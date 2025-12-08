import timeit
import unittest

class AocSolver():

    def setup(self, input_file_path = 'input.txt') -> str:
        return open("input.txt", "r").read()

    def init(self):
        self.boxes = [list(map(int, line.split(','))) for line in self.input.split()]
        self.N = len(self.boxes)
        self.parents = list(range(self.N))
        self.sizes = [1]*self.N
        self.pq = [(self.dist(self.boxes[i], self.boxes[j]), i, j) 
            for i in range(self.N) for j in range(i+1, self.N)]
        self.pq.sort(key=lambda item: item[0], reverse=True)

    def find(self, a):
        if self.parents[a] != a:
            self.parents[a] = self.find(self.parents[a])
        return self.parents[a]

    def union(self, a,b):
        a,b = self.find(a), self.find(b)

        if a == b:
            return
        if self.sizes[b] > self.sizes[a]:
            a,b = b,a

        self.parents[b] = a

        self.sizes[a] += self.sizes[b]
        self.sizes[b] = 0

    def dist(self, a, b):
        return sum(abs(int(x1)-int(x2))**2 for x1,x2 in zip(a, b))

    def part_one(self, input, iterations: int) -> int:
        self.input = input
        self.init()
        for _ in range(iterations):
            dist, a, b = self.pq.pop()
            self.union(a, b)

        self.sizes.sort(reverse = True)
        return self.sizes[0]*self.sizes[1]*self.sizes[2]

    def part_two(self, input) -> int:
        self.input = input
        self.init()
        while True:
            dist, a, b = self.pq.pop()
            self.union(a, b)

            if self.sizes[self.find(a)] == self.N:
                return self.boxes[a][0]*self.boxes[b][0]

class AocSolutionTest(unittest.TestCase):
    def setUp(self):
        self.test_part_one = """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
        """
        self.solution_part_one = 40

        self.test_part_two = """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
        """
        self.solution_part_two = 25272

        self.solver = AocSolver()

    def test_part_one(self):
        value = self.solver.part_one(self.test_part_one, 10)

        self.assertIsNotNone(value)
        self.assertEqual(value, self.solution_part_one)

    def test_part_two(self):
        value = self.solver.part_two(self.test_part_two)

        self.assertIsNotNone(value)
        self.assertEqual(value, self.solution_part_two)

if __name__ == '__main__':
    setup = '''
from aoc import AocSolver
solver = AocSolver()
problem = solver.setup()
    '''
    iterations = 1
    print(f"Time for part1: {
    timeit.timeit(setup=setup, 
                  stmt='print(solver.part_one(problem,1000))', 
                  number = iterations)
                  /iterations
    } sec")
    print(f"Time for part2: {
    timeit.timeit(setup=setup, 
                  stmt='print(solver.part_two(problem))', 
                  number = iterations)
                  /iterations
    } sec")
