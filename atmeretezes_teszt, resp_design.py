from selenium import webdriver
import time

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/responsive-table.html")
    driver.set_window_size(800, 1080)
    size = driver.get_window_size()
    print("Window size: width = {}px, height = {}px.".format(size["width"], size["height"]))
    time.sleep(2.0)
    driver.set_window_size(240, 1080)
    size = driver.get_window_size()
    print("Window size: width = {}px, height = {}px.".format(size["width"], size["height"]))
    time.sleep(2.0)
finally:
    driver.close()
