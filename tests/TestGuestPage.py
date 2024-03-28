import pytest
from configs.Config import link_guest, comment, setup_driver, log_details
from poms.GuestPageObjects import GuestPage

"""
1. Open browser and visit idincer944.blogpost.com as a guest
2. Check if there is post
3. Click Post a Comment button and add comment
4. Store all comments in a list and get the last comment
5. Check if added comment in the last comment
"""


class TestGuestPage:
    """ This test is trying to figure out if it can add comment to a post """
    @pytest.mark.parametrize("setup_driver", [link_guest], indirect=True)
    @pytest.mark.order(4)
    def test_guest_page(self, setup_driver):
        self.logger = log_details()
        self.logger.info("-----Testing Guest Page-----")

        self.logger.info("1. Open browser and idincer944.blogpost.com as a guest")
        self.driver = setup_driver
        self.logger.info("Browser opened successfully!")

        self.gp = GuestPage(self.driver)

        self.logger.info("2. Check if there is post")
        is_post = self.gp.check_post()
        assert is_post

        self.logger.info("3. Click Post a Comment button, login and add comment")
        self.gp.add_comment(comment)

        self.logger.info("4. Store all comments in a list and get the last comment")
        comments_list = self.gp.check_comments()
        comment_text = comments_list[-1].text

        self.logger.info("5. Check if added comment in the last comment")
        assert comment in comment_text
