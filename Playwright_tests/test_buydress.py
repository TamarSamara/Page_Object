import time
import pytest
from playwright.sync_api import sync_playwright
from playwright_pages.buyDressPage import BuyDressPage
from playwright_pages.authenticationPage import AuthenticationPage

import logging


@pytest.fixture
def account():
    return {
        "email": "tamar.samara@gmail.com",
        "password": "12345"
    }

@pytest.fixture
def Start_buyDress_page(playwright):
    """
    start buyDress page
    """
    chromium = playwright.chromium.launch(headless=False)
    newContext = chromium.new_context()
    page = newContext.new_page()
    page.goto("http://automationpractice.com/index.php")
    return BuyDressPage(page)


def test_buy_dress(account):
    with sync_playwright() as playwright:
        dress_page = Start_buyDress_page(playwright)
        logging.warning(f'Error not fount title "My Store"')
        assert dress_page.title_text() == "My Store"
        time.sleep(3)

        # click sign in
        auth_page = AuthenticationPage(dress_page.click_sign_in())
        logging.warning(f'Error not fount title "Login - My Store"')
        assert auth_page.title_text() == "Login - My Store"

        # send email and password and click sign in
        auth_page.send_email(account["email"])
        # time.sleep(3)
        auth_page.send_password(account["password"])
        # time.sleep(3)
        auth_page.click_signin()
        logging.warning(f'Error not fount title "My account - My Store"')
        assert auth_page.title_text() == "My account - My Store"

        # search summer and click
        dress_page.search_text("summer")
        dress_page.click_search()
        logging.warning(f'Error not fount title "Search - My Store"')
        assert dress_page.title_text() == "Search - My Store"

        # click the cheapest item
        prices = dress_page.price_elements()
        dress_page.Select_The_Cheapest_Item(prices)
        # time.sleep(6)
        dress_page.click_add_to_cart()

        time.sleep(6)
        # go back page
        dress_page.page_back()
        logging.warning(f'Error not fount title 2 "My account - My Store"')
        assert dress_page.title_text() == "My account - My Store"

        # click order cart button
        dress_page.click_order_cart()
        logging.warning(f'Error not fount text in the body "SHOPPING-CART SUMMARY"')
        assert dress_page.text_in_body("SHOPPING-CART SUMMARY")
        # time.sleep(3)

        # click Proceed to checkout
        dress_page.click_Proceed_to_checkout()
        logging.warning(f'Error not fount text in the body "ADDRESSES"')
        assert dress_page.text_in_body("ADDRESSES")

        # click process address
        dress_page.click_proceed_address()
        logging.warning(f'Error not fount text in the body "SHIPPING"')
        assert dress_page.text_in_body("SHIPPING")

        # click_checkbox
        dress_page.click_checkbox()
        time.sleep(5)

        # click process carrier
        dress_page.click_process_carrier()
        logging.warning(f'Error not fount "Order - My Store" in the title ')
        assert dress_page.title_text() == "Order - My Store"

        # click bank wire
        dress_page.click_bank_wire()
        logging.warning(f'Error not fount "My Store" in the title')
        assert dress_page.title_text() == "My Store"

        # click confirm my order
        dress_page.click_confirm_my_order()
        logging.warning(' Error not found title "My Store"')
        assert dress_page.title_text() == "My Store"

        time.sleep(5)
        dress_page.close_page()
