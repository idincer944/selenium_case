import pytest
from selenium import webdriver
from configs.config import login
from credentials import email, password
from configs.config import link_admin, send_options
from poms.add_post_page_objects import AddPost
from poms.delete_post_page_objects import DeletePost


class TestDeletePost:
    @pytest.mark.order(9)
    def test_delete_post(self):
        options = send_options()
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)
        self.driver.get(link_admin)
        self.driver.maximize_window()

        login(self.driver, email, password)

        self.ap = AddPost(self.driver)

        post_count = self.ap.count_of_posts()

        self.dp = DeletePost(self.driver)
        self.dp.click_delete_post()
        self.driver.refresh()
        post_count_updated = self.ap.count_of_posts()
        self.driver.close()

        assert post_count_updated == post_count - 1


