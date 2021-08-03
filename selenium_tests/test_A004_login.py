# TC_005 teszteset

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
driver.implicitly_wait(3)


def test_login():
    # Sign in gombra kattintás
    driver.find_element_by_xpath(locators.sign_in_x).click()
    driver.implicitly_wait(10)

    # Bejelentkezési adatok kitöltése
    driver.find_element_by_xpath(locators.si_email_x).send_keys(
        'testuser1@example.com')
    driver.find_element_by_xpath(locators.si_password_x).send_keys('Abcd123$')
    driver.find_element_by_xpath(locators.sign_in_button_x).click()
    driver.implicitly_wait(10)

    assert (driver.find_element_by_xpath(locators.user_x).text == 'testuser1')

    driver.close()
