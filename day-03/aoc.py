import timeit
import unittest

class AocSolver():

    def setup(self, input_file_path = 'input.txt') -> str:
        return open("input.txt", "r").read()

    def part_one(self, input: str) -> int:
        batteries =  [line.strip() for line in input.split()]

        total_jolts = 0

        for battery in batteries:
            curr_jolts = "0", "0"
            for i in range(len(battery)):
                if battery[i] > curr_jolts[0] and i+1 in range(len(battery)):
                    curr_jolts = battery[i], battery[i+1]
                elif battery[i] > curr_jolts[1]:
                    curr_jolts = curr_jolts[0], battery[i]

            total_jolts += int("".join(curr_jolts))

        return total_jolts

    def part_two(self, input: str) -> int:
        batteries =  [line.strip() for line in input.split()]

        total_jolts = 0

        for battery in batteries:
            curr_jolts = ["0"] * 12
            for i,s in enumerate(battery):
                for j,v in enumerate(curr_jolts):
                    if s > v and len(battery)-i-1 >= len(curr_jolts)-1-j:
                        curr_jolts[j] = s
                        for k in range(j+1, len(curr_jolts)):
                            curr_jolts[k] = "0"
                        break

            total_jolts += int("".join(curr_jolts))

        return total_jolts

class AocSolutionTest(unittest.TestCase):
    def setUp(self):
        self.test_part_one = """
987654321111111
811111111111119
234234234234278
818181911112111
        """
        self.solution_part_one = 357

        self.test_part_two = """
987654321111111
811111111111119
234234234234278
818181911112111
        """
        self.solution_part_two = 3121910778619

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
    iterations = 10
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
