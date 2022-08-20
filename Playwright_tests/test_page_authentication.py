import pytest
from playwright.sync_api import sync_playwright
from playwright_pages.buyDressPage import BuyDressPage
from playwright_pages.authenticationPage import AuthenticationPage
import logging
import time


@pytest.fixture
def account():
    return {
        "email": "tamar.samara@gmail.com",
        "password": "12345"
    }


def Start_BuyDress_Page(playwright):
    """
    start BuyDress page
    """
    chromium = playwright.chromium.launch(headless=False)
    newContext = chromium.new_context()
    page = newContext.new_page()
    page.goto("http://automationpractice.com/index.php")
    return BuyDressPage(page)


def check_account(email, password):
    with sync_playwright() as playwright:
        dress_page = Start_BuyDress_Page()
        # time.sleep(3)
        auth_page = AuthenticationPage(dress_page.click_sign_in())
        # time.sleep(3)
        auth_page.send_email(email)
        # time.sleep(3)
        auth_page.send_password(password)
        # time.sleep(3)
        auth_page.click_signin()
        time.sleep(3)
        text = auth_page.title_text()
        auth_page.close_page()
        return text == "My account - My Store"


@pytest.mark.passed
def test_Forgot_your_password_exists():
    """
    Check if forgot your title exists
    passed
    """
    dress_page = Start_BuyDress_Page()
    auth_page = AuthenticationPage(dress_page.click_sign_in())
    logging.info("Successful 'Login - My Store' is in the body")
    logging.warning('Error, "Login - My Store" Does not exist in the body')
    assert auth_page.title_text() == "Login - My Store"
    auth_page.close_page()


@pytest.mark.passed
def test_valid_email_valid_password(account):
    """
    Check valid email and valid password
    passed
    """
    logging.info("Successful Login")
    logging.warning("Error")
    assert check_account(account["email"], account["password"])


@pytest.mark.failed
def test_wrong_email_wrong_password():
    """
    Check wrong email and wrong password
    Error message: "Authentication failed."
    failed
    """
    logging.info("Successful Login")
    logging.warning("Error message: Authentication failed.")
    assert check_account("tamarsamara", "tttttt")


@pytest.mark.failed
def test_valid_email_empty_password(account):
    """
    Check valid email and empty password
    Error message: "Password is required."
    failed
    """
    logging.info("Successful Login")
    logging.warning("Error message: Password is required.")
    assert check_account(account["email"], "tttttt")


@pytest.mark.failed
def test_empty_email_empty_password():
    """
    Check empty email and empty password
    Error message: "An email address required."
    failed
    """
    logging.info("Successful Login")
    logging.warning("Error message: An email address required.")
    assert check_account("", "")


@pytest.mark.failed
def test_empty_email_valid_password(account):
    """
    Check empty email and valid password
    Error message: "An email address required."
    failed
    """
    logging.info("Successful Login")
    logging.warning("Error message: An email address required.")
    assert check_account("", account["password"])


@pytest.mark.failed
def test_hebrew_email_valid_password(account):
    """
    Check hebrew email and valid password
    Error message: "Invalid email address."
    failed
    """
    logging.info("Successful Login")
    logging.warning("Error message: An email address required.")
    assert check_account("אשצשרץדשצשרש@עצשןךץבםצ", account["password"])


@pytest.mark.passed
def test_Forgot_your_password_exists():
    """
    Check if "forgot your password" is in the body
    passed
    """
    dress_page = Start_BuyDress_Page()
    auth_page = AuthenticationPage(dress_page.click_sign_in())
    logging.info("Successful 'forgot your password' is in the body")
    logging.warning('Error, "Forgot your password?" Does not exist in the body')
    assert auth_page.text_in_body("Forgot your password?")
    auth_page.close_page()


@pytest.mark.passed
def test_Click_Forgot_your_password():
    """
    Click Forgot your password and check if "Forgot your password" is in the title
    passed
    """
    dress_page = Start_BuyDress_Page()
    auth_page = AuthenticationPage(dress_page.click_sign_in())
    auth_page.click_forgot_password()
    logging.info('Successful login to "Forgot your password?"')
    logging.warning('Error, "Forgot your password - My Store" Does not exist in the title')
    assert auth_page.title_text() == "Forgot your password - My Store"
    auth_page.close_page()