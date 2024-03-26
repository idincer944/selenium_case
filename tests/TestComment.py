import time
import pytest
from selenium.webdriver.common.by import By
from poms.CommentPageObjects import CheckComment
from configs.Config import login, link_admin, comment, link_guest, setup_driver
from Credentials import email, password
from poms.GuestPageObjects import GuestPage
global get_comment_admin_id


class TestCheckComment:
    @pytest.mark.parametrize("setup_driver", [link_admin], indirect=True)
    @pytest.mark.order(6)
    def test_check_comment(self, setup_driver):
        self.driver = setup_driver

        login(self.driver, email, password)

        self.cc = CheckComment(self.driver)
        self.cc.click_comments()
        _last_comment = self.cc.check_comment_admin_page().text
        global get_comment_admin_id
        get_comment_admin_id = self.cc.get_comment_admin_id()
        # self.driver.close()
        assert comment in _last_comment

    @pytest.mark.parametrize("setup_driver", [link_admin], indirect=True)
    @pytest.mark.order(7)
    def test_delete_comment(self, setup_driver):
        self.driver = setup_driver

        login(self.driver, email, password)

        self.cc = CheckComment(self.driver)
        self.cc.click_comments()
        self.cc.click_delete_comment()
        time.sleep(3)
        # self.driver.close()

    @pytest.mark.parametrize("setup_driver", [link_guest], indirect=True)
    @pytest.mark.order(8)
    def test_comment_status(self, setup_driver):
        self.driver = setup_driver

        self.gp = GuestPage(self.driver)
        self.driver.find_element(By.XPATH, self.gp.a_comment_xpath).click()
        comments_list = self.gp.check_comments()
        if len(comments_list) > 0:
            self.comment_id_with_c = comments_list[-1].get_attribute("id")
        else:
            self.comment_id_with_c = "0"
        global get_comment_admin_id
        before_id = "c" + str(get_comment_admin_id)
        after_id = self.comment_id_with_c

        assert before_id != after_id
