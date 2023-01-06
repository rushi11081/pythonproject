import time

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.AddCartPage import Add_cart
from PageObjects.LoginPage import Login
from PageObjects.ProductSearchPage import Product_search

service_obj = Service("Driver/chromedriver.exe")


@pytest.mark.usefixtures("setup")
class Test_Add_Cart:

    def test_001(self):
        pc = Product_search(self.driver)
        ac = Add_cart(self.driver)
        pc.input_product_search("macbook")
        pc.click_Search_button()

        assert "MacBook Pro" == ac.gettext_of_added_product()

    def test_002(self):
        pc = Product_search(self.driver)
        ac = Add_cart(self.driver)
        pc.input_product_search("macbook")
        pc.click_Search_button()
        assert ac.get_cart_price() == ac.get_price_product()

    @pytest.mark.skip
    def test_003(self):
        pc = Product_search(self.driver)
        ac = Add_cart(self.driver)
        pc.input_product_search("macbook")
        pc.click_Search_button()
        assert "Success" in ac.item_added_correct_msg()
