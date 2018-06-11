#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.chrome.options import Options # <1>

chrome_options = Options()  # <2>
chrome_options.add_argument("--headless") # <3>
chrome_options.add_argument("--window-size=1920x1080") # <4>

WIKI_URL = 'http://en.wikipedia.org/wiki' # <5>

browser = webdriver.Chrome(options=chrome_options)  # <6>

browser.get(WIKI_URL) # <7>

print(browser.page_source[:400]) # <8>

browser.close()  # <9>
