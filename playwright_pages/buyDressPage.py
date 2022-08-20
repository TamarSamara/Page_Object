from playwright_pages.basePage import BasePage
import time


class BuyDressPage(BasePage):
    locators = {
        "SIGNIN_BUTTON": "a.login",
        "SEARCH_TEXT": '#search_query_top',
        "CLICK_SEARCH": 'button.button-search',
        "PRICES": 'ul.product_list li .product-price',
        "INDEX0": 'ul.product_list lw',
        "INDEX1": 'ul.product_list le',
        "INDEX2": 'ul.product_list li',
        "INDEX3": 'ul.product_list la',
        "ADD_TO_CART": "text='Add to cart'",
        "CLOSE_WINDOW": 'span.cross',
        "IFRAME": "fancybox-iframe",
        "ORDER_CART_BUTTON": "button >> text='Proceed to checkout'",
        "PROCEED_TO_CHECKOUT": "text='Proceed to checkout'",
        "PROCESS_ADDRESS":  "processAddress",
        "PROCESS_CARRIER": "button >> text='Proceed to checkout'",
        "CHECKBOX": "#total_product",
        "BANK_WIRE": "text='Pay by bank wire'",
        "SUBMIT": "button >> text='I confirm my order'"
    }

    def __init__(self, page):
        super().__init__(page)

    def click_sign_in(self):
        """
        click login
        """
        self._page.locator(self.locators["SIGNIN_BUTTON"]).click()
        return self._page

    def search_text(self, text):
        """
        search text
        """
        self._page.locator(self.locators["SEARCH_TEXT"]).fill(text)

    def click_search(self):
        """
        click search
        """
        self._page.locator(self.locators["CLICK_SEARCH"]).click()

    def price_elements(self):
        """
        :return list of prices
        """
        return self._page.locator(self.locators["PRICES"])

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
            self._page.locator(self.locators["INDEX0"]).click()
        if index == 1:
            self._page.locator(self.locators["INDEX1"]).click()
        if index == 2:
            self._page.locator(self.locators["INDEX2"]).click()
        if index == 3:
            self._page.locator(self.locators["INDEX3"]).click()
        time.sleep(5)

    def click_order_cart(self):
        """
        click order cart button
        """
        self._page.locator(self.locators["ORDER_CART_BUTTON"]).click()

    def click_Proceed_to_checkout(self):
        """
        Proceed to checkout
        """
        self._page.locator(self.locators["PROCEED_TO_CHECKOUT"]).click()

    def click_proceed_address(self):
        """
        click proceed address
        """
        self._page.locator(self.locators["PROCESS_ADDRESS"]).click()

    def click_process_carrier(self):
        """
        click process carrier
        """
        self._page.locator(self.locators["PROCESS_CARRIER"]).click()

    def click_checkbox(self):
        """
        click_checkbox
        """
        self._page.locator(self.locators["CHECKBOX"]).click()

    def click_bank_wire(self):
        """
        click bank wire
        """
        self._page.locator(self.locators["BANK_WIRE"]).click()

    def click_confirm_my_order(self):
        """
        click confirm my order
        """
        self._page.locator(self.locators["SUBMIT"]).click()
