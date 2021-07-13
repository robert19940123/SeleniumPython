from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/another_form.html")

    driver.find_element_by_id("submit").click()
    time.sleep(2.0)
    msg = WebDriverWait(driver, 20).until(  # behívott fügvénnyt atadjuk a drivernek, aztan varunk 20 secet
        EC.visibility_of_element_located((By.XPATH, '//input[@id="fullname" and @name="fullname"]'))).get_attribute(
        "validationMessage")
    # majd megkeressük hogy hol helyezkedik el az inoput mező aminel a felugró ablak megjelenik és adott értékét kiolvassuk(elvileg ezeket ezzel kell)

    assert msg is not None  # ellenőrzés hogy a felugro ablak létezik
    assert msg == 'Kérjük, töltse ki ezt a mezőt.'  # felugro ablak szöveg ellenőrzése
    time.sleep(2.0)
finally:
    driver.close()
