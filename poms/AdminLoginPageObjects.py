from selenium.webdriver.common.by import By


class LoginPage:
    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Locators
    button_sign_in_xpath = "//a[@class='sign-in ga-header-sign-in']"
    txtbox_email_id = "identifierId"
    txtbox_password_name = "Passwd"
    button_next_xpath = "//*[@id='identifierNext']/div/button"
    button_login_xpath = "//*[@id='passwordNext']/div/button"

    # Action Methods
    def click_sign_in(self):
        self.driver.find_element(By.XPATH, self.button_sign_in_xpath).click()

    def set_email(self, email):
        """
        This function types email into email text box
        :param email:
        """
        email_txt = self.driver.find_element(By.ID, self.txtbox_email_id)
        email_txt.clear()
        email_txt.send_keys(email)

    def click_next(self):
        self.driver.find_element(By.XPATH, self.button_next_xpath).click()

    def set_password(self, password):
        password_txt = self.driver.find_element(By.NAME, self.txtbox_password_name)
        password_txt.clear()
        password_txt.send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()


