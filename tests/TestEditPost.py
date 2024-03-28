import time
import pytest
from poms.AdminHomePageObjects import AddPost
from poms.EditPostPageObjects import EditPost
from configs.Config import login, link_admin, edit_text, setup_driver, log_details
from Credentials import email, password

"""
1. Open browser and visit blogger.com
2. Handle login
3. Click the first post
4. Enter new text into title box
5. Click Update
6. Go back to previous page(Home Page)
7. Get post text and store it in eddited_text
8. Check if the new text is in eddited_text
"""


class TestEditPost:
    """ This test is trying to figure out if it can edit a post """
    @pytest.mark.parametrize("setup_driver", [link_admin], indirect=True)
    @pytest.mark.order(3)
    def test_edit_post(self, setup_driver):
        self.logger = log_details()
        self.logger.info("-----Testing Edit Post-----")

        self.logger.info("1. Open browser and visit blogger.com")
        self.driver = setup_driver
        self.logger.info("Browser opened successfully!")

        self.logger.info("2. Handle login")
        login(self.driver, email, password)

        self.ep = EditPost(self.driver)

        self.logger.info("3. Click the first post")
        self.ep.click_post()

        self.logger.info("4. Enter new text into title box")
        self.ep.edit_post(edit_text)

        self.logger.info("5. Click Update")
        self.ep.update_post()

        self.logger.info("6. Go back to previous page(Home Page)")
        self.driver.back()

        self.ap = AddPost(self.driver)
        time.sleep(3)

        self.logger.info("7. Get post text and store it in eddited_text")
        eddited_text = self.ap.get_published()

        self.logger.info("8. Check if the new text is in eddited_text")
        assert edit_text in eddited_text, "The first element does not contain text edit"
