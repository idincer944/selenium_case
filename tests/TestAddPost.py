import pytest
from poms.AddPostPageObjects import AddPost
from configs.Config import login, link_admin, text, img_url, setup_driver
from Credentials import email, password


class TestAddPost:
    @pytest.mark.parametrize("setup_driver", [link_admin], indirect=True)
    @pytest.mark.order(2)
    def test_add_post(self, setup_driver):
        self.driver = setup_driver

        login(self.driver, email, password)

        self.ap = AddPost(self.driver)

        post_count = self.ap.count_of_posts()

        self.ap.click_newpost()
        self.ap.click_add_img()
        self.ap.input_url(img_url)
        self.ap.set_post(text)
        self.ap.click_publish_btn()
        self.driver.refresh()
        post_count_updated = self.ap.count_of_posts()
        element_text = self.ap.get_published()

        # Check if a new post added
        assert post_count_updated == post_count + 1

        # Check if the new post Published
        assert "Published" in element_text, "The first element does not contain 'Published'"
