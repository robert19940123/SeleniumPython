from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/trickybuttons.html")

    buttons = driver.find_elements_by_xpath("//button")
    print(buttons)
    print(type(buttons))

    for button in buttons:
        button.click()
        result = driver.find_element_by_xpath("//label[@id='result']")
        print(result.text)

        assert(result.text == f"{button.text} was clicked")

finally:
    driver.close()


# x0ami kell xpath-ba jobb egérgomb - copy- copy to xpath