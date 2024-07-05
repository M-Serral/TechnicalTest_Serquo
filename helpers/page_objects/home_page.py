from selenium.webdriver.common.by import By

from helpers.page_objects import base_page
from helpers.page_objects.base_page import BasePage


class HomePage(BasePage):
    SIGNIN_BUTTON = (By.ID, 'signin2')
    LOGIN_BUTTON = (By.ID, 'login2')
    FIRSTMOBILE_BUTTON = (By.LINK_TEXT, 'Samsung galaxy s6')
    CART_BUTTON = (By.ID, 'cartur')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://www.demoblaze.com/')

    def click_sign_up_button(self):
        self.click_element(self.SIGNIN_BUTTON)

    def click_log_in_button(self):
        self.click_element(self.LOGIN_BUTTON)

    def click_product(self):
        self.click_element(self.FIRSTMOBILE_BUTTON)

    def click_cart_button(self):
        self.click_element(self.CART_BUTTON)