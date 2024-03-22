import pytest
from selenium import webdriver
from poms.add_post_page_objects import AddPost
from configs.config import login, link_admin, send_options, text, img_url
from credentials import email, password


class TestAddPost:
    @pytest.mark.order(2)
    def test_add_post(self):
        options = send_options()
        # Setting the driver path and requesting a page
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)
        self.driver.get(link_admin)
        self.driver.maximize_window()

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
        self.driver.close()

        # Check if a new post added
        assert post_count_updated == post_count + 1

        # Check if the new post Published
        assert "Published" in element_text, "The first element does not contain 'Published'"
