import pytest
from poms.AdminHomePageObjects import AddPost
from configs.Config import login, link_admin, text, img_url, setup_driver, log_details
from Credentials import email, password

"""
1. Open browser and visit blogger.com
2. Handle login
3. Get post count before adding a new post and store it in post_count
4. Click newpost button
5. Click add img icon and Click by URL
6. Enter img url into text box and Click select button
7. Enter post text into textbox
8. Click Publish button
9. Refresh the page to get the right amount of post list count and store it in post_count_updated
10. Get post status text and store it in element_text
11. Compare post_count and post_count_updated and see if it increased by 1
12. Check if post status is 'Published'
"""


class TestAddPost:
    """This test tries to figure out if it can add post"""
    @pytest.mark.parametrize("setup_driver", [link_admin], indirect=True)
    @pytest.mark.order(2)
    def test_add_post(self, setup_driver):
        self.logger = log_details()
        self.logger.info("-----Testing Add Post-----")

        self.logger.info("1. Open browser and visit blogger.com")
        self.driver = setup_driver
        self.logger.info("Browser opened successfully!")

        self.logger.info("2. Handle login")
        login(self.driver, email, password)

        self.ap = AddPost(self.driver)

        post_count = self.ap.count_of_posts()
        self.logger.info(f"3. Get post count before adding a new post and store it in post_count -> {post_count}")

        self.logger.info("4. Click newpost button")
        self.ap.click_newpost()

        self.logger.info("5. Click add img icon and Click by URL")
        self.ap.click_add_img()

        self.logger.info("6. Enter img url into text box and Click select button")
        self.ap.input_url(img_url)

        self.logger.info("7. Enter post text into textbox")
        self.ap.set_post(text)

        self.logger.info("8. Click Publish button")
        self.ap.click_publish_btn()
        self.logger.info("Post published successfully!")

        self.driver.refresh()
        post_count_updated = self.ap.count_of_posts()
        self.logger.info(
            f"9. Refresh the page to get the right amount of post list count and store it in post_count_updated -> "
            f"{post_count_updated}")

        element_text = self.ap.get_published()
        self.logger.info("10. Get post status text and store it in element_text")

        self.logger.info("11. Compare post_count and post_count_updated and see if it increased by 1")
        assert post_count_updated == post_count + 1

        self.logger.info("12. Check if post status is 'Published'")
        assert "Published" in element_text, "The first element does not contain 'Published'"
