from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from poms.GuestPageObjects import GuestPage


class CheckComment:
    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Locators
    nvgtr_comments_xpath = "(//a[@class='Un8wMb zRRGMc'])[12]"
    last_comment_xpath_admin = "(//div[@class='Opvl3b'])[1]"
    last_comment_xpath_for_id = "(//div[@class='Zl8jqd'])[1]"
    delete_icon_xpath = ("//c-wiz[@class='zQTmif SSPGKf eejsDc qWnhY O3LMFb haXJ6e']//div["
                         "@role='list']//div[1]//span[1]//div[1]//div[1]//div[4]//div[3]//span["
                         "1]//span[1]//span[1]")
    delete_button_xpath = "//*[@id='yDmH0d']/div[4]/div/div[2]/div[2]/div[2]"
    guest_page_comment_button_xpath = "//a[@class='comment-link']"

    # Action Methods
    def click_comments(self):
        """
        This function clicks Comments navigator in the home page
        """
        self.driver.find_element(By.XPATH, self.nvgtr_comments_xpath).click()

    def check_comment_admin_page(self):
        """
        This function gets the last comment in admin page
        :return: It returns the last comment as a web element
        """
        last_comment = self.driver.find_element(By.XPATH, self.last_comment_xpath_admin)
        return last_comment

    def click_delete_comment(self):
        """
        This function deletes the last comment in admin page by clicking the trash bin icon
        """
        action = ActionChains(self.driver)
        last_comment = self.driver.find_element(By.XPATH, self.last_comment_xpath_admin)
        action.move_to_element(last_comment).perform()
        self.driver.find_element(By.XPATH, self.delete_icon_xpath).click()
        self.driver.find_element(By.XPATH, self.delete_button_xpath).click()

    def get_comment_admin_id(self):
        """
        This function gets the id of the last comment in the admin page
        :return: It returns the id of the last comment in the admin page
        """
        last_comment = self.driver.find_element(By.XPATH, self.last_comment_xpath_for_id)
        admin_comment_id = last_comment.get_attribute("data-commentid")
        return "c" + admin_comment_id

    def get_comment_guest_id(self):
        """
        This function gets the id of the last comment in the guest page
        :return: It returns the id of the last comment in the guest page
        """
        gp = GuestPage(self.driver)
        self.driver.find_element(By.XPATH, gp.a_comment_xpath).click()
        comments_list = gp.check_comments()
        if len(comments_list) > 0:
            comment_id_with_c = comments_list[-1].get_attribute("id")
        else:
            comment_id_with_c = None

        return comment_id_with_c
