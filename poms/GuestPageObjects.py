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
        """
        This function checks if there is post in guest page
        :return: It returns True if there is a post and False if there isn't
        """
        return self.driver.find_element(By.XPATH, self.post_xpath).is_displayed()

    def add_comment(self, comment):
        """
        This function,
        1. Clicks Comment button
        2. Switches to the required frame
        3. Clicks Sign In With Google button
        4. Handles login process
        5. Switches to required frame again after login
        6. Enters comment in comment text box
        7. Clicks Publish button
        :param comment: This parameter is the comment that is entered
        """
        self.driver.find_element(By.XPATH, self.a_comment_xpath).click()
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, self.frame_for_button_xpath))
        self.driver.find_element(By.XPATH, self.button_sign_in_with_google_xpath).click()
        login(self.driver, email, password)
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, self.frame_for_button_xpath))
        self.driver.find_element(By.XPATH, self.txtbox_comment_xpath).send_keys(comment)
        self.driver.find_element(By.XPATH, self.button_publish_comment_xpath).click()

    def check_comments(self):
        """
        This function switches back to default frame, stores all the comments on the page
        :return: It returns the list of all comments
        """
        self.driver.switch_to.default_content()
        comments = self.driver.find_elements(By.XPATH, self.check_comments_xpath)
        return comments
