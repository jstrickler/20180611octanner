#!/usr/bin/env python

import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

CL_URL = 'http://raleigh.craigslist.org'

browser = webdriver.Chrome()
browser.get(CL_URL) # Load page

computers_link = browser.find_element_by_link_text('computers')
computers_link = browser.find_element_by_link_text('computers')
computers_link.click()

byowner_link = browser.find_element_by_link_text('BY-OWNER ONLY')
byowner_link.click()


query_field = browser.find_element_by_id('query')
query_field.send_keys('macbook pro' + Keys.ENTER)
browser.implicitly_wait(5)

row_elements = browser.find_elements_by_class_name('row')
for row_element in row_elements:

    result_item_link = row_element.find_element_by_class_name('txt')

    item_link = result_item_link.find_element_by_tag_name('a')

    l2_element = row_element.find_element_by_class_name('l2')
    price_element = l2_element.find_element_by_tag_name('span')
    price = price_element.text
    if price.lstrip().startswith('$'):
        print('{0:>8s} {1}'.format(price_element.text, item_link.text))

browser.close()
