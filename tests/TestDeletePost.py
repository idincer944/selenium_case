import pytest
from configs.Config import login
from Credentials import email, password
from configs.Config import link_admin, setup_driver
from poms.AddPostPageObjects import AddPost
from poms.DeletePostPageObjects import DeletePost


class TestDeletePost:
    @pytest.mark.parametrize("setup_driver", [link_admin], indirect=True)
    @pytest.mark.order(9)
    def test_delete_post(self, setup_driver):
        self.driver = setup_driver

        login(self.driver, email, password)

        self.ap = AddPost(self.driver)

        post_count = self.ap.count_of_posts()

        self.dp = DeletePost(self.driver)
        self.dp.click_delete_post()
        self.driver.refresh()
        post_count_updated = self.ap.count_of_posts()
        self.driver.close()

        assert post_count_updated == post_count - 1


