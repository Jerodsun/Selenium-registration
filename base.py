from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

from secrets import netid, password

start_url = "https://myaccess.georgetown.edu/pls/bninbp/twbkwbis.P_WWWLogin"
term = "Fall 2019"


# Implicit waits may work well

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(2)
driver.get(start_url)

elem = driver.find_element_by_id("UserID")
elem.clear()
elem.send_keys(netid)

password_form = driver.find_element_by_name("PIN")
password_form.send_keys(password)

enter_key = driver.find_element_by_id("id____UID0")
enter_key.click()

# Enter new page

services_link = driver.find_element_by_id("bmenu--P_StuMainMnu___UID1")
services_link.click()

registration_link = driver.find_element_by_id("bmenu--P_RegMnu___UID0")
registration_link.click()

registration_final = driver.find_element_by_id("contentItem13")
registration_final.click()

# Enter Registration select term

term_select = driver.find_element_by_id("term_id")
term_select.send_keys(term)

submit_button = driver.find_element_by_id("id____UID6")
submit_button.click()

# Assuming we already did the initial registration things and now are in "Add or Drop Classes"
