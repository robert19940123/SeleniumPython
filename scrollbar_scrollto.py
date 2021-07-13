from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/general.html")

    # html = driver.find_element_by_tag_name("html") # lehet így is, js nélkül, gombok használatával - END, SCR UP/DOWN
    # html.send_keys(Keys.END)
    # js = "window.scrollTo(0, 2000);" # leteker 2000-nyi értéket
    js = "window.scrollTo(0, document.body.scrollHeight);"  # letekerünk az oldal aljára
    driver.execute_script(js)
    time.sleep(3.0)
finally:
    driver.close()
