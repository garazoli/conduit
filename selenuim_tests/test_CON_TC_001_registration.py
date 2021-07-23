import time
import random
import string
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
# from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()


def test_reg():
    # Random username és email generálás
    class MyRND:
        chars = string.ascii_lowercase

        @classmethod
        def uname(cls):
            return "".join([random.choice(cls.chars) for _ in range(8)])

    random_user = MyRND.uname()

    # Conduit megnyitása
    driver.get("http://localhost:1667")

    # Sign up gombra kattintás
    driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[3]/a').click()

    # Kitöltendő mezők kinyerése
    username = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input')
    email = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input')
    password = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[3]/input')
    sign_up_button = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button')

    # Mezők kitöltése tesztadatokkal
    username.send_keys(random_user)
    email.send_keys(random_user + '@example.com')
    password.send_keys('Abcd123$')
    sign_up_button.click()
    time.sleep(2)

    # A regisztráció sikerességének ellenőrzése
    assert (driver.find_element_by_xpath('/html/body/div[2]/div/div[3]').text == 'Your registration was successful!')

    driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div/button').click()
    time.sleep(2)

    # Bejelentkezés után a felhasználónév ellenőrzése
    assert (driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a').text == random_user)

    driver.close()
