import pytest
from configs.Config import login, log_details
from Credentials import email, password
from configs.Config import link_admin, setup_driver
from poms.AdminHomePageObjects import AddPost

"""
1. Open browser and visit blogger.com
2. Handle login
3. Get post count before adding deleting the last post and store it in post_count
4. Click the trash bin icon on the post
5. Refresh the page to get the right amount of post list count and store it in post_count_updated
6. Compare post_count and post_count_updated and see if it increased by 1
7. Close browser
"""


class TestDeletePost:
    @pytest.mark.parametrize("setup_driver", [link_admin], indirect=True)
    @pytest.mark.order(8)
    def test_delete_post(self, setup_driver):
        self.logger = log_details()
        self.logger.info("-----Testing Delete Post-----")

        self.logger.info("1. Open browser and visit blogger.com")
        self.driver = setup_driver
        self.logger.info("Browser opened successfully!")

        self.logger.info("2. Handle login")
        login(self.driver, email, password)

        self.ap = AddPost(self.driver)

        post_count = self.ap.count_of_posts()
        self.logger.info(f"3. Get post count before adding deleting the last post and "
                         f"store it in post_count -> {post_count}")

        self.logger.info("4. Click the trash bin icon on the post")
        self.ap.click_delete_post()

        self.driver.refresh()
        post_count_updated = self.ap.count_of_posts()
        self.logger.info(f"5. Refresh the page to get the right amount of post list count and store it in "
                         f"post_count_updated -> {post_count_updated}")

        self.logger.info("6. Compare post_count and post_count_updated and see if it decreased by 1")
        assert post_count_updated == post_count - 1
        self.logger.info("7. Close browser")
