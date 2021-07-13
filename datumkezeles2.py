from datetime import datetime, date, time, timezone
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://localhost:9999/forms.html")

nowutc = datetime.now(timezone.utc)
print(nowutc)
# hh/nn/eeee
time.sleep(2.0)
driver.find_element_by_id("example-input-date").send_keys(nowutc.strftime("00%Y/%m/%d"))
