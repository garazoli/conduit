# TC_009 teszteset

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import csv
import time

# Headless mode
opt = Options()
opt.headless = True

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)

# Conduit megnyitása
driver.get("http://localhost:1667")
driver.maximize_window()
driver.implicitly_wait(3)


def test_new_post():
    # Bejelentkezés
    # Sign in gombra kattintás
    driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a').click()
    driver.implicitly_wait(3)

    # Bejelentkezési adatok kitöltése
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input').send_keys(
        'testuser1@example.com')
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input').send_keys('Abcd123$')
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button').click()
    driver.implicitly_wait(3)

    new_article = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a')
    new_article.click()
    driver.implicitly_wait(3)

    a_title = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input')
    a_about = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input')
    a_article = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[3]/textarea')
    a_tag = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li/input')

    with open('selenium_tests/data_in.csv', encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';')
        next(csvreader)

        for row in csvreader:
            a_title.send_keys(row[0])
            a_about.send_keys(row[1])
            a_article.send_keys(row[2])
            a_tag.send_keys(row[3])
            driver.implicitly_wait(3)
            driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button').click()
            driver.implicitly_wait(3)
            new_article.click()
            driver.implicitly_wait(3)

    driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[1]/a').click()
    driver.implicitly_wait(3)

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
        with open('selenium_tests/data_in.csv', encoding='UTF-8') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=';')
            next(csvreader)
            for row in csvreader:
                data_list.append(row[data_list_row])

        assert (data_list == posted_list)

    assert_data(0, titles_list, posted_titles_list)
    assert_data(1, about_list, posted_about_list)
    assert_data(3, tag_list, posted_tag_list)

    driver.close()
