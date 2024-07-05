from selenium.webdriver.common.by import By
from helpers.page_objects.base_page import BasePage
import time


class ProductPage(BasePage):
    ADD_TO_CART_BUTTON = (By.XPATH, '//a[contains(text(),"Add to cart")]')

    def add_to_cart(self):

        time.sleep(2)
        self.driver.find_element(*self.ADD_TO_CART_BUTTON).click()
        try:
            alert = self.driver.switch_to.alert
            alert.accept()  # Aceptar la alerta
        except Exception as e:
            print(f"No se encontró alerta o error al manejarla: {str(e)}")

