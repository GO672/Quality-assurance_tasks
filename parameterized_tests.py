import unittest
from typing import List
from unittest.mock import patch
import random

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if len(gas) != len(cost):
            return -1
        
        if sum(gas) < sum(cost):
            return -1

        total = 0
        res = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                res = i + 1
        
        return res if res < len(gas) else -1  # Ensure res is within bounds

def generate_random_test_case(size: int) -> (List[int], List[int], int):
    gas = [random.randint(1, 100) for _ in range(size)]
    cost = [random.randint(1, 100) for _ in range(size)]
    solution = Solution()
    expected = solution.canCompleteCircuit(gas, cost)
    return gas, cost, expected

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        # Any cleanup code goes here
        pass

    def test_parametrized_cases(self):
        test_cases = [
            ([1,2,3,4,5], [3,4,5,1,2], 3),
            ([2,3,4], [3,4,3], -1),
            ([5,1,2,3,4], [4,4,1,5,1], 4),
            ([1,2,3,4,5], [1,2,3,4,5], 0),
            ([2,3,4,3], [3,4,3,2], 2),
            ([5], [4], 0),
            ([5,1], [4,2], 0),
            ([1,2,3,4,5], [5,4,3,2,1], 2),
            ([2,4,6,8,10], [1,3,5,7,9], 0),
            ([5,8,3,4,9], [2,6,7,2,3], 0),
            ([10,20,30,40,50], [5,4,3,2,1], 0),
            ([1,0,0,0,0], [1,0,0,0,0], 0),
            ([2,3,4,5,1], [1,2,3,4,5], 0),
            ([5,10,15,20,25], [5,10,15,20,25], 0),
            ([1000,1000,1000,1000,1000], [20000,20000,20000,20000,20000], -1),
            ([3,4,5,6,7], [4,5,6,7,8], -1),
            ([10,15,20,25,30], [15,20,25,30,35], -1),
            ([5,4,3,2,1], [1,2,3,4,5], 0),
            ([1000,500,200,100,50], [300,200,100,80,70], 0),
            ([10,20,30,40,50,60], [15,25,35,45,55,65], -1),
            ([5,-10,15,-20,25], [5,10,15,20,25], -1),
            ([-10,-20,-30,-40,-50], [-5,-10,-15,-20,-25], -1),
        ]
        
        for gas, cost, expected in test_cases:
            with self.subTest(gas=gas, cost=cost):
                self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_random_cases(self):
        for _ in range(10):  # Run 10 random test cases
            gas, cost, expected = generate_random_test_case(random.randint(1, 20))
            with self.subTest(gas=gas, cost=cost):
                self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

if __name__ == '__main__':
    unittest.main()
