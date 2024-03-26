import pytest
from configs.Config import link_admin, login, setup_driver
from Credentials import email, password


class TestLogin:
    """ This test is trying to figure out if it logins using admin credentials"""
    @pytest.mark.parametrize("setup_driver", [link_admin], indirect=True)
    @pytest.mark.order(1)
    def test_login(self, setup_driver):
        self.driver = setup_driver
        login(self.driver, email, password)
        self.act_title = self.driver.title
        self.driver.close()

        assert self.act_title == "Blogger"

# logger ekle
# her case için yorum ekle
