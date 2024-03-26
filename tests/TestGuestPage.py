import pytest
from configs.Config import link_guest, comment, setup_driver
from poms.GuestPageObjects import GuestPage


class TestGuestPage:
    @pytest.mark.parametrize("setup_driver", [link_guest], indirect=True)
    @pytest.mark.order(4)
    def test_guest_page_post(self, setup_driver):
        self.driver = setup_driver
        self.gp = GuestPage(self.driver)
        is_post = self.gp.check_post()
        self.driver.close()

        assert is_post

    @pytest.mark.parametrize("setup_driver", [link_guest], indirect=True)
    @pytest.mark.order(5)
    def test_guest_page_comment(self, setup_driver):
        self.driver = setup_driver
        self.gp = GuestPage(self.driver)
        self.gp.add_comment(comment)
        comments_list = self.gp.check_comments()
        comment_text = comments_list[-1].text
        self.driver.close()

        assert comment in comment_text
