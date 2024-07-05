from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from helpers.page_objects.home_page import HomePage
from helpers.page_objects.product_page import ProductPage
from helpers.page_objects.cart_page import CartPage


@given("the user sign up")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given the user sign up')