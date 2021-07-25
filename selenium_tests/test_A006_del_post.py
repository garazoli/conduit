# TC_014 teszteset

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Headless mode
opt = Options()
opt.headless = True

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)

# Conduit megnyitása
driver.get("http://localhost:1667")
driver.implicitly_wait(5)


def test_del_post():
    # Sign in gombra kattintás
    driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a').click()
    driver.implicitly_wait(5)

    # Bejelentkezési adatok kitöltése
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input').send_keys(
        'testuser1@example.com')
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input').send_keys('Abcd123$')
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button').click()
    driver.implicitly_wait(5)

    # Törölni kívánt bejegyzés kiválasztása és törlése
    driver.find_element_by_xpath('//a[@href="#/@testuser1/"]').click()
    driver.implicitly_wait(5)
    title_post = driver.find_element_by_xpath(
        '//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div/div/div[1]/a/h1')  # Az első elem címe
    title_post.click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//button[@class='btn btn-outline-danger btn-sm']").click()
    driver.implicitly_wait(10)

    # Elem törlésének ellenőrzése:
    driver.find_element_by_xpath('//a[@href="#/@testuser1/"]').click()  # Visszanavigálás a saját postok közé
    driver.implicitly_wait(5)
    title_next_post = driver.find_element_by_xpath(
        '//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div/div/div[1]/a/h1')  # Az első elem címe a törlés után

    assert (title_post != title_next_post)

    driver.close()
