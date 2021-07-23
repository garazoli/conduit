from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = True

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)

# Conduit megnyitása
driver.get("http://localhost:1667")
driver.maximize_window()
time.sleep(2)


def test_login():
    # Sign in gombra kattintás
    driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a').click()
    time.sleep(2)

    # Bejelentkezési adatok kitöltése
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input').send_keys(
        'testuser1@example.com')
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input').send_keys('Abcd123$')
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button').click()
    time.sleep(2)

    assert (driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a').text == 'testuser1')

    driver.close()
