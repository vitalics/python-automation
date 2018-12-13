from selenium import webdriver

from behave.runner import Context


def before_feature(context: Context, feature):
    context.browser = webdriver.Chrome()


def after_feature(context: Context, feature):
    context.browser.quit()
