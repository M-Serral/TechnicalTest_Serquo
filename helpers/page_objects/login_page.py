from selenium.webdriver.common.by import By

from helpers.page_objects import base_page
from helpers.page_objects.base_page import BasePage
import time

class LogInPage(BasePage):
    USERNAME_LOGIN_BUTTON = (By.ID, 'loginusername')
    PASSWORD_LOGIN_BUTTON = (By.ID, 'loginpassword')
    LOGIN_BUTTON = (By.XPATH, '//button[contains(.,"Log in")]')

    def log_in_user(self, USERNAME, PASSWORD):
        self.wait_for_element_to_be_clickable(self.USERNAME_LOGIN_BUTTON)
        self.driver.find_element(*self.USERNAME_LOGIN_BUTTON).send_keys(USERNAME)
        self.driver.find_element(*self.PASSWORD_LOGIN_BUTTON).send_keys(PASSWORD)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        time.sleep(2)

        try:
            alert = self.driver.switch_to.alert
            alert.accept()  # Aceptar la alerta
        except Exception as e:
            print(f"No se encontró alerta o error al manejarla: {str(e)}")