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

    def test_ten_test_cases(self):
        driver = self.driver
        test_case_forms = driver.find_elements(By.CSS_SELECTOR, 'form')
        for form in test_case_forms[:10]:  # Test the first 10 test cases
            gas_inputs = form.find_elements(By.CSS_SELECTOR, 'input[name="gas"]')
            cost_inputs = form.find_elements(By.CSS_SELECTOR, 'input[name="cost"]')
            expected_result = form.find_element(By.CSS_SELECTOR, 'input[name="expected"]').get_attribute('value')

            gas_values = [int(input_field.get_attribute('value')) for input_field in gas_inputs]
            cost_values = [int(input_field.get_attribute('value')) for input_field in cost_inputs]

            submit_button = form.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
            submit_button.click()

            time.sleep(2)  # Wait for result
            result_div = form.find_element(By.XPATH, './div')
            self.assertIn(f"Result: {expected_result}", result_div.text)

if __name__ == "__main__":
    unittest.main()
