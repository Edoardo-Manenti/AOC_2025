import timeit
import unittest

class AocSolver():

    def setup(self, input_file_path = 'input.txt') -> str:
        return open("input.txt", "r").read()

    def part_one(self, input: str) -> int:
        ranges = [[int(a) for a in range.split('-')] for range in input.split(',')]
        sum = 0
        curr_base = 1
        curr_invalid = int(2*str(curr_base))
        upper_limit = ranges[-1][-1]
        
        while curr_invalid < upper_limit:
            for a,b in ranges:
                if curr_invalid < a or curr_invalid > b:
                    continue
                else:
                    sum += curr_invalid
            curr_base += 1
            curr_invalid = int(2*str(curr_base))

        return sum
    
    def part_one_revised(self, input: str) -> int:
        ranges = [[int(a) for a in range.split('-')] for range in input.split(',')]
        sum = 0

        for a,b in ranges:
            for i in range(a,b+1):
                s = str(i)
                if len(s)%2==0 and s[:len(s)//2] == s[len(s)//2:]:
                    sum += i
        return sum

    def part_two_revised(self, input: str) -> int:
        ranges = [[int(a) for a in range.split('-')] for range in input.split(',')]
        sum = 0

        for a,b in ranges:
            for i in range(a,b+1):
                s = str(i)
                for sz in range(1,len(s)//2+1):
                    if len(s)%sz==0 and s == s[:sz]*(len(s)//sz):
                        sum += i
                        break
        return sum
    
    def generate_next_invalid(self, old_base, old_invalid, upper_limit) -> (int, int):
        new_invalid = int(str(old_invalid) + str(old_base))
        if new_invalid < upper_limit:
            return old_base, new_invalid
        new_base = old_base+1
        new_invalid = int(2*str(new_base))
        return new_base, new_invalid

    def part_two(self, input: str) -> int:
        ranges = [[int(a) for a in range.split('-')] for range in input.split(',')]
        invalid_found = set()
        curr_base = 1
        curr_invalid = int(2*str(curr_base))
        upper_limit = ranges[-1][-1]
        
        while curr_invalid < upper_limit:
            for a,b in ranges:
                if curr_invalid < a or curr_invalid > b:
                    continue
                else:
                    invalid_found.add(curr_invalid)
            curr_base, curr_invalid = self.generate_next_invalid(curr_base, curr_invalid, upper_limit)

        return sum(invalid_found)

class AocSolutionTest(unittest.TestCase):
    def setUp(self):
        self.test_part_one = """
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124
        """
        self.solution_part_one = 1227775554

        self.test_part_two = """
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124
        """
        self.solution_part_two = 4174379265

        self.solver = AocSolver()

    def test_part_one(self):
        value = self.solver.part_one(self.test_part_one)

        self.assertIsNotNone(value)
        self.assertEqual(value, self.solution_part_one)

    def test_part_one_revised(self):
        value = self.solver.part_one_revised(self.test_part_one)

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
                  number = 100)
    } sec")
    print(f"Time for part1_revised: {
    timeit.timeit(setup=setup, 
                  stmt='print(solver.part_one_revised(problem))', 
                  number = 100)
    } sec")
    print(f"Time for part2: {
    timeit.timeit(setup=setup, 
                  stmt='print(solver.part_two(problem))', 
                  number = 100)
    } sec")
    print(f"Time for part2_revised: {
    timeit.timeit(setup=setup, 
                  stmt='print(solver.part_two_revised(problem))', 
                  number = 100)
    } sec")
