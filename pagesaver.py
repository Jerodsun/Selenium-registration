from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


import time
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()

print("now =", now)

name = now.strftime("metabase_%Y%m%d_%H%M.png")

print("date and time =", name)	


# from secrets import netid, password, class_list

start_url = "http://104.131.48.154:3000/public/dashboard/e65fcfcb-70a4-4d86-b7fb-888057c67881"

chrome_options = Options()
chrome_options.add_argument("--window-size=3840,2160") # width, height

driver = webdriver.Chrome("./chromedriver", chrome_options=chrome_options)

# driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get(start_url)

time.sleep(60)

driver.save_screenshot(name)

# mime_types = "application/pdf,application/vnd.adobe.xfdf,application/vnd.fdf,application/vnd.adobe.xdp+xml"

# fp = webdriver.FirefoxProfile()
# fp.set_preference("browser.download.folderList", 2)
# fp.set_preference("browser.download.manager.showWhenStarting", False)
# fp.set_preference("browser.download.dir", "/home/aafanasiev/Downloads")
# fp.set_preference("browser.helperApps.neverAsk.saveToDisk", mime_types)
# fp.set_preference("plugin.disable_full_page_plugin_for_types", mime_types)
# fp.set_preference("pdfjs.disabled", True)

# browser = webdriver.Firefox() # firefox_profile=fp)
# browser.get("http://104.131.48.154:3000/public/dashboard/e65fcfcb-70a4-4d86-b7fb-888057c67881")

# webobj_get_link = browser.find_element_by_id("liSavePdf")
# webobj_get_object = webobj_get_link.find_element_by_tag_name("a")
# webobj_get_object.click()