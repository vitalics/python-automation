from selenium import webdriver


def before_feature(context, feature):
    browser = webdriver.Chrome(
        executable_path='./vendors/chromedriver.exe')
    context.browser = browser


def after_feature(context, feature):
    context.browser.quit()
