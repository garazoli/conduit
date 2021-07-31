# TC_016 teszteset

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import csv
import time

# Headless mode
opt = Options()
opt.headless = True

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)

# Conduit megnyit�sa
driver.get("http://localhost:1667")


def test_edit_post():
    # Bejelentkez�s
    # Sign in gombra kattint�s
    driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a').click()
    time.sleep(2)

    # Bejelentkez�si adatok kit�lt�se
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input').send_keys(
        'testuser1@example.com')
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input').send_keys('Abcd123$')
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button').click()
    time.sleep(3)

    def fill_and_clear_form(xpath):
        element = driver.find_element_by_xpath(xpath)
        element.clear()
        return element

    with open('selenium_tests/edit_data_in.csv', encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';')
        next(csvreader)

        for row in csvreader:
            driver.find_element_by_xpath('//a[@href="#/@testuser1/"]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div[2]/div/div/div[1]/a/h1').click()
            time.sleep(2)
            driver.find_element_by_xpath("//a[@class='btn btn-sm btn-outline-secondary']").click()
            time.sleep(2)
            fill_and_clear_form('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input').send_keys(
                row[0])
            fill_and_clear_form('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input').send_keys(
                row[1])
            fill_and_clear_form('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[3]/textarea').send_keys(
                row[2])
            driver.find_element_by_xpath("//button[@type='submit']").click()
            time.sleep(2)

    driver.find_element_by_xpath('//a[@href="#/@testuser1/"]').click()
    time.sleep(2)

    with open('selenium_tests/edit_data_out.csv', 'w', encoding='UTF-8') as f:
        f.write('Title;About;Article' + '\n')

    def collect_edited_posts_and_write_to_file(l_index):
        edited_titles_list = driver.find_elements_by_xpath('//h1')
        edited_abouts_list = driver.find_elements_by_xpath('//a/p')
        edited_title = edited_titles_list[l_index].text
        edited_about = edited_abouts_list[l_index].text

        edited_titles_list[l_index].click()
        time.sleep(2)

        edited_article = driver.find_element_by_xpath('//p').text

        edited_data = [edited_title, edited_about, edited_article]

        with open('selenium_tests/edit_data_out.csv', 'a', encoding='UTF-8') as file:
            file.write(';'.join(edited_data) + '\n')

        driver.find_element_by_xpath('//a[@href="#/@testuser1/"]').click()
        time.sleep(2)

    collect_edited_posts_and_write_to_file(-3)
    collect_edited_posts_and_write_to_file(-2)
    collect_edited_posts_and_write_to_file(-1)
