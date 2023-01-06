import time

import pytest
import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from PageObjects.LoginPage import Login
from Utilities.logger import logclass

service_obj = Service("Driver/chromedriver.exe")
config = configparser.ConfigParser()
config.read("Utilities/input.properties")


@pytest.mark.usefixtures("setup")
class Test_login(logclass):

    def test_001(self):
        log = self.getthelog()
        lg = Login(self.driver)
        log.info("first test case start")
        log.info("move to my_account")
        lg.click_my_account_tab()
        log.info("wait for to open menu of my_account until login link display")

        lg.explicit_wait()
        log.info("click on login text")
        lg.click_login_text()
        log.info("scroll down page to see login tab ")

        lg.scroll_down_login_page()

        time.sleep(2)
        log.info("enter valid user name")

        lg.input_email(config.get("credential", "correct_username"))
        log.info("enter valid password")

        lg.input_password(config.get("credential", "correct_password"))
        log.info("click on login button")

        lg.click_login_button()
        time.sleep(2)
        assert self.driver.find_element(By.XPATH, "//i[@class='fa fa-exclamation-circle']").is_displayed()
        log.info("Test case pass")

        self.driver.get_screenshot_as_file("Screenshots\\Test2.png")

    def test_002(self):
        log = self.getthelog()
        lg = Login(self.driver)
        log.info("move to my_account")
        lg.click_my_account_tab()
        log.info("wait for to open menu of my_account until login link display")
        lg.explicit_wait()
        log.info("click on login text")
        lg.click_login_text()
        log.info("scroll down page to see login tab ")
        lg.scroll_down_login_page()

        time.sleep(2)
        log.info("enter valid user name")
        lg.input_email(config.get("credential", "correct_username"))
        log.info("enter invalid password")

        lg.input_password(config.get("credential", "incorrect_password"))
        log.info("click on login button")
        lg.click_login_button()

        assert "I am a returning customer" in lg.invalid_message()
        log.info("test case pass")

    def test_003(self):
        log = self.getthelog()
        lg = Login(self.driver)
        log.info("move to my_account")
        lg.click_my_account_tab()
        log.info("wait for to open menu of my_account until login link display")
        lg.explicit_wait()
        log.info("click on login text")
        lg.click_login_text()
        log.info("scroll down page to see login tab ")
        lg.scroll_down_login_page()

        time.sleep(2)
        log.info("enter Invalid user name")
        lg.input_email(config.get("credential", "incorrect_username"))
        log.info("enter valid password")
        lg.input_password(config.get("credential", "correct_password"))
        log.info("click login_button")
        lg.click_login_button()

        assert "I am a returning customer" in lg.invalid_message()
        log.info("pass")
