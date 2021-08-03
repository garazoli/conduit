# TC_014 teszteset

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import locators
import time
# Headless mode
opt = Options()
opt.headless = True

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)

# Conduit megnyitása
driver.get(locators.CON_URL)
driver.implicitly_wait(10)


def test_del_post():
    # Sign in gombra kattintás
    driver.find_element_by_xpath(locators.sign_in_x).click()
    time.sleep(20)

    # Bejelentkezési adatok kitöltése
    driver.find_element_by_xpath(locators.si_email_x).send_keys('testuser1@example.com')
    driver.find_element_by_xpath(locators.si_password_x).send_keys('Abcd123$')
    driver.find_element_by_xpath(locators.sign_in_button_x).click()
    time.sleep(20)

    # Törölni kívánt bejegyzés kiválasztása és törlése
    driver.find_element_by_xpath(locators.user_x).click()
    time.sleep(20)
    title_post = driver.find_element_by_xpath(locators.first_post_x)  # Az első elem címe
    title_post.click()
    time.sleep(20)
    driver.find_element_by_xpath(locators.delete_button_x).click()
    time.sleep(20)

    # Elem törlésének ellenőrzése:
    driver.find_element_by_xpath(locators.user_x).click()  # Visszanavigálás a saját postok közé
    time.sleep(20)
    title_next_post = driver.find_element_by_xpath(locators.first_post_x)  # Az első elem címe a törlés után

    assert (title_post != title_next_post)

    driver.close()
