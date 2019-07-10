from .google import Google
from .page import Page


class PageFactory(object):
    currentPage = Page(url='')
    @staticmethod
    def getPage(pageName: str) -> Google:
        # enum workaround
        currentPage = {
            pageName == 'Google': Google()
        }[True]

        return currentPage
