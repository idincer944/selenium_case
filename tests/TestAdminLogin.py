import pytest
from configs.Config import link_admin, login, setup_driver, title_name, log_details
from Credentials import email, password

"""
1. Open browser and visit blogger.com
2. Handle login
3. Store title name in act_title
4. Close browser 
5. Compare act_title and the right title "Blogger"
"""


class TestLogin:
    """ This test is trying to figure out if it logins using admin credentials """
    @pytest.mark.parametrize("setup_driver", [link_admin], indirect=True)
    @pytest.mark.order(1)
    def test_login(self, setup_driver):
        self.logger = log_details()
        self.logger.info("-----Testing Login-----")
        self.logger.info("1. Open browser and visit blogger.com")
        self.driver = setup_driver
        self.logger.info("Browser opened successfully!")

        self.logger.info("2. Handle login")
        login(self.driver, email, password)

        self.logger.info("5. Store title name in act_title")
        self.act_title = self.driver.title
        self.logger.info("6. Close browser")

        self.logger.info("7. Compare act_title and the right title 'Blogger'")
        assert self.act_title == title_name
