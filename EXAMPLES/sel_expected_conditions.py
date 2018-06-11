#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(options=chrome_options)

driver.get("http://www.google.com")


print("Original title:", driver.title) # <1>


inputElement = driver.find_element_by_name("q") # <2>


inputElement.send_keys("monty python") # <3>

inputElement.submit() # <4>

try:

    WebDriverWait(driver, 10).until(EC.title_contains("monty python")) # <5>

    print("Final title:", driver.title) # <6>

finally:
    driver.quit()
