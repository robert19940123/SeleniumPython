import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://react-card-2a6c5.web.app/")


time.sleep(2.0)
t_shirt = driver.find_elements_by_class_name("shelf-item__buy-btn")

for x in t_shirt:
    x.click()
