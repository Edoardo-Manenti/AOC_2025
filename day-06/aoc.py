import timeit
import unittest
from functools import reduce

class AocSolver():

    def setup(self, input_file_path = 'input.txt') -> str:
        return open("input.txt", "r").read()

    def calculate_operations(self, numbers, operators):
        total = 0

        for col, operator in enumerate(operators):
            if operator == '+':
                total += sum(numbers[col])
            elif operator == '*':
                total += reduce(lambda x,y: x*y, numbers[col])

        return total

    def part_one(self, input: str) -> int:
        inputs = [line.strip().split() for line in input.strip().split("\n")]

        operators = inputs[-1]
        numbers = [
            [
                int(num[i]) 
                for num in inputs[:-1]
            ] 
            for i in range(len(operators))
        ]

        return self.calculate_operations(numbers, operators)

    def part_two(self, input: str) -> int:
        operators = input.strip().split('\n')[-1].split()

        inputs = input.strip().split("\n")[:-1]

        #scan vertically"
        numbers = []
        operation = []
        for j in range(len(inputs[0])):
            curr = ""
            for i in range(len(inputs)):
                curr += inputs[i][j]
            if len(curr.strip()) > 0:
                operation.append(int(curr))
            else:
                numbers.append(operation)
                operation = []
        numbers.append(operation)

        return self.calculate_operations(numbers, operators)

class AocSolutionTest(unittest.TestCase):
    def setUp(self):
        self.test_part_one = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""
        self.solution_part_one = 4277556

        self.test_part_two = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""

        self.solution_part_two = 3263827

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
