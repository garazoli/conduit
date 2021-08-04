# TC_025 teszteset

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import csv
import time
import locators

# Headless mode
opt = Options()
opt.headless = True

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)

# Conduit megnyitása
driver.get(locators.CON_URL)
time.sleep(10)


def test_pagination():
    # Bejelentkezés
    # Sign in gombra kattintás
    driver.find_element_by_xpath(locators.sign_in_x).click()
    time.sleep(10)

    # Bejelentkezési adatok kitöltése
    driver.find_element_by_xpath(locators.si_email_x).send_keys('testuser2@example.com')
    driver.find_element_by_xpath(locators.si_password_x).send_keys('Abcd123$')
    driver.find_element_by_xpath(locators.sign_in_button_x).click()
    time.sleep(10)

    driver.find_element_by_xpath(locators.new_article_x).click()
    time.sleep(10)

    # Postok feltöltése fileból, hogy lapozható felületet kapjak:
    # A postok címe mindegyik esetben más, hogy az esetleges ismétlődések kiszűrhetőek legyenek.
    with open('selenium_tests/pagination_data_in.csv', encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';')
        next(csvreader)

        for row in csvreader:
            driver.find_element_by_xpath(locators.title_x).send_keys(row[0])
            driver.find_element_by_xpath(locators.about_x).send_keys(row[1])
            driver.find_element_by_xpath(locators.article_x).send_keys(row[2])
            driver.find_element_by_xpath(locators.tag_x).send_keys(row[3])
            time.sleep(5)
            driver.find_element_by_xpath(locators.publish_button_x).click()
            time.sleep(5)
            driver.find_element_by_xpath(locators.new_article_x).click()
            time.sleep(5)

    # A felhasználó oldarára navigálás
    driver.find_element_by_xpath(locators.user_x).click()
    time.sleep(10)

    # Lapozó hivatkozások kigyűjtése
    page_links = driver.find_elements_by_xpath('//a[@class="page-link"]')

    # Ebbe a listába gyűjtöm a különféle lepokon található címeket
    titles_list = []

    for link in page_links:
        link.click()
        time.sleep(5)
        titles = driver.find_elements_by_xpath('//h1')
        for title in titles:
            titles_list.append(title.text)

    # A lapokról összegyűjtött címek listájának hosszának,
    # és az ismétlődések nélküli lista hosszának kellene megegyeznie,
    # ez mutatná, hogy a lapozófelület megfelelően működik.

    print(len(titles_list))  # Az összes összegyűjtött cím
    print(len(set(titles_list)))  # Ennyinek kellene látszódnia összesen
    assert len(titles_list) == len(set(titles_list))

    driver.close()
