from pages.basePage import BasePage
from selenium.webdriver.common.by import By
import time


class BuyDressPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    locator = {
        "SIGNIN_BUTTON": (By.CLASS_NAME, 'login'),
        "SEARCH_TEXT": (By.ID, "search_query_top"),
        "CLICK_SEARCH": (By.NAME, 'submit_search'),
        "PRICES": (By.CLASS_NAME, 'content_price'),
        "INDEX0": (By.XPATH, '//*[@id="center_column"]/ul/li[1]/div/div[2]/div[2]/a[1]/span'),
        "INDEX1": (By.XPATH, '//*[@id="center_column"]/ul/li[2]/div/div[2]/div[2]/a[1]/span'),
        "INDEX2": (By.XPATH, '//*[@id="center_column"]/ul/li[3]/div/div[1]/div/a[1]/img'),
        "INDEX3": (By.XPATH, '//*[@id="center_column"]/ul/li[4]/div/div[2]/div[2]/a[1]/span'),
        "ADD_TO_CART": (By.XPATH, '//*[@id="add_to_cart"]/button'),
        "CLOSE_WINDOW": (By.XPATH, '//*[@id="layer_cart"]/div[1]/div[1]/span'),
        "ORDER_CART_BUTTON": (By.XPATH, '//*[@id="header"]/div[3]/div/div/div[3]/div/a'),
        "PROCEED_TO_CHECKOUT": (By.XPATH, '//*[@id="center_column"]/p[2]/a[1]'),
        "PROCESS_ADDRESS": (By.NAME, "processAddress"),
        "PROCESS_CARRIER": (By.NAME, "processCarrier"),
        "CHECKBOX": (By.ID, "cgv"),
        "BANK_WIRE": (By.CLASS_NAME, "bankwire"),
        "SUBMIT": (By.ID, "module-bankwire-payment")

    }

    def click_sign_in(self):
        """
        click login
        """
        self._driver.find_element(*self.locator["SIGNIN_BUTTON"]).click()
        return self._driver

    def search_text(self, text):
        """
        search text
        """
        self._driver.find_element(*self.locator["SEARCH_TEXT"]).send_keys(text)

    def click_search(self):
        """
        click search
        """
        self._driver.find_element(*self.locator["CLICK_SEARCH"]).click()

    def price_elements(self):
        """
        :return list of prices
        """
        return self._driver.find_elements(*self.locator["PRICES"])

    def Select_The_Cheapest_Item(self, prices):
        """
        click the cheapest price
        """
        # 'for' for all price items, cut off all '$', and take only 5 places from the string
        list1 = []
        for i in range(len(prices) - 1):
            if '$' in prices[i + 1].text:
                price2 = prices[i + 1].text.replace('$', '')[0:5]
                list1.append(price2)

        minp = float(list1[0])
        index = 0
        # "for" for all prices and convert them from a string to an integer, and take the cheapest price
        for i in range(len(list1)):
            floatPrice = float(list1[i])
            if minp > floatPrice:
                minp = floatPrice
                index = i

        # Click on the item with the help of index
        if index == 0:
            self._driver.find_element(*self.locator["INDEX0"]).click()
        if index == 1:
            self._driver.find_element(*self.locator["INDEX1"]).click()
        if index == 2:
            self._driver.find_element(*self.locator["INDEX2"]).click()
        if index == 3:
            self._driver.find_element(*self.locator["INDEX3"]).click()
        time.sleep(5)

    def click_add_to_cart(self):
        """
        click add to cart
        """
        iframe = self._driver.find_element(By.CLASS_NAME, "fancybox-iframe")
        self._driver.switch_to.frame(iframe)
        self._driver.find_element(*self.locator["ADD_TO_CART"]).click()

    def click_order_cart(self):
        """
        click order cart button
        """
        self._driver.find_element(*self.locator["ORDER_CART_BUTTON"]).click()

    def click_Proceed_to_checkout(self):
        """
        Proceed to checkout
        """
        self._driver.find_element(*self.locator["PROCEED_TO_CHECKOUT"]).click()

    def click_proceed_address(self):
        """
        click proceed address
        """
        self._driver.find_element(*self.locator["PROCESS_ADDRESS"]).click()

    def click_process_carrier(self):
        """
        click process carrier
        """
        self._driver.find_element(*self.locator["PROCESS_CARRIER"]).click()

    def click_checkbox(self):
        """
        click_checkbox
        """
        self._driver.find_element(*self.locator["CHECKBOX"]).click()

    def click_bank_wire(self):
        """
        click bank wire
        """
        self._driver.find_element(*self.locator["BANK_WIRE"]).click()

    def click_confirm_my_order(self):
        """
        click confirm my order
        """
        self._driver.find_element(*self.locator["SUBMIT"]).click()
