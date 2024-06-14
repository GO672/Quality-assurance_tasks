import unittest
from typing import List
from unittest.mock import patch
import random

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = 0
        res = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                res = i + 1
        
        return res

def generate_random_test_case(size: int) -> (List[int], List[int], int):
    gas = [random.randint(1, 100) for _ in range(size)]
    cost = [random.randint(1, 100) for _ in range(size)]
    solution = Solution()
    expected = solution.canCompleteCircuit(gas, cost)
    return gas, cost, expected

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_random_case(self):
        gas, cost, expected = generate_random_test_case(10)
        with patch('builtins.sum', side_effect=sum) as mock_sum:
            self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

if __name__ == '__main__':
    unittest.main()
