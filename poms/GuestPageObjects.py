import time

from selenium.webdriver.common.by import By
from configs.Config import login
from Credentials import email, password


class GuestPage:
    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Locators
    post_xpath = "//article[@role='article']"
    a_comment_xpath = "//a[@class='comment-link']"
    frame_for_button_xpath = "//iframe[@id='comment-editor']"
    button_sign_in_with_google_xpath = "//*[@id='yDmH0d']/c-wiz/div/div/c-wiz/div/div[1]"
    txtbox_comment_xpath = "//*[@id='yDmH0d']/c-wiz/div/div/c-wiz/div/div/div[2]/div[2]/div[1]/div[2]/textarea"
    button_publish_comment_xpath = "//*[@id='yDmH0d']/c-wiz/div/div/c-wiz/div/div/div[2]/div[3]/div[1]/div"
    check_comments_xpath = "//li[@class='comment']"

    # Action Methods
    def check_post(self):
        return self.driver.find_element(By.XPATH, self.post_xpath).is_displayed()

    def add_comment(self, comment):
        self.driver.find_element(By.XPATH, self.a_comment_xpath).click()
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, self.frame_for_button_xpath))
        self.driver.find_element(By.XPATH, self.button_sign_in_with_google_xpath).click()
        login(self.driver, email, password)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, self.frame_for_button_xpath))
        txtbox_comment = self.driver.find_element(By.XPATH, self.txtbox_comment_xpath)
        txtbox_comment.click()
        txtbox_comment.send_keys(comment)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.button_publish_comment_xpath).click()
        time.sleep(3)

    def check_comments(self):
        self.driver.switch_to.default_content()
        comments = self.driver.find_elements(By.XPATH, self.check_comments_xpath)
        return comments

