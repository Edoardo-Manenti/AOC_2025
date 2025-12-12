import timeit
import unittest

class AocSolver():

    def setup(self, input_file_path = 'input.txt') -> str:
        return open("input.txt", "r").read()

    def part_one(self, input: str) -> int:
        problem = input.split('\n\n')
        tiles, floors = problem[:-1], problem[-1]
        tiles = [tile.strip().split(':')[1] for tile in tiles]
        floors = [floor.strip().split(':') for floor in floors.strip().split('\n')]
        avails = [floor[1].strip().split(' ') for floor in floors]
        avails = [list(map(int, avail)) for avail in avails]
        floors = [list(map(int, floor[0].split('x'))) for floor in floors]

        c_tiles = [sum(1 if c == '#' else 0 for c in tile) for tile in tiles]

        total = 0
        for i,floor in enumerate(floors):
            total_space = floor[0]*floor[1]
            min_space = sum(a*b for a,b in zip(avails[i], c_tiles))
            if min_space < total_space:
                total += 1
        return total

    def part_two(self, input: str) -> int:
        pass

class AocSolutionTest(unittest.TestCase):
    def setUp(self):
        self.test_part_one = """
0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
        """
        self.solution_part_one = 2

        self.test_part_two = """
        """
        self.solution_part_two = 0

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
