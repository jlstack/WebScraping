__author__ = 'lukestack'
from selenium import webdriver
import time
from datetime import datetime, timedelta

USERNAME = ''
PASSWORD = ''
REGISTERPIN = ''
SEMESTER = 'Fall 2015'
CRNS = ["11156", "10387", "16238", "10383", "10384", "10658", "13435"] # max 10 CRNS
REGISTERDATE = datetime(2015, 3, 30, 1, 40) # datetime('Year', 'Month', 'Date', 'Hour(0-23)', 'Minute')
present = datetime.now()
while present.date() < REGISTERDATE.date():
    time.sleep(60 * 15) # sleeps for 15 minutes
    present = datetime.now()
while present.time() < REGISTERDATE.time():
    time.sleep(1) # sleeps for 1 second before checking again
    present = datetime.now()
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
    browser.find_element_by_xpath("//*[@id='term_id']/option[contains(text(),'" + SEMESTER + "')]").click()
    browser.find_element_by_xpath("//input").click()
    browser.find_element_by_xpath("//input").send_keys(REGISTERPIN)
    browser.find_element_by_xpath("//input[contains(@type, 'submit')]").click()
    crn_inputs = browser.find_elements_by_xpath("//input[contains(@id, 'crn_id')]")
    print crn_inputs
    for i in range(len(CRNS)):
        crn_inputs[i].send_keys(CRNS[i])
    browser.find_element_by_xpath("/html/body/div[3]/form/input[contains(@value, 'Submit Changes')]").click()
    time.sleep(5)
    browser.close()
except:
    pass