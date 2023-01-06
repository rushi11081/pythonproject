from selenium.webdriver.common.by import By
from selenium import webdriver


class Product_search:

    def __init__(self, driver):
        self.driver = driver

        self.search_textbox_by_css = "input[name='search']"
        self.search_button_by_css = "div#search button"
        self.search_result_text_by_css = "div#content h1"
        self.product_list_by_xpath = "//div[@class='caption']"

    def input_product_search(self, product_name):
        self.driver.find_element(By.CSS_SELECTOR, self.search_textbox_by_css).send_keys(product_name)

    def click_Search_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.search_button_by_css).click()

    def search_result_message(self):
        result = self.driver.find_element(By.CSS_SELECTOR, self.search_result_text_by_css).text
        return result

    def check_product_count(self):
        product_list = self.driver.find_elements(By.XPATH, "//div[@class='caption']")
        count = len(product_list)
        return count

    def check_product_list(self):
        actualList = ["MacBook", "MacBook Air", "MacBook Pro"]
        expect_list = []
        pc = Product_search(self.driver)
        pc.input_product_search("macbook")
        pc.click_Search_button()
        product_list = self.driver.find_elements(By.XPATH, "//div[@class='caption']")
        for product in product_list:
            expect_list = expect_list.append(product.find_element(By.XPATH, "h4").text)
            return expect_list
