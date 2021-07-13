import time

from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/kitchensink.html")
    driver.find_element_by_id("openwindow").click()
    time.sleep(1.0)

    main_window = driver.window_handles[0]
    other_window = driver.switch_to.window('myWin')  # switch_to_val váltani kell a másik ablakra amit megnyitunk
    # majd meg kell adni a nevét amit a javascript automatikusan ad neki (forráskodban van --> F12 - Sources))

    assert driver.title == "met.hu - Országos Meteorológiai Szolgálat"  # ellenőrzés ablak címre
    print(driver.title)
    time.sleep(5.0)
    driver.close()  # ezzel bezájuk azt az ablakot amire átswitcheltünk
    driver.switch_to.window(main_window)  # ezzel átváltunk az eredeti ablakra (0.)
    driver.close()  # majd bezárjuk azt is

finally:
    pass
    # driver.quit() #ezzel minden ablakot egyszerre bne lehet zarni
