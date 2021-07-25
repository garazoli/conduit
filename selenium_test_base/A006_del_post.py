# TC_014 teszteset

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Headless mode
opt = Options()
opt.headless = False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)

# Conduit megnyitása
driver.get("http://localhost:1667")
time.sleep(2)


try:
    # Sign in gombra kattintás
    driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a').click()
    time.sleep(2)

    # Bejelentkezési adatok kitöltése
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input').send_keys(
        'testuser1@example.com')
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input').send_keys('Abcd123$')
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button').click()
    time.sleep(2)

    # Törölni kívánt bejegyzés kiválasztása és törlése
    driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a').click()
    time.sleep(2)
    title_post = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div/div/div[1]/a/h1')  # Az első elem címének elmentése
    title_post.click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/span/button/span').click()
    time.sleep(2)

    # Elem törlésének ellenőrzése:
    driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a').click()  # Visszanavigálás a saját postok közé
    title_next_post = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div/div/div[1]/a/h1') # Az első elem címének elmentése a törlés után

    assert (title_post != title_next_post)

finally:
    pass
