#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")


WIKI_URL = 'http://en.wikipedia.org/wiki'

browser = webdriver.Chrome(options=chrome_options)
browser.get(WIKI_URL) # Load page

search_field = browser.find_element_by_id('searchInput')

search_field.send_keys('monty python' + Keys.ENTER)
browser.implicitly_wait(3)

try:
    idle_link = browser.find_element_by_partial_link_text('Eric Idle') # <1>
    print(idle_link.text, idle_link.tag_name)
    idle_link.click() # <2>
except NoSuchElementException as err:
    print(err)

browser.close()
