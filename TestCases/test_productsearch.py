import time

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from PageObjects.LoginPage import Login
from PageObjects.ProductSearchPage import Product_search

service_obj = Service("Driver/chromedriver.exe")


@pytest.mark.usefixtures("setup")
class Test_product_search:
    @pytest.mark.parametrize('product_name', ["Macbook", "iMac", "Samsung"])
    def test_001(self, product_name):
        pc = Product_search(self.driver)
        pc.input_product_search(product_name)
        pc.click_Search_button()
        assert product_name in pc.search_result_message()
        # assert "macbook" in pc.search_result_message()

    def test_002(self):

        pc = Product_search(self.driver)
        pc.input_product_search("macbook")
        pc.click_Search_button()
        assert pc.check_product_count() > 0

    def test_003(self):
        actualList = ["MacBook", "MacBook Air", "MacBook Pro"]
        expect_list = []
        pc = Product_search(self.driver)
        pc.input_product_search("macbook")
        pc.click_Search_button()
        product_list = self.driver.find_elements(By.XPATH, "//div[@class='caption']")
        for product in product_list:
            expect_list.append(product.find_element(By.XPATH, "h4").text)

        assert actualList == expect_list





