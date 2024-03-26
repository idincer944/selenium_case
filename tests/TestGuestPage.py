import pytest
from selenium import webdriver
from configs.Config import link_guest, send_options, comment
from poms.GuestPageObjects import GuestPage


class TestGuestPage:
    @pytest.mark.order(4)
    def test_guest_page_post(self):
        options = send_options()
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)
        self.driver.get(link_guest)
        self.driver.maximize_window()

        self.gp = GuestPage(self.driver)
        is_post = self.gp.check_post()
        self.driver.close()

        assert is_post

    @pytest.mark.order(5)
    def test_guest_page_comment(self):
        options = send_options()
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)
        self.driver.get(link_guest)
        self.driver.maximize_window()

        self.gp = GuestPage(self.driver)
        self.gp.add_comment(comment)
        comments_list = self.gp.check_comments()
        comment_text = comments_list[-1].text
        self.driver.close()

        assert comment in comment_text

