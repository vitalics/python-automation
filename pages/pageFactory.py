from .google import Google


class PageFactory(object):
    @staticmethod
    def getPage(pageName: str) -> Google:
        return {
            pageName == 'Google': Google()
        }[True]
