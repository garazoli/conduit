# TC_003 teszteset

import random
import string

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Headless mode
opt = Options()
opt.headless = False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)

# Conduit megnyitása
driver.get("http://localhost:1667")
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
    driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[3]/a').click()
    time.sleep(2)

    # Kitöltendő mezők kinyerése
    username = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input')
    email = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input')
    password = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[3]/input')
    sign_up_button = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button')

    # Mezők kitöltése tesztadatokkal
    username.send_keys(random_user)
    email.send_keys(random_user + '@example.com')
    password.send_keys('1234')
    sign_up_button.click()
    time.sleep(2)

    # A regisztráció sikerességének ellenőrzése
    assert (driver.find_element_by_xpath(
        '/html/body/div[2]/div/div[3]').text == 'Password must be 8 characters long and include 1 number, 1 uppercase '
                                                'letter, and 1 lowercase letter.')

finally:
    driver.close()
