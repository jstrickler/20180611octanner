#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")


WIKI_URL = 'http://en.wikipedia.org/wiki'

browser = webdriver.Chrome(options=chrome_options)
browser.get(WIKI_URL) # Load page

search_field = browser.find_element_by_id('searchInput') # <1>

search_field.send_keys('monty python' + Keys.ENTER) # <2>
browser.implicitly_wait(3) # <3>

idle_link = browser.find_element_by_link_text('Eric Idle') # <4>
idle_link.click() # <5>
browser.implicitly_wait(3) # <3>

links = browser.find_elements_by_tag_name('a') # <6>
browser.implicitly_wait(3) # <3>
links = browser.find_elements_by_tag_name('a') # <6>

all_links = []
for link in links:
    try:
        if link.text:
            all_links.append( (link.text, link.get_attribute('href')))
    except StaleElementReferenceException as err:
        pass

for target, url in all_links[:15]:
    print('{0:20.20s} {1}'.format(target, url))

browser.close()
