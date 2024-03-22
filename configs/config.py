from selenium import webdriver
from poms.admin_login_page_objects import LoginPage

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


def login(driver, _email, _password):
    lp = LoginPage(driver)
    try:
        lp.click_sign_in()
    except:
        pass
    lp.set_email(_email)
    lp.click_next()
    lp.set_password(_password)
    lp.click_login()


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
