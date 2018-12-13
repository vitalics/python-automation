from pages import Page, PageFactory, Google
from models import Search

from behave import given, then, when
from behave.runner import Context
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


@given('User visit "{pageName}" page')
def step_impl1(context: Context, pageName: str):
    context.currentPage = PageFactory.getPage(pageName)
    context.browser.get(context.currentPage.url)


@when('User type "{text}" on search')
def step_impl2(context: Context, text: str):
    search_box = context.browser.find_elements_by_css_selector(
        context.currentPage.search_box_locator
    )[0]

    ActionChains(driver=context.browser).send_keys_to_element(
        search_box, text
    ).key_down(Keys.ENTER).perform()


@then('Result must be shown')
def step_impl3(context: Context):
    time.sleep(10)
