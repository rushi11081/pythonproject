import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Add_cart:

    def __init__(self, driver):
        self.driver = driver
        self.product_list = "//div[@class='caption']"
        self.product_list_by_xpath = "//div[@class='caption/h4/a']"
        self.add_cart_button_by_xpath = "(//span[text()='Add to Cart'])[3]"
        self.top_cart_button_by_xpath = "//button[@data-toggle='dropdown'])[2]"
        self.view_cart_btn_by_xpath = "//i[@class='fa fa-shopping-cart'])[3]"
        self.added_product_text_by_xpath = "(//a[text()='MacBook Pro'])[1]"
        self.product_price_by_xpath = "(//p[@class='price'])[3]"
        self.cart_price_by_xpath = "//span[@id='cart-total']"
        self.item_added_correct_msg_by_xpath = "//div[@class='alert alert-success alert-dismissible']"

    def add_cart_button_click(self):
        self.driver.find.element(By.XPATH, self.add_cart_button_by_xpath).click()
        self.driver.find.element(By.XPATH, self.top_cart_button_by_xpath).click()
        self.driver.find.element(By.XPATH, self.view_cart_btn_by_xpath).click()

    def gettext_of_added_product(self):
        product_list = self.driver.find_elements(By.XPATH, self.product_list)

        for product in product_list:

            if product.find_element(By.XPATH, "h4").text == "MacBook Pro":
                result = self.driver.find_element(By.XPATH, self.added_product_text_by_xpath).text
                return result

    def get_price_product(self):
        product_list = self.driver.find_elements(By.XPATH, self.product_list_by_xpath)
        for product in product_list:
            prod = product.text
            if prod == "MacBook Pro":
                price = self.driver.find_element(By.XPATH, self.product_price_by_xpath).text
                price1 = price.split()
                return price1[0]

    def get_cart_price(self):
        product_list = self.driver.find_elements(By.XPATH, self.product_list_by_xpath)
        for product in product_list:
            prod = product.text
            if prod == "MacBook Pro":
                price = self.driver.find_element(By.XPATH, self.product_price_by_xpath).text
                price1 = price.split()

                self.driver.find_element(By.XPATH, self.add_cart_button_by_xpath).click()
                time.sleep(3)

                cart_price = self.driver.find_element(By.XPATH, self.cart_price_by_xpath).text
                cart_price1 = cart_price.split()
                return cart_price1[3]

    def item_added_correct_msg(self):
        product_list = self.driver.find_elements(By.XPATH,"//div[@class='caption/h4/a']")
        for product in product_list:
            prod = product.text
            if prod == "MacBook Pro":
                self.driver.find_element(By.XPATH, "(//span[text()='Add to Cart'])[3]").click()
                time.sleep(3)
                return self.driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text

