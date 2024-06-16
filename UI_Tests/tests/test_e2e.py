import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

class TestGasStationCircuit(unittest.TestCase):

    def setUp(self):
        # Path to ChromeDriver and Brave Browser executable
        chromedriver_path = 'C:\\Users\\kira_\\OneDrive\\Escritorio\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe'
        brave_path = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'

        # Configure Selenium WebDriver
        options = Options()
        options.binary_location = brave_path
        self.driver = webdriver.Chrome(service=Service(chromedriver_path), options=options)

    def tearDown(self):
        # Cleanup after each test
        self.driver.quit()

    def test_gas_station_circuit(self):
        # Open the web application
        self.driver.get('http://localhost:5000')  # Replace with your app's URL if hosted elsewhere

        # Wait for the page to load
        time.sleep(2)

        # Retrieve test cases from the server (assuming they are dynamically loaded)
        test_cases = self.driver.execute_script("return JSON.parse(document.querySelector('#test-cases').innerText)")

        # Iterate over each test case
        for index, test_case in enumerate(test_cases):
            # Populate gas inputs
            gas_inputs = self.driver.find_elements_by_name('gas[]')
            for i, gas in enumerate(test_case['gas']):
                gas_inputs[i].clear()
                gas_inputs[i].send_keys(str(gas))

            # Populate cost inputs
            cost_inputs = self.driver.find_elements_by_name('cost[]')
            for i, cost in enumerate(test_case['cost']):
                cost_inputs[i].clear()
                cost_inputs[i].send_keys(str(cost))

            # Populate expected result input
            expected_input = self.driver.find_element_by_name('expected')
            expected_input.clear()
            expected_input.send_keys(str(test_case['expected']))

            # Submit the form
            submit_button = self.driver.find_element_by_xpath("//input[@type='submit']")
            submit_button.click()

            # Wait for the result
            time.sleep(1)

            # Verify the result displayed matches the expected result
            result_element = self.driver.find_element_by_id('result')
            result_text = result_element.text.split(':')[1].strip()
            expected_result = str(test_case['expected'])
            self.assertEqual(result_text, expected_result, f"Test case {index + 1} failed: Expected {expected_result}, got {result_text}")

            # Go back to the main page for the next test case (if not the last one)
            if index < len(test_cases) - 1:
                self.driver.get('http://localhost:5000')  # Replace with your app's URL if hosted elsewhere
                time.sleep(2)

if __name__ == '__main__':
    unittest.main()
