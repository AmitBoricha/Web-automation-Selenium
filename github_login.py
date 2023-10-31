from tests import BaseClass
from locator.github_login_page_locator import *
from selenium.webdriver.common.keys import Keys


class TestGithubPage(BaseClass):
    def test_1_login_wrong_username_wrong_password(self):
        self.log().info("Github Login Page Bad case Test Started")
        self.driver.get("https://github.com/login")