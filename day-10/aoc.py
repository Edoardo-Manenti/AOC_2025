import timeit
import unittest
import re
from z3 import Int, Optimize
from collections import defaultdict

class AocSolver():

    def setup(self, input_file_path = 'input.txt') -> str:
        return open("input.txt", "r").read()

    def toggle(self, state, button):
        new_state = []
        for s in state:
            new_state.append(s)
        for b in button:
            new_state[b] = (state[b]+1)%2
        return new_state

    def rec(self, state, obj, counter, b, buttons):
        if state == obj:
            return counter
        if b >= len(buttons):
            return float('inf')
        press = self.rec(self.toggle(state, buttons[b]), obj, counter+1, b+1, buttons)
        no_press = self.rec(state, obj, counter, b+1, buttons)
        return min(press, no_press)

    def part_one(self, input: str) -> int:
        machines = re.findall(r'\[(.*)\]\ (.*)\ \{(.*)\}\n', input)

        sum = 0
        for lights, buttons, _ in machines:
            buttons = [b[1:-1].split(',') for b in buttons.split(' ')]
            buttons = [list(map(int, b)) for b in buttons]

            obj = list(map(lambda s: 0 if s == '.' else 1, lights))

            sum += self.rec([0]*len(lights), obj, 0, 0, buttons)
        return sum

    def part_two(self, input: str) -> int:
        machines = re.findall(r'\[(.*)\]\ (.*)\ \{(.*)\}\n', input)

        total = 0
        for m in machines:
            _, buttons, obj = m
            buttons = [b[1:-1].split(',') for b in buttons.split(' ')]
            buttons = [map(int, b) for b in buttons]
            obj = [int(o) for o in obj.split(',')]

            # We to solve AX = B while minimizing sum(X)
            presses = Int('presses')
            X = [Int(f'A{i}') for i in range(len(buttons))]

            button_dict = defaultdict(list)
            for i,b in enumerate(buttons):
                for index in b:
                    button_dict[index].append(i)

            equations = []

            for index, button_press in button_dict.items():
                equations.append(obj[index] == sum([X[i] for i in button_press]))

            for x in X:
                equations.append(x >= 0)

            equations.append(presses == sum(X))

            optimizer = Optimize()
            optimizer.add(equations)
            optimizer.minimize(presses)
            optimizer.check()

            total += int(str(optimizer.model()[presses]))
        return total


class AocSolutionTest(unittest.TestCase):
    def setUp(self):
        self.test_part_one = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
        """
        self.solution_part_one = 7

        self.test_part_two = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
        """
        self.solution_part_two = 33

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
