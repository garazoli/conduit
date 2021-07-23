import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
# import time

opt = Options()
opt.headless = True

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)

# Conduit megnyitása
driver.get("http://localhost:1667")
driver.maximize_window()
driver.implicitly_wait(10)

def test_reg():
    # Random username és email generálás
    class MyRND:
        chars = string.ascii_lowercase

        @classmethod
        def uname(cls):
            return "".join([random.choice(cls.chars) for _ in range(8)])

    random_user = MyRND.uname()

    # Sign up gombra kattintás
    driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[3]/a').click()
    driver.implicitly_wait(10)

    # Kitöltendő mezők kinyerése
    username = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input')
    email = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input')
    password = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[3]/input')
    sign_up_button = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button')
    driver.implicitly_wait(10)

    # Mezők kitöltése tesztadatokkal
    username.send_keys(random_user)
    email.send_keys(random_user + '@example.com')
    password.send_keys('Abcd123$')
    sign_up_button.click()
    driver.implicitly_wait(10)

    # A regisztráció sikerességének ellenőrzése
    assert (driver.find_element_by_xpath('/html/body/div[2]/div/div[3]').text == 'Your registration was successful!')

    driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div/button').click()
    driver.implicitly_wait(10)

    # Bejelentkezés után a felhasználónév ellenőrzése
    assert (driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a').text == random_user)

    driver.close()
