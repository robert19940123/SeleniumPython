# HTML4nél müködik csak !!!!!!!!!!!

from selenium import webdriver
import time
from os import getcwd

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('http://localhost:9999/dragndrop1.html')

time.sleep(2.0)

cwd = getcwd()
JS_DRAG_DROP = open(cwd + '\\drag-drop.js', 'r').read()  # ez egy js script amit magadnak kellene megirni :O
print(JS_DRAG_DROP)  # egy adott elemet egyik pontból a másikba huzni és ledobni ilyen tipusu mezőkben
source = driver.find_element_by_id("drag1")
target = driver.find_element_by_id("div2")

driver.execute_script(JS_DRAG_DROP, source, target)
driver.implicitly_wait(5.0)
