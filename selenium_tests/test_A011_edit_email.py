# TC_021 teszteset

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import locators

# Headless mode
opt = Options()
opt.headless = True

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)

# Conduit megnyitasa
driver.get(locators.CON_URL)
time.sleep(10)


def test_edit_email():
    # Sign in gombra kattintas
    driver.find_element_by_xpath(locators.sign_in_x).click()
    time.sleep(10)

    # Bejelentkezesi adatok kitoltese
    driver.find_element_by_xpath(locators.si_email_x).send_keys('testuser2@example.com')
    driver.find_element_by_xpath(locators.si_password_x).send_keys('Abcd123$')
    driver.find_element_by_xpath(locators.sign_in_button_x).click()
    time.sleep(10)

    # Email megvatoztatasa
    driver.find_element_by_xpath(locators.settings_x).click()
    time.sleep(10)
    driver.find_element_by_xpath(locators.new_email_x).clear()
    driver.find_element_by_xpath(locators.new_email_x).send_keys('newemail@example.com')
    driver.find_element_by_xpath(locators.update_button_x).click()
    time.sleep(10)

    assert driver.find_element_by_xpath(locators.update_success_x).text == 'Update successful!'

    driver.find_element_by_xpath(locators.update_ok_button_x).click()
    time.sleep(10)

    new_email_value = driver.find_element_by_xpath(locators.new_email_x).get_attribute('value')
    print(new_email_value)
    assert new_email_value == 'newemail@example.com'

    # Eredeti allapot visszaallitasa nem szukseges, mert a teszteset elbukott...

    driver.close()
