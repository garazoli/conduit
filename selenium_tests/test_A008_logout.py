# TC_017 teszteset

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Headless mode
opt = Options()
opt.headless = True

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)

# Conduit megnyit�sa
driver.get("http://localhost:1667")
time.sleep(2)


def test_logout():
    # Sign in gombra kattint�s
    driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a').click()
    time.sleep(2)

    # Bejelentkez�si adatok kitolt�se
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input').send_keys(
        'testuser1@example.com')
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input').send_keys('Abcd123$')
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button').click()
    time.sleep(2)

    assert (driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a').text == 'testuser1')

    # Kijelentkez�s

    target_link = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a')
    driver.find_element_by_xpath("//a/i[@class='ion-android-exit']").click()
    time.sleep(2)

    # Kijelentkez�s ellen�rz�se
    links = driver.find_elements_by_xpath("//a[starts-with(@class, 'nav-link')]")

    assert (target_link not in links)
