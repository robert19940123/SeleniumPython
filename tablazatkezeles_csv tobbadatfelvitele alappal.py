from selenium import webdriver
import csv

driver = webdriver.Chrome()
driver.get("http://localhost:9999/filltablewithsum.html")


def find_and_clear_by_id(id):
    element = driver.find_element_by_id(id)
    element.clear()
    return element


add_button = driver.find_element_by_id("add")

with open("csvtext.text") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        print(row)
        find_and_clear_by_id("product").send_keys(row[0])  # a row[0] paranccsal a send keys-ben lehet meghívni a csv adott sorát
        find_and_clear_by_id("quantity").send_keys(row[1])
        find_and_clear_by_id("price").send_keys(row[2])
        add_button.click()

totals = driver.find_element_by_xpath('//table[@id="resultTotals"]/tbody/tr/td[3]')
print(totals.text)

results_rows = driver.find_elements_by_xpath("//table[@id='results']/tbody/tr")

for row in results_rows:
    cells = row.find_elements_by_tag_name("td")
    print(cells[0].text, cells[1].text, cells[2].text)

