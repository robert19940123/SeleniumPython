from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/forms.html")
    main_window = driver.window_handles[0]
    driver.execute_script("window.open('', 'newwin', 'height=800, width=600')")
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)
    driver.get("http://localhost:9999/general.html")
    text = driver.find_element_by_tag_name("h4").text
    driver.switch_to.window(main_window)
    ex_input = driver.find_element_by_id("example-input-text")
    ex_input.send_keys(text)
finally:
    pass
    # driver.close()
