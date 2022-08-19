import pytest
from selenium import webdriver
from pages.buyDressPage import BuyDressPage
from pages.authenticationPage import AuthenticationPage
import logging
import time


@pytest.fixture
def account():
    return {
        "email": "tamar.samara@gmail.com",
        "password": "12345"
    }


def Start_BuyDress_Page():
    """
    start BuyDress page
    """
    driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
    driver.maximize_window()
    driver.get('http://automationpractice.com/index.php')
    return BuyDressPage(driver)


def check_account(email, password):
    dress_driver = Start_BuyDress_Page()
    # time.sleep(3)
    driver = AuthenticationPage(dress_driver.click_sign_in())
    # time.sleep(3)
    driver.send_email(email)
    # time.sleep(3)
    driver.send_password(password)
    # time.sleep(3)
    driver.click_signin()
    time.sleep(3)
    text = driver.title_text()
    driver.close_page()
    return text == "My account - My Store"


@pytest.mark.passed
def test_Forgot_your_password_exists():
    """
    Check if forgot your title exists
    passed
    """
    dress_driver = Start_BuyDress_Page()
    driver = AuthenticationPage(dress_driver.click_sign_in())
    logging.info("Successful 'Login - My Store' is in the body")
    logging.warning('Error, "Login - My Store" Does not exist in the body')
    assert driver.title_text() == "Login - My Store"
    driver.close_page()


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
    dress_driver = Start_BuyDress_Page()
    driver = AuthenticationPage(dress_driver.click_sign_in())
    logging.info("Successful 'forgot your password' is in the body")
    logging.warning('Error, "Forgot your password?" Does not exist in the body')
    assert driver.text_in_body("Forgot your password?")
    driver.close_page()


@pytest.mark.passed
def test_Click_Forgot_your_password():
    """
    Click Forgot your password and check if "Forgot your password" is in the title
    passed
    """
    dress_driver = Start_BuyDress_Page()
    driver = AuthenticationPage(dress_driver.click_sign_in())
    driver.click_forgot_password()
    logging.info('Successful login to "Forgot your password?"')
    logging.warning('Error, "Forgot your password - My Store" Does not exist in the title')
    assert driver.title_text() == "Forgot your password - My Store"
    driver.close_page()
