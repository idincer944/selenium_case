import time
import pyperclip
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class AddPost:
    # Locators
    button_newpost_xpath = "//*[@id='yDmH0d']/c-wiz/div[1]/gm-raised-drawer/div/div[2]/div/c-wiz/div[3]/div/div"
    txtbox_post_xpath = "(//body)[1]"
    button_add_img_xpath = ("/html[1]/body[1]/div[7]/c-wiz[2]/div[1]/c-wiz[1]/div[1]/div[2]/div[1]/div[1]/div[3]/span["
                            "1]/div[1]/div[1]/div[1]/div[1]/div[16]/div[3]/div[1]/span[1]/span[1]/span[1]")
    button_by_url_xpath = "//div[@class='JPdR6b e5Emjc qjTEB']//span[@aria-label='By URL']"
    txtbox_input_url_class = "picker-urlview-input"
    button_select_id = "picker:ap:0"
    button_publish_xpath = "//div[@aria-label='Publish'] //span[@class='CwaK9']"
    post_list_class = "gNK4lf"

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Action Methods
    def click_newpost(self):
        self.driver.find_element(By.XPATH, self.button_newpost_xpath).click()

    def set_post(self, text):
        action = ActionChains(self.driver)
        action.key_down(Keys.ARROW_DOWN).perform()
        time.sleep(3)
        self.driver.switch_to.frame(self.driver.find_elements(By.TAG_NAME, 'iframe')[0])
        time.sleep(3)
        post_text = self.driver.find_element(By.XPATH, self.txtbox_post_xpath)
        post_text.send_keys(text)

    def click_add_img(self):
        self.driver.switch_to.default_content()
        self.driver.find_element(By.XPATH, self.button_add_img_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_by_url_xpath).click()

    def input_url(self, img_url):
        time.sleep(3)
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "/html/body/div[11]/div[2]/div/iframe"))
        url_txt = self.driver.find_element(By.CLASS_NAME, self.txtbox_input_url_class)
        url_txt.clear()
        pyperclip.copy(img_url)
        url_txt.send_keys(Keys.CONTROL, 'v')
        time.sleep(3)
        self.driver.find_element(By.ID, self.button_select_id).click()

    def click_publish_btn(self):
        self.driver.switch_to.default_content()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.button_publish_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div[7]/div[4]/div/div[2]/div[3]/div[2]").click()
        time.sleep(3)

    def count_of_posts(self):
        post_elements = self.driver.find_elements(By.CLASS_NAME, self.post_list_class)
        if len(post_elements) > 0:
            return len(post_elements)
        else:
            return 0

    def get_published(self):
        post_elements = self.driver.find_elements(By.CLASS_NAME, self.post_list_class)
        return post_elements[0].text