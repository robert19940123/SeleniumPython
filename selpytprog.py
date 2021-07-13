from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://python.org")

q = driver.find_element_by_name("q")   #a zárójelbe beírt "q" az oldalon ennek az elementnek a name tulajdonsága (ezert is find element byname)
q.send_keys("hello")

submit = driver.find_element_by_name("submit")
submit.click()

# driver.close() #Chrome oldal bezárása automatikusan ahogyan lefutott a fájlunk
