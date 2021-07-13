from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/twitter.html")

text1 = "mind1"
post = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div/div/div[2]/textarea")
post.send_keys(text1)

butt1 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div[2]/button").click()


like = driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div/div[1]/ul/div[1]/li/div/div[2]/div[4]/div[4]/div/svg/path")


