# TC_017 teszteset

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
    # Sign in gombra kattintás
    driver.find_element_by_xpath(locators.sign_in_x).click()
    time.sleep(2)

    # Bejelentkezési adatok kitoltése
    driver.find_element_by_xpath(locators.si_email_x).send_keys(
        'testuser1@example.com')
    driver.find_element_by_xpath(locators.si_password_x).send_keys('Abcd123$')
    driver.find_element_by_xpath(locators.sign_in_button_x).click()
    time.sleep(2)

    assert (driver.find_element_by_xpath(locators.user_x).text == 'testuser1')

    # Kijelentkezés

    target_link = driver.find_element_by_xpath(locators.user_x)
    driver.find_element_by_xpath(locators.log_out_x).click()
    time.sleep(2)

    # Kijelentkezés ellenőrzése
    links = driver.find_elements_by_xpath("//a[starts-with(@class, 'nav-link')]")

    assert (target_link not in links)

finally:
    driver.close()
