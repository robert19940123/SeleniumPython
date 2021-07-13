from selenium import webdriver
import csvpy

driver = webdriver.Chrome()
driver.get("http://www.rpachallenge.com/")


def list(l, f, a, r, c, p, e):
    last = driver.find_element_by_xpath('//*[@ng-reflect-name="labelLastName"]')
    first = driver.find_element_by_xpath('//*[@ng-reflect-name="labelFirstName"]')
    address = driver.find_element_by_xpath('//*[@ng-reflect-name="labelAddress"]')
    role = driver.find_element_by_xpath('//*[@ng-reflect-name="labelRole"]')
    comp_name = driver.find_element_by_xpath('//*[@ng-reflect-name="labelCompanyName"]')
    phone = driver.find_element_by_xpath('//*[@ng-reflect-name="labelPhone"]')
    email = driver.find_element_by_xpath('//*[@ng-reflect-name="labelEmail"]')
    button = driver.find_element_by_class_name("btn uiColorButton")

    last.send_keys(l)
    first.send_keys(f)
    address.send_keys(a)
    role.send_keys(r)
    comp_name.send_keys(c)
    phone.send_keys(p)
    email.send_keys(e)
    button.click()



#with open("challenge (1).csv", "r") as file:
    #csvreader = csvpy.reader(file, delimiter=',')
    #next(csvreader)
    #for row in csvreader:
