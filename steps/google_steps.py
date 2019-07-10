from pages import Page, PageFactory, Google
from models import Search

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


@given('User visit "{pageName}" page')
def step_impl1(context, pageName: str):
    currentPage = PageFactory.getPage(pageName)

    context.currentPage = currentPage
    browser: webdriver.Chrome = context.browser

    browser.get(currentPage.url)


@when('User type "{text}" on search')
def step_impl2(context, text: str):
    browser: webdriver.Chrome = context.browser
    currentPage: Google = context.currentPage

    search_box = browser.find_elements_by_css_selector(
        currentPage.search_box_locator
    )[0]

    ActionChains(driver=context.browser).send_keys_to_element(
        search_box, text
    ).key_down(Keys.ENTER, element=search_box).perform()


@then('Result must be shown')
def step_impl3(context):
    time.sleep(10)
