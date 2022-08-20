from playwright.async_api import Page
from playwright_pages.basePage import BasePage
from playwright_pages.buyDressPage import BuyDressPage


class AuthenticationPage(BasePage):
    locators = {
        "EMAIL": "input#email",
        "PASSWORD": "input#passwd",
        "LOGIN_BUTTON": "#SubmitLogin",
        "FORGOT_YOUR_PASSWORD_LINK": 'text=Forgot your password?'
    }

    def __init__(self, page : Page):
        super().__init__(page)

    def send_email(self, email):
        self._page.locator(self.locators["EMAIL"]).fill(email)

    def send_password(self, password):
        self._page.locator(self.locators["PASSWORD"]).fill(password)

    def click_signin(self):
        self._page.locator(self.locators["LOGIN_BUTTON"]).click()
        return BuyDressPage(self._page)

    def click_forgot_password(self):
        self._page.locator(self.locators["FORGOT_YOUR_PASSWORD_LINK"]).click()

