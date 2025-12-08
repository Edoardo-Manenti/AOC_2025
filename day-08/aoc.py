import timeit
import unittest
import heapq
from collections import defaultdict, Counter

class AocSolver():

    def setup(self, input_file_path = 'input.txt') -> str:
        self.circuits = defaultdict(int)
        self.connections = set()
        self.id = 1
        self.pq = []
        input = open("input.txt", "r").read()
        self.boxes = [tuple(line.split(",")) for line in input.split()]
        self.build_pq()

    def dist(self, a, b):
        return sum(abs(int(x1)-int(x2))**2 for x1,x2 in zip(a, b))

    def build_pq(self):
        for i,box1 in enumerate(self.boxes):
            for j, box2 in enumerate(self.boxes):
                if i == j:
                    continue
                dist = self.dist(box1, box2)
                heapq.heappush(self.pq, (dist, (i,j)))

    def next_closest_connection(self):
            while self.pq:
                conn = heapq.heappop(self.pq)
                if conn[1] not in self.connections:
                    return conn[1]

    def connect(self, connection):
        b1,b2 = connection
        self.connections.add((b1,b2))
        self.connections.add((b2,b1))
        if self.circuits[b1] != 0:
            if self.circuits[b2] != 0:
                v1,v2 = self.circuits[b1], self.circuits[b2]
                for k,v in self.circuits.items():
                    if v == v1 or v == v2:
                        self.circuits[k] = self.id
                self.id +=1
            else:
                self.circuits[b2] = self.circuits[b1]
        else:
            if self.circuits[b2] != 0:
                self.circuits[b1] = self.circuits[b2]
            else:
                self.circuits[b1] = self.id
                self.circuits[b2] = self.id
                self.id +=1

    def part_one(self, iterations: int) -> int:
        for _ in range(iterations):
            connection = self.next_closest_connection()
            self.connect(connection)

        res = Counter(v for k,v in self.circuits.items())
        res = [v for k,v in sorted(res.items(), key=lambda item: item[1])]
        return res[-1]*res[-2]*res[-3]

    def part_two(self) -> int:
        last_connection = None
        while len(self.circuits.keys()) < len(self.boxes) \
            or \
            len(set(self.circuits.values())) > 1:
            connection = self.next_closest_connection()
            self.connect(connection)
            last_connection = connection

        b1 = self.boxes[last_connection[0]]
        b2 = self.boxes[last_connection[1]]
        return [int(a)*int(b) for a,b in zip(b1,b2)][0]

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
        value = self.solver.part_one(10)

        self.assertIsNotNone(value)
        self.assertEqual(value, self.solution_part_one)

    def test_part_two(self):
        value = self.solver.part_two()

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
                  stmt='print(solver.part_one(1000))', 
                  number = iterations)
                  /iterations
    } sec")
    print(f"Time for part2: {
    timeit.timeit(setup=setup, 
                  stmt='print(solver.part_two())', 
                  number = iterations)
                  /iterations
    } sec")
