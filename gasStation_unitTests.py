import unittest
from typing import List

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

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        # Standard case with positive numbers.
        gas = [1,2,3,4,5]
        cost = [3,4,5,1,2]
        expected = 3
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_case_2(self):
        # Impossible to complete the circuit.
        gas = [2,3,4]
        cost = [3,4,3]
        expected = -1
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_case_3(self):
        # Last index should be the starting point.
        gas = [5,1,2,3,4]
        cost = [4,4,1,5,1]
        expected = 4
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_case_4(self):
        # All numbers are equal, any index is a valid starting point.
        gas = [1,2,3,4,5]
        cost = [1,2,3,4,5]
        expected = 0
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_case_5(self):
        # Positive numbers, different from test_case_1.
        gas = [2,3,4,3]
        cost = [3,4,3,2]
        expected = 2
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_case_6(self):
        # Single-element arrays.
        gas = [5]
        cost = [4]
        expected = 0
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_case_7(self):
        # Single element with enough gas.
        gas = [5,1]
        cost = [4,2]
        expected = 0
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_case_8(self):
        # Large cost values, ensuring the last index works.
        gas = [1,2,3,4,5]
        cost = [5,4,3,2,1]
        expected = 2
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_case_9(self):
        # Large gas values.
        gas = [2,4,6,8,10]
        cost = [1,3,5,7,9]
        expected = 0
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_case_10(self):
        # Impossible to complete with high cost.
        gas = [5,8,3,4,9]
        cost = [2,6,7,2,3]
        expected = 0
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_case_11(self):
        # Large gas values with decreasing cost.
        gas = [10,20,30,40,50]
        cost = [5,4,3,2,1]
        expected = 0
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_case_12(self):
        # All elements are 1, all indices are valid starting points.
        gas = [1,0,0,0,0]
        cost = [1,0,0,0,0]
        expected = 0
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_case_13(self):
        # Gas array rotated, expecting the last index to work.
        gas = [2,3,4,5,1]
        cost = [1,2,3,4,5]
        expected = 0
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_case_14(self):
        # Gas and cost are identical, any index is valid.
        gas = [5,10,15,20,25]
        cost = [5,10,15,20,25]
        expected = 0
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_case_15(self):
        # Insufficient gas for any starting point.
        gas = [1000,1000,1000,1000,1000]
        cost = [20000,20000,20000,20000,20000]
        expected = -1
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_case_16(self):
        # Similar to test_case_1 but different values.
        gas = [3,4,5,6,7]
        cost = [4,5,6,7,8]
        expected = -1
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_case_17(self):
        # Large gas values with increasing cost.
        gas = [10,15,20,25,30]
        cost = [15,20,25,30,35]
        expected = -1
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_case_18(self):
        # Gas array rotated in opposite direction to test_case_13.
        gas = [5,4,3,2,1]
        cost = [1,2,3,4,5]
        expected = 0
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_case_19(self):
        # Large positive and negative numbers in gas and cost.
        gas = [1000,500,200,100,50]
        cost = [300,200,100,80,70]
        expected = 0
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_case_20(self):
        # Large arrays with increasing values.
        gas = [10,20,30,40,50,60]
        cost = [15,25,35,45,55,65]
        expected = -1
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_case_21(self):
        # Negative numbers in gas array, expecting the last index to work.
        gas = [5,-10,15,-20,25]
        cost = [5,10,15,20,25]
        expected = -1
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_case_22(self):
        # All negative numbers in gas and cost, impossible to complete the circuit.
        gas = [-10,-20,-30,-40,-50]
        cost = [-5,-10,-15,-20,-25]
        expected = -1
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

if __name__ == '__main__':
    unittest.main()
