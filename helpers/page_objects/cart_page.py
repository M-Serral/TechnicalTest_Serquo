from selenium.webdriver.common.by import By
from helpers.page_objects.base_page import BasePage


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.page_objects.base_page import BasePage


class CartPage(BasePage):
    SECOND_COLUMN_TEXT = (By.XPATH, "//tbody[@id='tbodyid']/tr[@class='success']/td[2]")

    def checkproduct(self, product_name):

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SECOND_COLUMN_TEXT)
        )


        element = self.driver.find_element(*self.SECOND_COLUMN_TEXT)
        actual_text = element.text.strip()


        assert actual_text == product_name, f"Expected product name '{product_name}', but got '{actual_text}'"
