from telnetlib import EC
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from helpers.page_objects import base_page
from helpers.page_objects.base_page import BasePage


class SignUpPage(BasePage):
    USERNAME_SIGNUP_BUTTON = (By.ID, 'sign-username')
    PASSWORD_SIGNUP_BUTTON = (By.ID, 'sign-password')
    SIGNUP_BUTTON = (By.XPATH, '//button[contains(.,"Sign up")]')

    def sign_up_user(self, USERNAME, PASSWORD):
        self.wait_for_element_to_be_clickable(self.PASSWORD_SIGNUP_BUTTON)
        self.driver.find_element(*self.USERNAME_SIGNUP_BUTTON).send_keys(USERNAME)
        self.driver.find_element(*self.PASSWORD_SIGNUP_BUTTON).send_keys(PASSWORD)
        self.driver.find_element(*self.SIGNUP_BUTTON).click()
        time.sleep(2)

        try:
            alert = self.driver.switch_to.alert
            alert.accept()  # Aceptar la alerta
        except Exception as e:
            print(f"No se encontró alerta o error al manejarla: {str(e)}")
