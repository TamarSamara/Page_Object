import time
import pytest
from selenium import webdriver
from pages.buyDressPage import BuyDressPage
from pages.authenticationPage import AuthenticationPage
import logging


@pytest.fixture
def account():
    return {
        "email": "tamar.samara@gmail.com",
        "password": "12345"
    }


def Start_buyDress_page():
    """
    start buyDress page
    """
    driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
    driver.maximize_window()
    driver.get('http://automationpractice.com/index.php')
    return BuyDressPage(driver)


def test_buy_dress(account):
    dress_driver = Start_buyDress_page()
    logging.warning(f'Error not fount title "My Store"')
    assert dress_driver.title_text() == "My Store"
    # time.sleep(3)

    # click sign in
    Auth_driver = AuthenticationPage(dress_driver.click_sign_in())
    logging.warning(f'Error not fount title "Login - My Store"')
    assert Auth_driver.title_text() == "Login - My Store"

    # send email and password and click sign in
    Auth_driver.send_email(account["email"])
    # time.sleep(3)
    Auth_driver.send_password(account["password"])
    # time.sleep(3)
    Auth_driver.click_signin()
    logging.warning(f'Error not fount title "My account - My Store"')
    assert Auth_driver.title_text() == "My account - My Store"

    # search summer and click
    dress_driver.search_text("summer")
    dress_driver.click_search()
    logging.warning(f'Error not fount title "Search - My Store"')
    assert dress_driver.title_text() == "Search - My Store"

    # click the cheapest item
    prices = dress_driver.price_elements()
    dress_driver.Select_The_Cheapest_Item(prices)
    # time.sleep(6)
    dress_driver.click_add_to_cart()

    time.sleep(6)
    # go back page
    dress_driver.page_back()
    logging.warning(f'Error not fount title 2 "My account - My Store"')
    assert dress_driver.title_text() == "My account - My Store"

    # click order cart button
    dress_driver.click_order_cart()
    logging.warning(f'Error not fount text in the body "SHOPPING-CART SUMMARY"')
    assert dress_driver.text_in_body("SHOPPING-CART SUMMARY")
    # time.sleep(3)

    # click Proceed to checkout
    dress_driver.click_Proceed_to_checkout()
    logging.warning(f'Error not fount text in the body "ADDRESSES"')
    assert dress_driver.text_in_body("ADDRESSES")

    # click process address
    dress_driver.click_proceed_address()
    logging.warning(f'Error not fount text in the body "SHIPPING"')
    assert dress_driver.text_in_body("SHIPPING")

    # click_checkbox
    dress_driver.click_checkbox()
    time.sleep(5)

    # click process carrier
    dress_driver.click_process_carrier()
    logging.warning(f'Error not fount "Order - My Store" in the title ')
    assert dress_driver.title_text() == "Order - My Store"

    # click bank wire
    dress_driver.click_bank_wire()
    logging.warning(f'Error not fount "My Store" in the title')
    assert dress_driver.title_text() == "My Store"

    # click confirm my order
    dress_driver.click_confirm_my_order()
    logging.warning(' Error not found title "My Store"')
    assert dress_driver.title_text() == "My Store"

    time.sleep(5)
    dress_driver.close_page()
