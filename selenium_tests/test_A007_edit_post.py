# TC_016 teszteset

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import csv
import locators

# Headless mode
opt = Options()
opt.headless = True

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)

# Conduit megnyitása
driver.get(locators.CON_URL)


def test_edit_post():
    # Bejelentkezés
    # Sign in gombra kattintás
    driver.find_element_by_xpath(locators.sign_in_x).click()
    driver.implicitly_wait(10)

    # Bejelentkezési adatok kitöltése
    driver.find_element_by_xpath(locators.si_email_x).send_keys('testuser1@example.com')
    driver.find_element_by_xpath(locators.si_password_x).send_keys('Abcd123$')
    driver.find_element_by_xpath(locators.sign_in_button_x).click()
    driver.implicitly_wait(20)

    def fill_and_clear_form(xpath):
        element = driver.find_element_by_xpath(xpath)
        element.clear()
        return element

    with open('selenium_tests/edit_data_in.csv', encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';')
        next(csvreader)

        for row in csvreader:
            driver.find_element_by_xpath(locators.user_x).click()
            driver.implicitly_wait(20)
            driver.find_element_by_xpath(locators.first_post_x).click()
            driver.implicitly_wait(20)
            driver.find_element_by_xpath(locators.edit_button_x).click()
            driver.implicitly_wait(20)
            fill_and_clear_form(locators.title_x).send_keys(row[0])
            fill_and_clear_form(locators.about_x).send_keys(row[1])
            fill_and_clear_form(locators.article_x).send_keys(row[2])
            driver.find_element_by_xpath(locators.publish_button_x).click()
            driver.implicitly_wait(20)

    driver.find_element_by_xpath(locators.user_x).click()
    driver.implicitly_wait(20)

    with open('selenium_tests/edit_data_out.csv', 'w', encoding='UTF-8') as f:
        f.write('Title;About;Article' + '\n')

    def collect_edited_posts_and_write_to_file(l_index):
        edited_titles_list = driver.find_elements_by_xpath('//h1')
        edited_abouts_list = driver.find_elements_by_xpath('//a/p')
        edited_title = edited_titles_list[l_index].text
        edited_about = edited_abouts_list[l_index].text

        edited_titles_list[l_index].click()
        driver.implicitly_wait(20)

        edited_article = driver.find_element_by_xpath('//p').text

        edited_data = [edited_title, edited_about, edited_article]

        with open('selenium_tests/edit_data_out.csv', 'a', encoding='UTF-8') as file:
            file.write(';'.join(edited_data) + '\n')

        driver.find_element_by_xpath(locators.user_x).click()
        driver.implicitly_wait(20)

    collect_edited_posts_and_write_to_file(-3)
    collect_edited_posts_and_write_to_file(-2)
    collect_edited_posts_and_write_to_file(-1)

    driver.close()
