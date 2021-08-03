# TC_017 teszteset

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import locators

# Headless mode
opt = Options()
opt.headless = True

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)

# Conduit megnyit�sa
driver.get(locators.CON_URL)
time.sleep(2)


def test_logout():
    # Sign in gombra kattint�s
    driver.find_element_by_xpath(locators.sign_in_x).click()
    time.sleep(2)

    # Bejelentkez�si adatok kitolt�se
    driver.find_element_by_xpath(locators.si_email_x).send_keys('testuser5@example.com')
    driver.find_element_by_xpath(locators.si_password_x).send_keys('Abcd123$')
    driver.find_element_by_xpath(locators.sign_in_button_x).click()
    time.sleep(2)

    assert (driver.find_element_by_xpath(locators.user_x).text == 'testuser5')

    # Kijelentkez�s

    target_link = driver.find_element_by_xpath(locators.user_x)
    driver.find_element_by_xpath(locators.log_out_x).click()
    time.sleep(2)

    # Kijelentkez�s ellen�rz�se
    links = driver.find_elements_by_xpath("//a[starts-with(@class, 'nav-link')]")

    assert (target_link not in links)

    driver.close()
