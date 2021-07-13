from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/kitchensink.html")

    mouse_hover = driver.find_element_by_id("mousehover")
    top_menu = driver.find_element_by_xpath("//div[@class='mouse-hover-content']/a[1]")
    time.sleep(2.0)
    ActionChains(driver).move_to_element(mouse_hover).perform()  # így  egyben is lehet kezelni persze
    time.sleep(3.0)
    actions = ActionChains(driver)  # az actionchain felépítése
    actions.move_to_element(mouse_hover)
    actions.click(top_menu)
    actions.perform()  # ezzel a paranccsal fut le az Actionchain, enélkül csak fel van épitve de nem csinál semmit


finally:
    driver.close()
