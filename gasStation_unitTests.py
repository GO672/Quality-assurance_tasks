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
        gas = [1,2,3,4,5]
        cost = [3,4,5,1,2]
        expected = 3
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_case_2(self):
        gas = [2,3,4]
        cost = [3,4,3]
        expected = -1
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_case_3(self):
        gas = [5,1,2,3,4]
        cost = [4,4,1,5,1]
        expected = 4
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_case_4(self):
        gas = [1,2,3,4,5]
        cost = [1,2,3,4,5]
        expected = 0
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_case_5(self):
        gas = [2,3,4,3]
        cost = [3,4,3,2]
        expected = 2
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_case_6(self):
        gas = [5]
        cost = [4]
        expected = 0
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_case_7(self):
        gas = [5,1]
        cost = [4,2]
        expected = 0
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_case_8(self):
        gas = [1,2,3,4,5]
        cost = [5,4,3,2,1]
        expected = 2
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_case_9(self):
        gas = [2,4,6,8,10]
        cost = [1,3,5,7,9]
        expected = 0
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_case_10(self):
        gas = [5,8,3,4,9]
        cost = [2,6,7,2,3]
        expected = 0
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_case_11(self):
        gas = [10,20,30,40,50]
        cost = [5,4,3,2,1]
        expected = 0
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_case_12(self):
        gas = [1,0,0,0,0]
        cost = [1,0,0,0,0]
        expected = 0
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_case_13(self):
        gas = [2,3,4,5,1]
        cost = [1,2,3,4,5]
        expected = 0
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_case_14(self):
        gas = [5,10,15,20,25]
        cost = [5,10,15,20,25]
        expected = 0
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_case_15(self):
        gas = [1000,1000,1000,1000,1000]
        cost = [20000,20000,20000,20000,20000]
        expected = -1
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_case_16(self):
        gas = [3,4,5,6,7]
        cost = [4,5,6,7,8]
        expected = -1
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_case_17(self):
        gas = [10,15,20,25,30]
        cost = [15,20,25,30,35]
        expected = -1
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_case_18(self):
        gas = [5,4,3,2,1]
        cost = [1,2,3,4,5]
        expected = 0
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_case_19(self):
        gas = [1000,500,200,100,50]
        cost = [300,200,100,80,70]
        expected = 0
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_case_20(self):
        gas = [10,20,30,40,50,60]
        cost = [15,25,35,45,55,65]
        expected = -1
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_case_21(self):
        gas = [5,-10,15,-20,25]
        cost = [5,10,15,20,25]
        expected = -1
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

    def test_case_22(self):
        gas = [-10,-20,-30,-40,-50]
        cost = [-5,-10,-15,-20,-25]
        expected = -1
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), expected)

if __name__ == '__main__':
    unittest.main()
