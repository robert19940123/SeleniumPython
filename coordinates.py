from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/dragndrop3.html")
    draggable = driver.find_element_by_id("dragThis")
    ActionChains(driver).drag_and_drop_by_offset(draggable,
                                                 draggable.location["x"] + 350,
                                                 draggable.location["y"] + 350).perform()
    time.sleep(3.0)

finally:
    driver.close()
