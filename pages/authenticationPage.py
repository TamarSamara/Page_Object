from selenium.webdriver.common.by import By
from pages.basePage import BasePage


class AuthenticationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    locators = {
      "EMAIL": (By.ID, "email"),
      "PASSWORD": (By.ID, "passwd"),
      "LOGIN_BUTTON": (By.ID, "SubmitLogin"),
      "FORGOT_YOUR_PASSWORD_LINK": (By.LINK_TEXT, "Forgot your password?")
    }

    def send_email(self, email):
        self._driver.find_element(*self.locators["EMAIL"]).send_keys(email)

    def send_password(self, password):
        self._driver.find_element(*self.locators["PASSWORD"]).send_keys(password)

    def click_signin(self):
        self._driver.find_element(*self.locators["LOGIN_BUTTON"]).click()

    def click_forgot_password(self):
        self._driver.find_element(*self.locators["FORGOT_YOUR_PASSWORD_LINK"]).click()

