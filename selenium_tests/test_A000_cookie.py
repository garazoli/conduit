# TC_000 teszteset

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import locators

# Headless mode
opt = Options()
opt.headless = True

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)

# Conduit megnyitása
driver.get(locators.CON_URL)
time.sleep(5)


def test_cookies():
    # A cookie policy panel megjelenésének ellnőrzése:
    assert driver.find_element_by_id(locators.cookie_panel).is_displayed()

    # Cookie-k elfogadása
    driver.find_element_by_xpath(locators.cookie_accept_btn).click()
    time.sleep(5)

    # Újbóli megnyitáskor a cookie elfogdó/elutasító gombok nemlétének ellenőrzése
    # (csak ez a két gomb van a bejelentkező képernyőn):

    driver.refresh()
    time.sleep(5)

    buttons = driver.find_elements_by_xpath('//button')
    assert buttons == []

    driver.close()
