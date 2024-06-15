import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class TestGasStationCircuit(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:5000")

    def tearDown(self):
        self.driver.quit()

    def test_select_test_case(self):
        driver = self.driver
        select = driver.find_element(By.ID, 'test-case-select')
        select.send_keys(Keys.DOWN)  # Select the first test case
        select.send_keys(Keys.ENTER)

        time.sleep(2)  # Wait for inputs to load

        gas_inputs = driver.find_element(By.ID, 'gas-inputs').find_elements(By.TAG_NAME, 'input')
        cost_inputs = driver.find_element(By.ID, 'cost-inputs').find_elements(By.TAG_NAME, 'input')
        comment_div = driver.find_element(By.ID, 'test-case-comment')

        self.assertEqual(len(gas_inputs), 5)
        self.assertEqual(len(cost_inputs), 5)
        self.assertIn("Standard case with positive numbers.", comment_div.text)

        submit_button = driver.find_element(By.XPATH, '//button[text()="Submit"]')
        submit_button.click()

        time.sleep(2)  # Wait for result
        result_div = driver.find_element(By.ID, 'result')
        self.assertIn("Result: 3", result_div.text)

    def test_custom_input(self):
        driver = self.driver

        gas_inputs = driver.find_element(By.ID, 'gas-inputs').find_elements(By.TAG_NAME, 'input')
        cost_inputs = driver.find_element(By.ID, 'cost-inputs').find_elements(By.TAG_NAME, 'input')

        gas_inputs[0].clear()
        gas_inputs[0].send_keys("1")
        cost_inputs[0].clear()
        cost_inputs[0].send_keys("5")

        add_button = driver.find_element(By.XPATH, '//button[text()="Add more"]')
        add_button.click()

        gas_inputs = driver.find_element(By.ID, 'gas-inputs').find_elements(By.TAG_NAME, 'input')
        cost_inputs = driver.find_element(By.ID, 'cost-inputs').find_elements(By.TAG_NAME, 'input')

        gas_inputs[1].send_keys("10")
        cost_inputs[1].send_keys("4")

        submit_button = driver.find_element(By.XPATH, '//button[text()="Submit"]')
        submit_button.click()

        time.sleep(2)  # Wait for result
        result_div = driver.find_element(By.ID, 'result')
        self.assertIn("Result: 1", result_div.text)

if __name__ == "__main__":
    unittest.main()
