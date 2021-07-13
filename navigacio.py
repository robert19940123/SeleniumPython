from selenium import webdriver
# import time  # ha ezt berakjuk mint függvényt onnantól használható a time.sleep() nevű függvény ami adott időtartamra megállitja az weboldalt

driver = webdriver.Chrome()

def navigate_to_general_page():
    link = driver.find_element_by_xpath('//a[text()="General text and other elements"]')
    link.click()
try:
    driver.get("http://localhost:9999/")
    print(driver.current_url) #adott oldalt kiirja nekünk
    navigate_to_general_page()
    # time.sleep(1.0)
    print(driver.current_url)
    driver.back() #ez a vissza gomb a chromeban
    print(driver.current_url)
    # time.sleep(1.0)
    navigate_to_general_page()

    anchors = driver.find_elements_by_xpath('//header//small//a')

    for a in anchors:
        a.click()
        # time.sleep(1.0)
        print(driver.current_url)
    print("*" * 50) #ezt csak azért hogy lássuk a kiirt texten a terminalban hogy mikortol "nyomkodjuk" a vissza gombot
    while driver.current_url != "http://localhost:9999/": #Chrome vissza gomb nyomkodása amig egy adott oldalra nem érünk
        print(driver.current_url)
        driver.back()

finally:
    driver.close()
