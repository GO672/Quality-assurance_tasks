from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

test_cases = [
    {
        'comment': "Standard case with positive numbers.",
        'gas': [1, 2, 3, 4, 5],
        'cost': [3, 4, 5, 1, 2],
        'expected': 3
    },
    {
        'comment': "Impossible to complete the circuit.",
        'gas': [2, 3, 4],
        'cost': [3, 4, 3],
        'expected': -1
    },
    {
        'comment': "Last index should be the starting point.",
        'gas': [5, 1, 2, 3, 4],
        'cost': [4, 4, 1, 5, 1],
        'expected': 4
    },
    {
        'comment': "All numbers are equal, any index is a valid starting point.",
        'gas': [1, 2, 3, 4, 5],
        'cost': [1, 2, 3, 4, 5],
        'expected': 0
    },
    {
        'comment': "Positive numbers, different from test_case_1.",
        'gas': [2, 3, 4, 3],
        'cost': [3, 4, 3, 2],
        'expected': 2
    },
    {
        'comment': "Single-element arrays.",
        'gas': [5],
        'cost': [4],
        'expected': 0
    },
    {
        'comment': "Single element with enough gas.",
        'gas': [5, 1],
        'cost': [4, 2],
        'expected': 0
    },
    {
        'comment': "Large cost values, ensuring the last index works.",
        'gas': [1, 2, 3, 4, 5],
        'cost': [5, 4, 3, 2, 1],
        'expected': 2
    },
    {
        'comment': "Large gas values.",
        'gas': [2, 4, 6, 8, 10],
        'cost': [1, 3, 5, 7, 9],
        'expected': 0
    },
    {
        'comment': "Impossible to complete with high cost.",
        'gas': [5, 8, 3, 4, 9],
        'cost': [2, 6, 7, 2, 3],
        'expected': -1
    },
    {
        'comment': "More gas at the end.",
        'gas': [4, 3, 2, 1, 7],
        'cost': [5, 4, 3, 2, 1],
        'expected': 4
    },
    {
        'comment': "Even distribution.",
        'gas': [6, 6, 6],
        'cost': [6, 6, 6],
        'expected': 0
    },
    {
        'comment': "Gas is higher.",
        'gas': [7, 1, 0, 11, 1],
        'cost': [5, 1, 5, 1, 1],
        'expected': 3
    },
    {
        'comment': "Decreasing gas values.",
        'gas': [5, 4, 3, 2, 1],
        'cost': [1, 2, 3, 4, 5],
        'expected': 0
    },
    {
        'comment': "Cycle is not possible.",
        'gas': [3, 1, 2],
        'cost': [4, 2, 1],
        'expected': -1
    },
    {
        'comment': "Minimum at the end.",
        'gas': [1, 1, 1, 10],
        'cost': [2, 2, 2, 1],
        'expected': 3
    },
    {
        'comment': "Exact match.",
        'gas': [2, 2, 2, 2],
        'cost': [2, 2, 2, 2],
        'expected': 0
    },
    {
        'comment': "Multiple minimums.",
        'gas': [1, 2, 1, 2, 1],
        'cost': [1, 1, 1, 1, 1],
        'expected': 0
    },
    {
        'comment': "Circuit not possible.",
        'gas': [1, 2, 3],
        'cost': [3, 3, 3],
        'expected': -1
    },
    {
        'comment': "Negative values.",
        'gas': [3, 3, 3],
        'cost': [1, 2, 1],
        'expected': 0
    },
    {
        'comment': "Large test case.",
        'gas': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'cost': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        'expected': 5
    },
    {
        'comment': "Another large test case.",
        'gas': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        'cost': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'expected': -1
    }
]

class Solution:
    def canCompleteCircuit(self, gas, cost):
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

solution = Solution()

def update_test_case():
    random.shuffle(test_cases)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        gas = list(map(int, request.form.getlist('gas[]')))
        cost = list(map(int, request.form.getlist('cost[]')))
        expected = int(request.form['expected'])
        test_case = {'comment': "Custom Test Case", 'gas': gas, 'cost': cost, 'expected': expected}
        return render_template('index.html', test_case=test_case)

    update_test_case()
    return render_template('index.html', test_case=test_cases[0])

@app.route('/submit', methods=['POST'])
def submit():
    gas = list(map(int, request.form.getlist('gas[]')))
    cost = list(map(int, request.form.getlist('cost[]')))
    result = solution.canCompleteCircuit(gas, cost)
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
