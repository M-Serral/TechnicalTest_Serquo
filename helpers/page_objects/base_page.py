from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_to_be_clickable(self, by_locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(by_locator)
            )
            return element
        except TimeoutException:
            print(f"Elemento {by_locator} no es clickeable en {timeout} segundos.")
            return None

    def click_element(self, by_locator, timeout=10):
        self.wait_for_element_to_be_clickable(by_locator, timeout)
        self.driver.find_element(*by_locator).click()

    def enter_text(self, by_locator, text, timeout=10):
        self.wait_for_element_to_be_clickable(by_locator, timeout)
        self.driver.find_element(*by_locator).send_keys(text)