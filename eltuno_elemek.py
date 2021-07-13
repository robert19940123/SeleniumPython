from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/kitchensink.html")

    input_text = driver.find_element_by_id("displayed-text")
    hide_button = driver.find_element_by_id("hide-textbox")
    show_textbox = driver.find_element_by_id("show-textbox")
    print(input_text.is_displayed())
    hide_button.click()
    print(input_text.is_displayed())

finally:
    driver.close()