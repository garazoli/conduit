# TC_020 teszteset

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


def test_edit_password():
    # Sign in gombra kattintas
    driver.find_element_by_xpath(locators.sign_in_x).click()
    time.sleep(10)

    # Bejelentkezesi adatok kitoltese
    def sign_in(email, password):
        driver.find_element_by_xpath(locators.si_email_x).send_keys(email)
        driver.find_element_by_xpath(locators.si_password_x).send_keys(password)
        driver.find_element_by_xpath(locators.sign_in_button_x).click()
        time.sleep(10)

    sign_in('testuser3@example.com', 'Abcd123$')

    # Jelszo megvatoztatasa
    def edit_settings(password):
        driver.find_element_by_xpath(locators.settings_x).click()
        time.sleep(10)
        driver.find_element_by_xpath(locators.new_password_x).send_keys(password)
        driver.find_element_by_xpath(locators.update_button_x).click()
        time.sleep(10)

    edit_settings('Efgh456$')

    assert driver.find_element_by_xpath(locators.update_success_x).text == 'Update successful!'

    driver.find_element_by_xpath(locators.update_ok_button_x).click()
    time.sleep(10)

    # Logout es bejelentkezes az uj jelszoval

    driver.find_element_by_xpath(locators.log_out_x).click()
    time.sleep(10)

    driver.find_element_by_xpath(locators.sign_in_x).click()
    time.sleep(10)

    # Bejelentkezes uj adatokkal
    sign_in('testuser3@example.com', 'Efgh456$')

    assert driver.find_element_by_xpath(locators.user_x).text == 'testuser3'

    # Eredeti allapot visszaallitasa:

    edit_settings('Abcd123$')

    assert driver.find_element_by_xpath(locators.update_success_x).text == 'Update successful!'

    driver.find_element_by_xpath(locators.update_ok_button_x).click()

    driver.close()
