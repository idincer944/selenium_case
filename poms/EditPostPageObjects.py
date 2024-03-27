import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EditPost:
    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Locators
    a_post_class = "azat"
    txtbox_post_xpath = "//*[@class='editable ']/p"
    button_publish_xpath = "/html/body/div[7]/c-wiz[2]/div/c-wiz/div/div[1]/div[2]/div[5]"
    button_confirm_xpath = "/html/body/div[7]/div[4]/div/div[2]/div[3]/div[2]"
    txtbox_title_css = "input[aria-label='Title']"

    # Action Methods
    def click_post(self):
        """
        This function clicks the last post
        """
        self.driver.find_element(By.CLASS_NAME, self.a_post_class).click()

    def edit_post(self, text):
        """
        This function enters new text into title box
        :param text: This parameter is the new text that is entered
        """
        time.sleep(3)
        post_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-label='Title']"))
        )
        post_text.clear()
        post_text.send_keys(text)

    def update_post(self):
        """
        This function clicks Update button
        """
        self.driver.find_element(By.XPATH, self.button_publish_xpath).click()
