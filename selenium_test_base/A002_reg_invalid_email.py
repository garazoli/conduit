# TC_002 teszteset

import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import locators

# Headless mode
opt = Options()
opt.headless = False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)

# Conduit megnyitása
driver.get(locators.CON_URL)
time.sleep(2)


try:
    # Random username és email generálás
    class MyRND:
        chars = string.ascii_lowercase

        @classmethod
        def uname(cls):
            return "".join([random.choice(cls.chars) for _ in range(8)])

    random_user = MyRND.uname()

    # Sign up gombra kattintás
    driver.find_element_by_xpath(locators.sign_up_x).click()
    time.sleep(2)

    # Kitöltendő mezők kinyerése
    username = driver.find_element_by_xpath(locators.username_x)
    email = driver.find_element_by_xpath(locators.email_x)
    password = driver.find_element_by_xpath(locators.password_x)
    sign_up_button = driver.find_element_by_xpath(locators.sign_up_button_x)

    # Mezők kitöltése tesztadatokkal
    username.send_keys(random_user)
    email.send_keys(random_user + 'vexample.com')
    password.send_keys('Abcd123$')
    sign_up_button.click()
    time.sleep(2)

    # A regisztráció sikerességének ellenőrzése
    assert (driver.find_element_by_xpath(locators.reg_fail_message_x).text == 'Email must be a valid email.')

finally:
    driver.close()
