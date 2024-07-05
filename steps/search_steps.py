from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from data.config import Config
from helpers.page_objects.home_page import HomePage
from helpers.page_objects.product_page import ProductPage
from helpers.page_objects.cart_page import CartPage
from helpers.page_objects.login_page import LogInPage
from helpers.page_objects.signup_page import SignUpPage
from helpers.page_objects.cart_page import CartPage


@given('the user is on the home page')
def step_given_user_on_home_page(context):
    service = ChromeService(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    context.driver = webdriver.Chrome(service=service, options=options)
    context.home_page = HomePage(context.driver)


@given('the user is logged in')
def step_given_user_logged_in(context):
    step_given_user_on_home_page(context)

    if not Config.USER_CREATED:
        context.signup_page = SignUpPage(context.driver)
        context.home_page.click_sign_up_button()
        context.signup_page.sign_up_user(Config.USERNAME, Config.PASSWORD)
        Config.USER_CREATED = True

    context.login_page = LogInPage(context.driver)
    context.home_page.click_log_in_button()
    context.login_page.log_in_user(Config.USERNAME, Config.PASSWORD)


@when('the user searches for a Samsung galaxy s6"')
def step_when_user_searches_product(context):
    context.home_page.click_product()


@when('the user adds the product to the cart')
def step_when_user_adds_product_to_cart(context):
    context.product_page = ProductPage(context.driver)
    context.product_page.add_to_cart()


@when('the user navigate to Cart tab')
def step_when_user_proceeds_to_checkout(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_cart_button()


@then('the user should see "{product_name}" in the purchase summary')
def step_then_user_sees_purchase_summary(context, product_name):
    context.cart_page = CartPage(context.driver)
    context.cart_page.checkproduct(product_name)
    context.driver.quit()



