import os
from selenium import webdriver
import time

driver = webdriver.Chrome() # executable need to be in path
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(5)
print(driver.find_element_by_id("content").text)
driver.close()
