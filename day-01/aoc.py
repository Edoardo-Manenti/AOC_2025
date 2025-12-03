import timeit
import unittest

class AocSolver():

    def setup(self, input_file_path = 'input.txt') -> str:
        return open("input.txt", "r").read()

    def part_one(self, input: str) -> int:
        moves = input.split()
        curr_pos = 50
        pw = 0
        for move in moves:
            dir, steps = move[0], int(move[1:])

            if move[0] == 'R':
                curr_pos = (curr_pos + steps) % 100
            if move[0] == 'L':
                curr_pos = (curr_pos - steps) % 100

            if curr_pos == 0:
                pw += 1
        return pw

    def part_two(self, input: str) -> int:
        moves = input.split()
        curr_pos = 50
        pw = 0
        for move in moves:
            dir, steps = move[0], int(move[1:])

            if move[0] == 'R':
                if curr_pos + steps >= 100:
                    if curr_pos == 0:
                        pw += (steps) // 100
                    else:
                        pw += ((curr_pos + steps) // 100)
                    #print(move, pw)
                curr_pos = (curr_pos + steps) % 100
            if move[0] == 'L':
                if curr_pos - steps <= 0:
                    if curr_pos == 0:
                        pw += (steps) // 100
                    else:
                        pw += ((100 - curr_pos + steps) // 100) 
                    #print(move, pw)
                curr_pos = (curr_pos - steps) % 100

        return pw

    def part_two_revised(self, input: str) -> int:
        moves = input.split()
        curr_pos = 50
        pw = 0
        for move in moves:
            dir, steps = 1 if move[0] == 'R' else -1, int(move[1:])

            if dir < 0:
                steps_to_reach_zero = curr_pos or 100
            else:
                steps_to_reach_zero = 100 - curr_pos

            curr_pos = (curr_pos + dir*steps) % 100

            if steps >= steps_to_reach_zero:
                pw += (steps - steps_to_reach_zero) // 100 + 1

        return pw

class AocSolutionTest(unittest.TestCase):

    def setUp(self):
        from aoc import AocSolver
        self.test_part_one = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
        """
        self.solution_part_one = 3

        self.test_part_two = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
R200
        """
        self.solution_part_two = 8

        self.solver = AocSolver()

    def test_part_one(self):
        value = self.solver.part_one(self.test_part_one)

        self.assertIsNotNone(value)
        self.assertEqual(value, self.solution_part_one)

    def test_part_two(self):
        value = self.solver.part_two(self.test_part_two)

        self.assertIsNotNone(value)
        self.assertEqual(value, self.solution_part_two)

    def test_part_two_revised(self):
        value = self.solver.part_two_revised(self.test_part_two)

        self.assertIsNotNone(value)
        self.assertEqual(value, self.solution_part_two)

if __name__ == '__main__':
    setup = '''
from aoc import AocSolver
solver = AocSolver()
problem = solver.setup()
    '''
    print(f"Time for part1: {
    timeit.timeit(setup=setup, 
                  stmt='print(solver.part_one(problem))', 
                  number = 1)
    } sec")
    print(f"Time for part2: {
    timeit.timeit(setup=setup, 
                  stmt='print(solver.part_two(problem))', 
                  number = 1)
    } sec")
