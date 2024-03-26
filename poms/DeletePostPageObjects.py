import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class DeletePost:
    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Locators
    post_list_class = "gNK4lf"
    delete_icon_xpath = "(//span[@class='DPvwYc'][contains(text(),'')])[2]"
    button_trash_post_xpath = "//*[@id='yDmH0d']/div[4]/div/div[2]/div[3]/div[2]/span/span"
    button_manage_xpath = "//div[@title='Manage Post List']"
    select_box_xpath = "//div[@aria-label='Select']"

    # Action Models
    def click_delete_post(self):
        action = ActionChains(self.driver)
        post_list = self.driver.find_elements(By.CLASS_NAME, self.post_list_class)
        action.move_to_element(post_list[0]).perform()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.delete_icon_xpath).click()
        self.driver.find_element(By.XPATH, self.button_trash_post_xpath).click()
        time.sleep(3)


    # def click_delete_post(self):
    #     self.driver.find_element(By.XPATH, self.button_manage_xpath).click()
    #     self.driver.find_element(By.XPATH, self.select_box_xpath).click()
    #     self.driver.find_element(By.XPATH, self.delete_icon_xpath).click()
    #     time.sleep(3)
    #     self.driver.find_element(By.XPATH, self.button_trash_post_xpath).click()
    #     time.sleep(3)
