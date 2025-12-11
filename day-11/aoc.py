import timeit
import unittest
from collections import defaultdict

class AocSolver():
    tree = defaultdict(list)

    def setup(self, input_file_path = 'input.txt') -> str:
        return open("input.txt", "r").read()

    def bfs(self, curr, end, dp):
        if curr in dp.keys():
            return dp[curr], dp
        if curr == end:
            return 1, dp
        sum = 0
        for n in self.tree[curr]:
            s, dp = self.bfs(n, end, dp)
            sum += s
        dp[curr] = sum
        return sum, dp

    def part_one(self, input: str) -> int:
        for line in input.strip().splitlines():
            key, values = line.split(':')
            self.tree[key.strip()] = values.strip().split(' ')

        v, _ =  self.bfs('you', 'out', {})
        return v

    def part_two(self, input: str) -> int:
        for line in input.strip().splitlines():
            key, values = line.split(':')
            self.tree[key.strip()] = values.strip().split(' ')

        svr_dac,dp = self.bfs('svr', 'dac', {})
        fft_dac,_ = self.bfs('fft', 'dac', dp)
        svr_fft,_ = self.bfs('svr', 'fft', {})
        dac_fft,dp = self.bfs('dac', 'fft', dp)
        dac_out,_ = self.bfs('dac', 'out', {})
        fft_out,dp = self.bfs('fft', 'out', dp)

        return svr_dac*dac_fft*fft_out + svr_fft*fft_dac*dac_out

class AocSolutionTest(unittest.TestCase):
    def setUp(self):
        self.test_part_one = """
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
        """
        self.solution_part_one = 5

        self.test_part_two = """
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
        """
        self.solution_part_two = 2

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
