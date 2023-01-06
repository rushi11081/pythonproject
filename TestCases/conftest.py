from selenium import webdriver
import pytest
import configparser
from selenium.webdriver.ie.service import Service


service_obj = Service("Driver/chromedriver.exe")

config = configparser.ConfigParser()
config.read("Utilities/input.properties")


@pytest.fixture
def setup(request):
    request.cls.driver = webdriver.Chrome(service=service_obj)
    request.cls.driver.maximize_window()
    request.cls.driver.get(config.get("url","base_url"))
    yield
    request.cls.driver.quit()


