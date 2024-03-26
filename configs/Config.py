import logging
import pytest
import os
from selenium import webdriver
from poms.AdminLoginPageObjects import LoginPage

link_admin = "https://www.blogger.com/about/?bpli=1"
link_guest = "https://idincer944.blogspot.com/"
img_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/NTT-Data-Logo.svg/510px-NTT-Data-Logo.svg.png"
text = ("What is Lorem Ipsum?Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum "
        "has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of "
        "type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the "
        "leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the "
        "release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing "
        "software like Aldus PageMaker including versions of Lorem Ipsum.")
edit_text = " This is my Edit........."
comment = "hello I'm a comment"
title_name = "Blogger"


def log_details():
    cwd_path = os.getcwd()
    print("Path is: ", cwd_path)
    logging.basicConfig(filename="test.log",
                        filemode="w",
                        level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s",
                        force=True)
    return logging.getLogger("selenium")


@pytest.fixture()
def setup_driver(request):
    options = send_options()
    link = request.param
    # Setting the driver path and requesting a page
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.get(link)
    driver.maximize_window()
    yield driver
    driver.close()


def login(driver, _email, _password):
    lp = LoginPage(driver)
    logger = logging.getLogger()
    logger.info(" a. Check if there is signin button")
    try:
        logger.info("  a.a. Click signin button")
        lp.click_sign_in()
    except:
        pass
    logger.info(" b. Enter email and Click next button")
    lp.set_email(_email)
    lp.click_next()
    logger.info(" c. Enter password and Click next button")
    lp.set_password(_password)
    lp.click_login()
    logger.info(" Logged in successfully!")


def send_options():
    options = webdriver.ChromeOptions()

    # Disable automatic close
    options.add_experimental_option("detach", True)

    options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"

    # Adding argument to disable the AutomationControlled flag
    options.add_argument("--disable-blink-features=AutomationControlled")

    # Exclude the collection of enable-automation switches
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    # Turn-off userAutomationExtension
    options.add_experimental_option("useAutomationExtension", False)

    return options
