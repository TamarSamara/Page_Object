from playwright.sync_api import Page


class BasePage(object):
    def __init__(self, page: Page):
        self._page = page

    @property
    def driver(self):
        """
        the driver
        """
        return self._page

    def title_text(self):
        """
        title text
        """
        return self._page.title

    def text_in_body(self, text):
        """
        title text
        """
        body_text = self._page.fill("body").inner_html()
        return text in body_text

    def url(self):
        """
        the url of the page
        """
        return self._page.url

    def close_page(self):
        """
        close the page
        """
        self._page.close()

    def page_back(self):
        """
        back one page
        """
        self._page.go_back()
