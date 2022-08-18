from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self._driver = driver

    @property
    def driver(self):
        """
        the driver
        """
        return self._driver

    def title_text(self):
        """
        title text
        """
        return self._driver.title

    def text_in_body(self, text):
        """
        title text
        """
        body_text = self._driver.find_element(By.TAG_NAME, "body").text
        return text in body_text

    def url(self):
        """
        the url of the page
        """
        return self._driver.current_url

    def close_page(self):
        """
        close the page
        """
        self._driver.close()

    def page_back(self):
        """
        back one page
        """
        self._driver.back()
