from .page import Page

from selenium.webdriver.common.by import By


class Google(Page):
    search_box_locator = "input[aria-label='Search']"

    def __init__(self):
        global Google
        self.url = 'https://google.com'
        self.name = 'google'
