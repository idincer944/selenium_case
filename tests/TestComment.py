import time
import pytest
from poms.CommentPageObjects import CheckComment
from configs.Config import login, link_admin, comment, link_guest, setup_driver, log_details, take_screenshot
from Credentials import email, password

global comment_id_admin

"""
1. Open browser and visit blogger.com
2. Handle login
3. Click Comments navigator
4. Get last comment text and store it in _last_comment 
5. Get comment id from Admin page and store it in global variable get_comment_admin_id
6. Check if added comment is in the last comment in Admin page
7. Close browser
8. Open browser and visit blogger.com
9. Handle login
10. Click Comments navigator
11. Click delete comment
12. Close browser
13. Open browser and visit idincer944.blogpost.com as a guest
14. Get the last comment's id on the guest page
15. Compare comment_id_admin and self.comment_id_with_c
16. Close browser
"""


class TestCheckComment:
    """ This test is trying to figure out if
        1. the comment exists
        2. it can delete comment
        3. the comment is deleted
    """
    @pytest.mark.parametrize("setup_driver", [link_admin], indirect=True)
    @pytest.mark.order(5)
    def test_check_comment(self, setup_driver):
        self.logger = log_details()
        self.logger.info("-----Testing Check Comment-----")

        self.logger.info("1. Open browser and visit blogger.com")
        self.driver = setup_driver
        self.logger.info("Browser opened successfully!")

        self.logger.info("2. Handle login")
        login(self.driver, email, password)

        self.logger.info("3. Click Comments navigator")
        self.cc = CheckComment(self.driver)
        self.cc.click_comments()

        self.logger.info("4. Get last comment text and store it in _last_comment")
        _last_comment = self.cc.check_comment_admin_page().text

        global comment_id_admin
        comment_id_admin = self.cc.get_comment_admin_id()
        self.logger.info(f"5. Get comment id from Admin page and "
                         f"store it in global variable get_comment_admin_id -> {comment_id_admin}")

        self.logger.info("6. Check if added comment is in the last comment in Admin page")
        assert comment in _last_comment, take_screenshot(self.driver)
        self.logger.info("7. Close browser")

    @pytest.mark.parametrize("setup_driver", [link_admin], indirect=True)
    @pytest.mark.order(6)
    def test_delete_comment(self, setup_driver):
        self.logger = log_details()
        self.logger.info("-----Testing Delete Comment-----")

        self.logger.info("8. Open browser and visit blogger.com")
        self.driver = setup_driver
        self.logger.info("Browser opened successfully!")

        self.logger.info("9. Handle login")
        login(self.driver, email, password)

        self.logger.info("10. Click Comments navigator")
        self.cc = CheckComment(self.driver)
        self.cc.click_comments()

        self.logger.info("11. Click delete comment")
        self.cc.click_delete_comment()
        self.logger.info("Comment deleted successfully!")
        self.logger.info("12. Close browser")

    @pytest.mark.parametrize("setup_driver", [link_guest], indirect=True)
    @pytest.mark.order(7)
    def test_comment_status(self, setup_driver):
        self.logger = log_details()
        self.logger.info("-----Testing Comment Status-----")

        self.logger.info("13. Open browser and visit blogger.com")
        self.driver = setup_driver
        self.logger.info("Browser opened successfully!")

        self.cc = CheckComment(self.driver)

        self.comment_id_with_c = self.cc.get_comment_guest_id()
        self.logger.info(f"14. Get the last comment's id on the guest page -> {self.comment_id_with_c}")

        global comment_id_admin
        self.logger.info(f"15. Compare comment_id_admin and self.comment_id_with_c -> {comment_id_admin}")
        assert comment_id_admin != self.comment_id_with_c, take_screenshot(self.driver)
        self.logger.info("16. Close browser")
