import pytest
from selenium import webdriver
from poms.EditPostPageObjects import EditPost
from configs.Config import login, link_admin, send_options, edit_text
from Credentials import email, password


class TestEditPost:
    @pytest.mark.order(3)
    def test_edit_post(self):
        options = send_options()
        # Setting the driver path and requesting a page
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)
        self.driver.get(link_admin)
        self.driver.maximize_window()

        login(self.driver, email, password)

        self.ep = EditPost(self.driver)
        self.ep.click_post()
        self.ep.edit_post(edit_text)
        self.ep.update_post()
        self.driver.close()
