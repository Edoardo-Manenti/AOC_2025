import timeit
import unittest
from collections import defaultdict
from collections import Counter
from functools import reduce

class AocSolver():

    def setup(self, input_file_path = 'input.txt') -> str:
        return open("input.txt", "r").read()

    def dist(self, a, b):
        return sum(abs(int(x1)-int(x2))**2 for x1,x2 in zip(a, b))

    def matrix_distances(self, boxes):
        md = [[0 for _ in boxes] for _ in boxes]
        for i,box1 in enumerate(boxes):
            for j, box2 in enumerate(boxes):
                if i == j:
                    md[i][j] = float('inf')
                    continue
                md[i][j] = self.dist(box1, box2)
        return md


    def part_one(self, input: str) -> int:
        boxes = [tuple(line.split(",")) for line in input.split()]
        circuits = defaultdict(int)
        connections = set()
        id = 1
        md = self.matrix_distances(boxes)

        for i in range(10):
            dist = float('inf')
            b1,b2 = None, None
            for i,r in enumerate(md):
                for j,c in enumerate(r):
                    if i == j:
                        continue
                    if (boxes[i],boxes[j]) in connections:
                        continue
                    if (boxes[j],boxes[i]) in connections:
                        continue
                    if c < dist:
                        dist = c
                        b1,b2 = boxes[i], boxes[j]
            connections.add((b1,b2))
            connections.add((b2,b1))
            if circuits[b1] != 0:
                if circuits[b2] != 0:
                    v1,v2 = circuits[b1], circuits[b2]
                    for k,v in circuits.items():
                        if v == v1 or v == v2:
                            circuits[k] = id
                    id +=1
                else:
                    circuits[b2] = circuits[b1]
            else:
                if circuits[b2] != 0:
                    circuits[b1] = circuits[b2]
                else:
                    circuits[b1] = id
                    circuits[b2] = id
                    id +=1

        res = Counter(v for k,v in circuits.items())
        res = [v for k,v in sorted(res.items(), key=lambda item: item[1])]
        return res[-1]*res[-2]*res[-3]

    def part_two(self, input: str) -> int:
        boxes = [tuple(line.split(",")) for line in input.split()]
        circuits = defaultdict(int)
        connections = set()
        id = 1
        md = self.matrix_distances(boxes)
        last_connection = None

        while len(boxes) != len(circuits.keys()) \
            or (set(circuits.values()) == set([0]) \
                 or len(set(circuits.values())) != 1):
            dist = float('inf')
            b1,b2 = None, None
            for i,r in enumerate(md):
                for j,c in enumerate(r):
                    if i == j:
                        continue
                    if (boxes[i],boxes[j]) in connections:
                        continue
                    if (boxes[j],boxes[i]) in connections:
                        continue
                    if c < dist:
                        dist = c
                        b1,b2 = boxes[i], boxes[j]
            connections.add((b1,b2))
            connections.add((b2,b1))
            last_connection = (b1,b2)
            if circuits[b1] != 0:
                if circuits[b2] != 0:
                    v1,v2 = circuits[b1], circuits[b2]
                    for k,v in circuits.items():
                        if v == v1 or v == v2:
                            circuits[k] = id
                    id +=1
                else:
                    circuits[b2] = circuits[b1]
            else:
                if circuits[b2] != 0:
                    circuits[b1] = circuits[b2]
                else:
                    circuits[b1] = id
                    circuits[b2] = id
                    id +=1

        return int(last_connection[0][0])*int(last_connection[1][0])

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
        value = self.solver.part_one(self.test_part_one)

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
                  stmt='print(solver.part_one(problem))', 
                  number = iterations)
                  /iterations
    } sec")
    print(f"Time for part2: {
    timeit.timeit(setup=setup, 
                  stmt='print(solver.part_two(problem))', 
                  number = iterations)
                  /iterations
    } sec")
