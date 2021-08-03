# TC_001 teszteset

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
driver.maximize_window()
driver.implicitly_wait(20)


def test_reg():
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
    password.send_keys('Abcd123$')
    sign_up_button.click()
    driver.implicitly_wait(30)

    # A regisztráció sikerességének ellenőrzése
    popup_text = driver.find_element_by_xpath(locators.reg_message_x)
    assert (popup_text.text == 'Welcome!')

    driver.find_element_by_xpath(locators.ok_button_x).click()
    driver.implicitly_wait(30)

    # Bejelentkezés után a felhasználónév ellenőrzése
    assert (driver.find_element_by_xpath(locators.user_x).text == random_user)

    driver.close()
