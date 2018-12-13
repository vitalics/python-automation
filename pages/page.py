class Page(object):
    def __init__(self, url):
        global Page
        self.url = url
        self.name = 'page'

    def getName(self):
        return self.name
