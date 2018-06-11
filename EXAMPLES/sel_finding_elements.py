#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")


WIKI_URL = 'http://en.wikipedia.org/wiki'
LINKS_TO_SHOW = 20

browser = webdriver.Chrome(options=chrome_options)
browser.get(WIKI_URL) # <1>

links = browser.find_elements_by_tag_name('a') # <2>

all_links = []
for link in links: # <3>
    all_links.append( (link.text, link.get_attribute('href'))) # <4>

link_count = len(all_links)
print("There were {0} links on the page".format(link_count))

print("The first {} are:".format(LINKS_TO_SHOW))
# for i, (link_text, url) in enumerate(all_links):
for link_text, url in all_links[:LINKS_TO_SHOW]:
    print("{:20.20s} {}".format(link_text, url))


browser.close()
