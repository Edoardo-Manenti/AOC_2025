import timeit
import unittest
from collections import defaultdict

class AocSolver():

    def setup(self, input_file_path = 'input.txt') -> str:
        return open("input.txt", "r").read()

    def part_one(self, input: str) -> int:
        tiles = [list(map(int, line.split(','))) for line in input.split()]
        N = len(tiles)

        largest = -1
        for i in range(N):
            for j in range(i+1, N):
                x1,y1 = tiles[i]
                x2,y2 = tiles[j]
                largest = max(largest, (abs(x1-x2)+1)*(abs(y1-y2)+1))
        return largest

    def part_two(self, input: str) -> int:
        tiles = [list(map(int, line.split(','))) for line in input.split()]
        N = len(tiles)
        r = max(tile[0] for tile in tiles)
        vedge = defaultdict(list)
        hedge = defaultdict(list)
        dp = {}
        pq = []

        for i in range(N):
            for j in range(i+1, N):
                x1,y1 = tiles[i]
                x2,y2 = tiles[j]
                pq.append(((abs(x1-x2)+1)*(abs(y1-y2)+1), i, j))
        pq.sort(key=lambda item: item[0])

        def make_edge(p,q):
            x1,y1 = p
            x2,y2 = q
            if x1 == x2:
                hedge[x1].append((min(y1,y2), max(y1,y2)))
            elif y1 == y2:
                vedge[y1].append((min(x1,x2), max(x1,x2)))

        #mark coloured tiles
        for i in range(1,N):
            make_edge(tiles[i], tiles[i-1])
        make_edge(tiles[0], tiles[-1])

        def is_green(x,y):
            counter = 0
            for i in range(x,r+1):
                for y1,y2 in hedge[i]:
                    if y1<=y<=y2:
                        counter += 1
            return counter%2 == 1

        def is_valid(i,j):
            x1,y1 = tiles[i]
            x2,y2 = tiles[j]
            xm = min(x1,x2)
            ym = min(y1,y2)
            xM = max(x1,x2)
            yM = max(y1,y2)
            if not is_green(xm+1, ym+1):
                return False
            for yl,yh in vedge[xm+1]:
                if yl<ym+1<yh or yl<yM-1<yh:
                    return False
            for yl,yh in vedge[xM-1]:
                if yl<=ym+1<=yh or yl<yM-1<yh:
                    return False
            for xl,xh in hedge[ym+1]:
                if xl<xm+1<xh or xl<xM-1<xh:
                    return False
            for yl,yh in hedge[yM-1]:
                if xl<xm+1<xh or xl<xM-1<xh:
                    return False
            return True

        print(len(vedge))
        print(len(hedge))
        print(vedge)
        print(hedge)
        print(len(pq))

        while pq:
            a,i,j = pq.pop()
            if is_valid(i,j):
                print(i,j)
                return a
        return -1

class AocSolutionTest(unittest.TestCase):
    def setUp(self):
        self.test_part_one = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
        """
        self.solution_part_one = 50

        self.test_part_two = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
        """
        self.solution_part_two = 24

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
