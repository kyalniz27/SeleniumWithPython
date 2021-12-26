from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Firefox(executable_path="C://Users//seker//Documents//driver//geckodriver.exe")
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(10)

element = driver.find_element(By.CSS_SELECTOR,"#dropdown-class-example")
drp = Select(element)

drp.select_by_index(1)
sleep(1)
drp.select_by_value("option2")
sleep(1)
drp.select_by_visible_text("Option3")
sleep(1)

print('Number of options:',len(drp.options))

for option in drp.options:
    if(option.text == "Select"):
        continue
    print(option.text)

driver.close()

