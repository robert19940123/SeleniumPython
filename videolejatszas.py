from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/videos.html")
    video = driver.find_element_by_id("html5video")
    video.click()
    video.send_keys(Keys.SPACE)
    time.sleep(4.0)
    video.screenshot('video_srcshot.png')
    time.sleep(5.0)

finally:
    driver.close()
