import time
from selenium.webdriver.common.by import By


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
        time.sleep(3)
        self.driver.find_element(By.CLASS_NAME, self.a_post_class).click()

    def edit_post(self, text):
        # self.driver.switch_to.frame(self.driver.find_elements(By.TAG_NAME, 'iframe')[0])
        time.sleep(3)
        post_text = self.driver.find_element(By.CSS_SELECTOR, "input[aria-label='Title']")
        post_text.clear()
        post_text.send_keys(text)

    def update_post(self):
        self.driver.find_element(By.XPATH, self.button_publish_xpath).click()

    # def get_editted_element(self):
    #     element = self.driver.find_element(By.XPATH, self.txtbox_title_css)
    #     return element.text
