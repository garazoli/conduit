# TC_019 teszteset

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import locators

# Headless mode
opt = Options()
opt.headless = False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)

# Conduit megnyitasa
driver.get(locators.CON_URL)
time.sleep(2)


try:
    # Sign in gombra kattintas
    driver.find_element_by_xpath(locators.sign_in_x).click()
    time.sleep(2)

    # Bejelentkezesi adatok kitoltese
    driver.find_element_by_xpath(locators.si_email_x).send_keys('testuser4@example.com')
    driver.find_element_by_xpath(locators.si_password_x).send_keys('Abcd123$')
    driver.find_element_by_xpath(locators.sign_in_button_x).click()
    time.sleep(2)

    # Felhasznalonev megvatoztatasa
    driver.find_element_by_xpath(locators.settings_x).click()
    time.sleep(2)


    def edit_settings(username):
        driver.find_element_by_xpath(locators.new_username_x).clear()
        driver.find_element_by_xpath(locators.new_username_x).send_keys(username)
        driver.find_element_by_xpath(locators.update_button_x).click()
        time.sleep(3)


    edit_settings('newtestuser')

    assert driver.find_element_by_xpath(locators.update_success_x).text == 'Update successful!'

    driver.find_element_by_xpath(locators.update_ok_button_x).click()
    time.sleep(3)

    assert driver.find_element_by_xpath(locators.user_x).text == 'newtestuser'
    assert driver.find_element_by_xpath(locators.new_username_x).get_attribute('value') == 'newtestuser'

    # Eredeti allapot visszaallitasa:

    edit_settings('testuser4')

    assert driver.find_element_by_xpath(locators.update_success_x).text == 'Update successful!'

    driver.find_element_by_xpath(locators.update_ok_button_x).click()
    time.sleep(3)

    assert driver.find_element_by_xpath(locators.user_x).text == 'testuser4'
    assert driver.find_element_by_xpath(locators.new_username_x).get_attribute('value') == 'testuser4'

finally:
    driver.close()
