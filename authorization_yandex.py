from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

options = Options()
options.page_load_strategy = 'none'
browser_emulator = Chrome(options=options)
browser_emulator.get("https://passport.yandex.ru/auth")

def wait_element(by: By, value: str):
    try:
        return WebDriverWait(browser_emulator, 1).until(lambda browser_emulator: browser_emulator.find_element(by, value))
    except TimeoutException:
        return None

def entering_form(user_possible_input: str) -> str: 
    input_box = wait_element(By.CLASS_NAME, "Textinput-Control")
    enter_button = wait_element(By.ID, "passp:sign-in")
    
    input_box.send_keys(Keys.CONTROL + "A")
    input_box.send_keys(Keys.DELETE)
    input_box.send_keys(user_possible_input)
    enter_button.click()

    input_hint = wait_element(By.CLASS_NAME, "Textinput-Hint")
    if input_hint == None:
        return "Все указано верно"
    else:    
        return input_hint.text