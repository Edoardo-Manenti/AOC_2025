import timeit
import unittest

class AocSolver():

    def setup(self, input_file_path = 'input.txt') -> str:
        return open("input.txt", "r").read()

    def parse_inputs(self, input):
        ranges, ids = input.split("\n\n")
        ranges = [[int(r) for r in range.split("-")] for range in ranges.split()]
        ids = [int(id) for id in ids.split()]

        return ids, ranges


    def squash_ranges(self, ranges):
        ranges.sort(key=lambda x: x[0])

        new_ranges = []

        for range in ranges:
            if not new_ranges or range[0] > new_ranges[-1][1]+1:
                new_ranges.append(range)
            elif range[1] <= new_ranges[-1][1]:
                continue
            else:
                new_ranges[-1][1] = range[1]

        return new_ranges

    def part_one(self, input: str) -> int:
        ids, ranges = self.parse_inputs(input)

        ranges = self.squash_ranges(ranges)

        return sum(1 
            if any(a<=id<=b for a,b in ranges) 
            else 0 
            for id in ids)


    def part_two(self, input: str) -> int:
        ids, ranges = self.parse_inputs(input)

        ranges = self.squash_ranges(ranges)

        return sum(b+1-a for a,b in ranges)

class AocSolutionTest(unittest.TestCase):
    def setUp(self):
        self.test_part_one = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
        """
        self.solution_part_one = 3

        self.test_part_two = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
        """
        self.solution_part_two = 14

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
