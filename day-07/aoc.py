import timeit
import unittest
from collections import defaultdict

class AocSolver():
    SPLITTER = '^'
    EMPTY = '.'
    START = 'S'

    def setup(self, input_file_path = 'input.txt') -> str:
        return open("input.txt", "r").read()

    def find_first_occurance(self, grid, value):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == value:
                    return i,j

    def build_tree(self, pos, last_splitter, grid, tree, seen):
        if pos[0] not in range(len(grid)) or pos[1] not in range(len(grid[0])):
            tree[last_splitter].append(-1)
            return tree, seen
        if grid[pos[0]][pos[1]] != self.SPLITTER:
            return self.build_tree((pos[0]+1,pos[1]), last_splitter, grid, tree, seen)
        if pos in seen and pos not in tree[last_splitter]:
            tree[last_splitter].append(pos)
            return tree, seen
        if last_splitter:
            tree[last_splitter].append(pos)
        tree,seen = self.build_tree((pos[0]+1, pos[1]-1), pos, grid, tree, seen)
        tree,seen = self.build_tree((pos[0]+1, pos[1]+1), pos, grid, tree, seen)
        seen.add(pos)
        return tree, seen

    def count_paths(self, node, tree, dp):
        if node in dp.keys():
            return dp[node], dp
        if node == -1:
            dp[node] = 1
            return 1, dp
        s = 0
        for child in tree[node]:
            s2, dp = self.count_paths(child, tree, dp)
            s += s2
        dp[node] = s
        return s, dp

    def part_one(self, input: str) -> int:
        grid = [list(line) for line in input.split()]

        #find_start
        start = self.find_first_occurance(grid, self.START)
        active_beams = set([start])
        splitter_activated = set()

        while active_beams:
            for x,y in list(active_beams):
                if y not in range(len(grid[0])):
                    active_beams.remove((x,y))
                    continue
                i = x+1
                while i in range(len(grid)) and grid[i][y] == self.EMPTY:
                    i += 1
                active_beams.remove((x,y))
                if i in range(len(grid)) and grid[i][y] == self.SPLITTER:
                    splitter_activated.add((i,y))
                    active_beams.add((i,y-1))
                    active_beams.add((i,y+1))
        return len(splitter_activated)

    def part_two(self, input: str) -> int:
        grid = [list(line) for line in input.split()]

        #find_start
        start = self.find_first_occurance(grid, self.START)
        root = self.find_first_occurance(grid, self.SPLITTER)


        #build tree
        tree, _ = self.build_tree(start, None, grid, defaultdict(list), set())

        res, _ = self.count_paths(root, tree, {})
        return res

class AocSolutionTest(unittest.TestCase):
    def setUp(self):
        self.test_part_one = """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
        """
        self.solution_part_one = 21

        self.test_part_two = """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
        """
        self.solution_part_two = 40

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
