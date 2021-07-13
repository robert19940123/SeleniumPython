import time

from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/kitchensink.html")

    name = driver.find_element_by_id("name")
    name.send_keys("Robi")
    button = driver.find_element_by_id("alertbtn")
    button.click()
    ref_text = "Hello Robi, share this practice page and share your knowledge"
    alert = driver.switch_to.alert  # ezzel a swtich_to-val tudunk átváltani a felugro ablak driverre vagy akár másik ablak driverre stb.
    assert alert.text == ref_text  # szöveget ellenőrzünk
    print(alert.text)
    time.sleep(2.0)
    alert.accept()  # a felugró ablakoknak külön van elfogadása, vagy elutasítása
    time.sleep(1.0)


finally:
    driver.close()
    # driver.close() # ezzel akár felugró ablakot is be lehet zárni,
    # ha a felugro ablakkal együtt akarjuk zárni az oldalt akkor quit kell
