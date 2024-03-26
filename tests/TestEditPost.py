import pytest
from poms.EditPostPageObjects import EditPost
from configs.Config import login, link_admin, edit_text, setup_driver
from Credentials import email, password


class TestEditPost:
    @pytest.mark.parametrize("setup_driver", [link_admin], indirect=True)
    @pytest.mark.order(3)
    def test_edit_post(self, setup_driver):
        self.driver = setup_driver
        login(self.driver, email, password)

        self.ep = EditPost(self.driver)
        self.ep.click_post()
        self.ep.edit_post(edit_text)
        self.ep.update_post()
        self.driver.close()
