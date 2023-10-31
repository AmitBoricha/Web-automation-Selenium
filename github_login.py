from tests import BaseClass
from locator.github_login_page_locator import *
from selenium.webdriver.common.keys import Keys


class TestGithubPage(BaseClass):
    def test_1_login_wrong_username_wrong_password(self):
        self.log().info("Github Login Page Bad case Test Started")
        self.driver.get("https://github.com/login")
        self.get_element(USERNAME_INPUT).send_keys('Test')  # wrong Username
        self.get_element(PASSWORD_INPUT).send_keys('test123')  # Wrong Password
        self.get_element(SIGNIN_BUTTON).submit()
        self.log().info("Test Success")
        assert self.get_element(SIGNIN_BUTTON).is_displayed()

    def test_2_login(self):
        self.log().info("Github Login Page Good case Test Started")
        self.get_element(USERNAME_INPUT).clear()
        self.get_element(PASSWORD_INPUT).clear()
        self.get_element(USERNAME_INPUT).send_keys('jagwithyou')  # right Username
        self.get_element(PASSWORD_INPUT).send_keys('Jag143NBS@#')  # right Password
        self.get_element(SIGNIN_BUTTON).submit()
        self.log().info("Test Success")