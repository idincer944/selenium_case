import inspect
import logging
from datetime import datetime

import pytest
import os
from selenium import webdriver
from selenium.common import NoSuchElementException
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
edit_text = "This is my Edit........."
comment = "hello I'm a comment"
title_name = "Blogger"
path = os.getcwd()


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
    except NoSuchElementException:
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

    # Adding argument to disable the AutomationControlled flag
    options.add_argument("--disable-blink-features=AutomationControlled")

    # Exclude the collection of enable-automation switches
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    # Turn-off userAutomationExtension
    options.add_experimental_option("useAutomationExtension", False)

    return options


def take_screenshot(driver):
    time_stamp = datetime.now().strftime("%H.%M.%S")
    method = inspect.stack()[1].function
    driver.save_screenshot(f"{path}\\tmp\\screenshots\\{time_stamp}_{method}.png")
    log_details().info(f"Screen shot will be in {path}\\tmp\\screenshots as {time_stamp}_{method}.png")


def log_details():
    logging.basicConfig(filename=f"{path}\\tmp\\Test.log",
                        filemode="a",
                        level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s",
                        force=True)
    return logging.getLogger("selenium")
