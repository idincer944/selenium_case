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
        self.driver.find_element(By.XPATH, self.nvgtr_comments_xpath).click()

    def check_comment_admin_page(self):
        last_comment = self.driver.find_element(By.XPATH, self.last_comment_xpath_admin)
        return last_comment

    def click_delete_comment(self):
        action = ActionChains(self.driver)
        last_comment = self.driver.find_element(By.XPATH, self.last_comment_xpath_admin)
        action.move_to_element(last_comment).perform()
        self.driver.find_element(By.XPATH, self.delete_icon_xpath).click()
        self.driver.find_element(By.XPATH, self.delete_button_xpath).click()

    def click_guest_page_comment(self):
        self.driver.find_element(By.XPATH, self.guest_page_comment_button_xpath)

    def get_comment_admin_id(self):
        last_comment = self.driver.find_element(By.XPATH, self.last_comment_xpath_for_id)
        admin_comment_id = last_comment.get_attribute("data-commentid")
        return admin_comment_id

    def get_comment_guest_id(self): #Kullanmıyorum--
        gp = GuestPage(self.driver)
        self.driver.find_element(By.XPATH, gp.a_comment_xpath).click()
        last_comment = gp.check_comments()
        comment_id_with_c = last_comment.get_attribute("id")
