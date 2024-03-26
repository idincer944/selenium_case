import pytest
from selenium import webdriver
from configs.Config import link_admin, send_options, login
from Credentials import email, password


class TestLogin:
    """ This test is trying to figure out if it logins using admin credentials"""
    @pytest.mark.order(1)
    def test_login(self):
        # Setting the driver path and requesting a page
        self.driver = webdriver.Chrome(options=send_options())
        self.driver.implicitly_wait(10)
        self.driver.get(link_admin)
        self.driver.maximize_window()
        login(self.driver, email, password)
        self.act_title = self.driver.title
        self.driver.close()

        assert self.act_title == "Blogger"

# logger ekle
# her case için yorum ekle