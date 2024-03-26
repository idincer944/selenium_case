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
        """
        This function clicks signin button
        """
        self.driver.find_element(By.XPATH, self.button_sign_in_xpath).click()

    def set_email(self, email):
        """
        This function types email into email text box
        :param email: This parameter is the user email used for signin/login
        """
        email_txt = self.driver.find_element(By.ID, self.txtbox_email_id)
        email_txt.clear()
        email_txt.send_keys(email)

    def click_next(self):
        """
        This function email clicks the next button after entering email
        """
        self.driver.find_element(By.XPATH, self.button_next_xpath).click()

    def set_password(self, password):
        """
        This function enters password into password text box
        :param password: This parameter is the user password used for signin/login
        """
        password_txt = self.driver.find_element(By.NAME, self.txtbox_password_name)
        password_txt.clear()
        password_txt.send_keys(password)

    def click_login(self):
        """
        This function email clicks the next button after entering password. Since both buttons are named 'next' in the
        website, this one is called 'click_login' to avoid duplicate function names
        """
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()


