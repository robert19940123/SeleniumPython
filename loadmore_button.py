from selenium import webdriver
import time

driver = webdriver.Chrome()

try:
    driver.get('http://localhost:9999/loadmore.html')
    load_more = driver.find_element_by_xpath('//div[@class="load-more-button"]/button')
    for i in range(5):
        time.sleep(3.0)
        images = driver.find_elements_by_xpath("//div[@class='image']")
        for j in images[-5:]:
            print(j.find_element_by_tag_name("img").get_attribute("src"))
            print(j.find_element_by_tag_name("p").text)
        load_more.click()
finally:
    driver.close()
