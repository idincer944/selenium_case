import time
import pyperclip
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddPost:
    # Locators
    button_newpost_xpath = "//*[@id='yDmH0d']/c-wiz/div[1]/gm-raised-drawer/div/div[2]/div/c-wiz/div[3]/div/div"
    txtbox_post_xpath = "(//body)[1]"
    button_add_img_xpath = ("/html[1]/body[1]/div[7]/c-wiz[2]/div[1]/c-wiz[1]/div[1]/div[2]/div[1]/div[1]/div[3]/span["
                            "1]/div[1]/div[1]/div[1]/div[1]/div[16]/div[3]/div[1]/span[1]/span[1]/span[1]")
    button_by_url_xpath = "//div[@class='JPdR6b e5Emjc qjTEB']//span[@aria-label='By URL']"
    frame_img_url_xpath = "/html/body/div[11]/div[2]/div/iframe"
    txtbox_input_url_class = "picker-urlview-input"
    button_select_id = "picker:ap:0"
    button_publish_xpath = "//div[@aria-label='Publish'] //span[@class='CwaK9']"
    button_confirm_xpath = "//div[@class='XfpsVe J9fJmf']//span[@class='RveJvd snByac'][normalize-space()='Confirm']"
    post_list_class = "gNK4lf"
    delete_icon_xpath = "(//span[@class='DPvwYc'][contains(text(),'')])[2]"
    button_trash_post_xpath = "//*[@id='yDmH0d']/div[4]/div/div[2]/div[3]/div[2]/span/span"
    button_manage_xpath = "//div[@title='Manage Post List']"
    select_box_xpath = "//div[@aria-label='Select']"

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Action Methods
    def click_newpost(self):
        """
        This function clicks New Post button
        """
        self.driver.find_element(By.XPATH, self.button_newpost_xpath).click()

    def set_post(self, text):
        """
        This function enters post text into text box
        :param text: This parameter is the post text that is entered
        """
        action = ActionChains(self.driver)
        action.key_down(Keys.ARROW_DOWN).perform()
        self.driver.switch_to.frame(self.driver.find_elements(By.TAG_NAME, 'iframe')[0])
        post_text = self.driver.find_element(By.XPATH, self.txtbox_post_xpath)
        post_text.send_keys(text)

    def click_add_img(self):
        """
        This function clicks add img icon and clicks By URL
        """
        self.driver.switch_to.default_content()
        self.driver.find_element(By.XPATH, self.button_add_img_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.button_by_url_xpath).click()

    def input_url(self, img_url):
        """
        This function switches frame, enters img url into text box and clicks select button
        :param img_url: This parameter is the img url
        """
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, self.frame_img_url_xpath))
        url_txt = self.driver.find_element(By.CLASS_NAME, self.txtbox_input_url_class)
        url_txt.clear()
        pyperclip.copy(img_url)
        url_txt.send_keys(Keys.CONTROL, 'v')
        time.sleep(1)  # Explicit wait doesn't work so I add this sleep here.
        select_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.button_select_id))
        )
        select_button.click()

    def click_publish_btn(self):
        """
        This functions switches to default frame, clicks publish button and clicks confirm button
        """
        self.driver.switch_to.default_content()
        self.driver.find_element(By.XPATH, self.button_publish_xpath).click()
        self.driver.find_element(By.XPATH, self.button_confirm_xpath).click()
        time.sleep(2)

    def count_of_posts(self):
        """
        This function gets post count of the home page
        :return: It returns the length of post list
        """
        post_elements = self.driver.find_elements(By.CLASS_NAME, self.post_list_class)
        return len(post_elements)

    def get_published(self):
        """
        This function gets the text of a post and its status
        :return: It returns the text and status
        """
        post_elements = self.driver.find_elements(By.CLASS_NAME, self.post_list_class)
        return post_elements[0].text

    def click_delete_post(self):
        """
        This function gets the last post and clicks the trash bin icon to delete the post
        """
        action = ActionChains(self.driver)
        post_list = self.driver.find_elements(By.CLASS_NAME, self.post_list_class)
        action.move_to_element(post_list[0]).perform()
        self.driver.find_element(By.XPATH, self.delete_icon_xpath).click()
        self.driver.find_element(By.XPATH, self.button_trash_post_xpath).click()
        time.sleep(2)
