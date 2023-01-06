from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Login:

    def __init__(self, driver):
        self.driver = driver

        self.My_Account_tab_xpath = "//span[text()='My Account']"
        self.LoginLink_link_text = "Login"
        self.Email_input_xpath = "//input[@id='input-email']"
        self.Password_input_xpath = "//input[@id='input-password']"
        self.Login_button_xpath = "//input[@value='Login'] "
        self.Logout_link_xpath = " //i[@class='fa fa-exclamation-circle']"
        self.my_account_xpath = "(//div[@id='content']/h2)[1]"
        self.Invalid_link_errortext_xpath = "//p//strong[text()='I am a returning customer']"

    def input_email(self, username):
        self.driver.find_element(By.XPATH, self.Email_input_xpath).send_keys(username)

    def input_password(self, pwd):
        self.driver.find_element(By.XPATH, self.Password_input_xpath).send_keys(pwd)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.Login_button_xpath).click()

    def click_my_account_tab(self):
        self.driver.find_element(By.XPATH, self.My_Account_tab_xpath).click()

    def invalid_message(self):
        return self.driver.find_element(By.XPATH, self.Invalid_link_errortext_xpath).text

    def explicit_wait(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, self.LoginLink_link_text)))

    def scroll_down_login_page(self):
        self.driver.execute_script("window.scrollBy(0,350);")

    def click_login_text(self):
        self.driver.find_element(By.LINK_TEXT, self.LoginLink_link_text).click()

    def valid_login_msg(self):
        return self.driver.find_element(By.XPATH,self.my_account_xpath).text

