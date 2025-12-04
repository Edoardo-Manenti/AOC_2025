import timeit
import unittest

class AocSolver():
    ROLL = '@'
    EMPTY = '.'
    dir = (-1,0,1)

    def setup(self, input_file_path = 'input.txt') -> str:
        return open("input.txt", "r").read()

    def part_one(self, input: str) -> int:
        rows = [list(row) for row in input.split()]

        result = 0

        for i,r in enumerate(rows):
            for j,c in enumerate(r):
                sum = 0
                if c == self.EMPTY:
                    continue

                sum = 0
                for dr in self.dir:
                    if i+dr not in range(len(rows)):
                        continue
                    for dc in self.dir:
                        if j+dc not in range(len(r)):
                            continue
                        if dr == 0 and dc == 0:
                            continue
                        if rows[i+dr][j+dc] == self.ROLL:
                            sum += 1
                
                if sum < 4:
                    result += 1

        return result

    def part_two(self, input: str) -> int:
        rows = [list(row) for row in input.split()]

        result_prev = -1
        result = 0

        # Break as soon as we do a complete scan without removing any ROLL
        while result_prev != result:
            result_prev = result
            for i,r in enumerate(rows):
                for j,c in enumerate(r):
                    sum = 0
                    if c == self.EMPTY:
                        continue

                    sum = 0
                    for dr in self.dir:
                        if i+dr not in range(len(rows)):
                            continue
                        for dc in self.dir:
                            if j+dc not in range(len(r)):
                                continue
                            if dr == 0 and dc == 0:
                                continue
                            if rows[i+dr][j+dc] == self.ROLL:
                                sum += 1

                    if sum < 4:
                        rows[i][j] = self.EMPTY
                        result += 1
        return result


class AocSolutionTest(unittest.TestCase):
    def setUp(self):
        self.test_part_one = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
        """
        self.solution_part_one = 13

        self.test_part_two = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
        """
        self.solution_part_two = 43

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
