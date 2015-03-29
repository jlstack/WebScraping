__author__ = 'lukestack'
from selenium import webdriver
import time

USERNAME = ''
PASSWORD = ''
try:
    path_to_chromedriver = '/Users/lukestack/Downloads/chromedriver' # change path as needed
    browser = webdriver.Chrome(executable_path = path_to_chromedriver)

    url = 'https://portal4.appstate.edu/cp/home/displaylogin'
    browser.get(url)
    browser.find_element_by_xpath("//*[@id='leftcol']/fieldset/form[1]/span/input").send_keys(USERNAME)
    browser.find_element_by_xpath("//*[@id='leftcol']/fieldset/form[2]/span/input[1]").send_keys(PASSWORD)
    browser.find_element_by_xpath("//*[@id='leftcol']/fieldset/p[1]/input[1]").click()
    browser.find_element_by_xpath("//*[@id='tabs_tda']/tbody/tr/td[2]/div/a").click()
    iframe = browser.find_elements_by_tag_name('iframe')[0]
    browser.switch_to.frame(iframe)
    browser.find_elements_by_xpath("//td[contains(@class, 'taboff')]")[0].click()
    browser.find_element_by_xpath("//a[contains(text(),'Registration')]").click()
    browser.find_element_by_xpath("//a[contains(text(),'Add/Drop')]").click()
    browser.find_element_by_id("term_id").click()
    browser.find_element_by_xpath("//*[@id='term_id']/option[1]").click()
    browser.find_element_by_xpath("//input").click()
    browser.find_element_by_xpath("//input").send_keys("000820")
    browser.find_element_by_xpath("//input[contains(@type, 'submit')]").click()
    """
    for result in results:
        print result.text
    """
except:
    pass
time.sleep(5)
browser.close()
