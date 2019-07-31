from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

from secrets import netid, password

start_url = "https://myaccess.georgetown.edu/pls/bninbp/twbkwbis.P_WWWLogin"
term = "Fall 2019"

driver = webdriver.Chrome("./chromedriver")
driver.get(start_url)

elem = driver.find_element_by_id("UserID")
elem.clear()
elem.send_keys(netid)

password_form = driver.find_element_by_name("PIN")
password_form.send_keys(password)

enter_key = driver.find_element_by_id("id____UID0")
enter_key.click()

# Later move to explicit waits
time.sleep(1)

services_link = driver.find_element_by_id("bmenu--P_StuMainMnu___UID1")
services_link.click()

time.sleep(1)

registration_link = driver.find_element_by_id("bmenu--P_RegMnu___UID0")
registration_link.click()

time.sleep(1)

registration_final = driver.find_element_by_id("contentItem13")
registration_final.click()

time.sleep(1)

term_select = driver.find_element_by_id("term_id")
term_select.send_keys(term)

submit_button = driver.find_element_by_id("id____UID6")
submit_button.click()

input()