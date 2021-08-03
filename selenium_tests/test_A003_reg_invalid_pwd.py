# TC_003 teszteset

import random
import string

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import locators

# Headless mode
opt = Options()
opt.headless = True

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)

# Conduit megnyitása
driver.get(locators.CON_URL)
driver.implicitly_wait(10)


def test_reg_pwd():
    # Random username és email generálás
    class MyRND:
        chars = string.ascii_lowercase

        @classmethod
        def uname(cls):
            return "".join([random.choice(cls.chars) for _ in range(8)])

    random_user = MyRND.uname()

    # Sign up gombra kattintás
    driver.find_element_by_xpath(locators.sign_up_x).click()
    driver.implicitly_wait(10)

    # Kitöltendő mezők kinyerése
    username = driver.find_element_by_xpath(locators.username_x)
    email = driver.find_element_by_xpath(locators.email_x)
    password = driver.find_element_by_xpath(locators.password_x)
    sign_up_button = driver.find_element_by_xpath(locators.sign_up_button_x)
    driver.implicitly_wait(10)

    # Mezők kitöltése tesztadatokkal
    username.send_keys(random_user)
    email.send_keys(random_user + '@example.com')
    password.send_keys('1234')
    sign_up_button.click()
    driver.implicitly_wait(10)

    # A regisztráció sikerességének ellenőrzése
    assert (driver.find_element_by_xpath(
        locators.reg_fail_message_x).text == 'Password must be 8 characters long and include 1 number, 1 uppercase '
                                                'letter, and 1 lowercase letter.')

    driver.close()
