# TC_009 teszteset

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import csv
import time

# Headless mode
opt = Options()
opt.headless = False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)

# Conduit megnyitása
driver.get("http://localhost:1667")
time.sleep(2)


try:
    # Bejelentkezés
    # Sign in gombra kattintás
    driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a').click()
    time.sleep(2)

    # Bejelentkezési adatok kitöltése
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input').send_keys(
        'testuser1@example.com')
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input').send_keys('Abcd123$')
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button').click()
    time.sleep(2)

    driver.find_element_by_xpath('//a[@href="#/editor"]').click()
    time.sleep(2)

    with open('post_data_in.csv', encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';')
        next(csvreader)

        for row in csvreader:
            driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input').send_keys(
                row[0])
            driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input').send_keys(
                row[1])
            driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[3]/textarea').send_keys(
                row[2])
            driver.find_element_by_xpath(
                '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li/input').send_keys(row[3])
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button').click()
            time.sleep(2)
            driver.find_element_by_xpath('//a[@href="#/editor"]').click()
            time.sleep(2)

    driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[1]/a').click()
    time.sleep(2)

    posted_titles = driver.find_elements_by_xpath('//h1')
    posted_about = driver.find_elements_by_xpath('//a/p')
    posted_tag = driver.find_elements_by_xpath('//a/div/a')

    posted_titles_list = [posted_titles[-3].text, posted_titles[-2].text, posted_titles[-1].text]
    posted_about_list = [posted_about[-3].text, posted_about[-2].text, posted_about[-1].text]
    posted_tag_list = [posted_tag[-3].text, posted_tag[-2].text, posted_tag[-1].text]

    titles_list = []
    about_list = []
    tag_list = []

    def assert_data(data_list_row, data_list, posted_list):
        with open('post_data_in.csv', encoding='UTF-8') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=';')
            next(csvreader)
            for row in csvreader:
                data_list.append(row[data_list_row])
            assert (data_list == posted_list)

    assert_data(0, titles_list, posted_titles_list)
    assert_data(1, about_list, posted_about_list)
    assert_data(3, tag_list, posted_tag_list)

finally:
    driver.close()
