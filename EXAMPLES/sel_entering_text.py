#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")


WIKI_URL = 'http://en.wikipedia.org/wiki'

browser = webdriver.Chrome(options=chrome_options)

browser.get(WIKI_URL)

search_field = browser.find_element_by_id('searchInput') # <1>

search_field.send_keys('monty python' + Keys.ENTER) # <2>
browser.implicitly_wait(5) # <3>

links = browser.find_elements_by_tag_name('a') # <4>

link_count = len(links)
print("There were {0} links on the page".format(link_count))


browser.close()
