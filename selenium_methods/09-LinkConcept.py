from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path="C://Users//seker//Documents//driver//geckodriver.exe")
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(10)

links = driver.find_elements(By.TAG_NAME,"a")
print('Number of links:',len(links))
for link in links:
    print(link.text)

driver.find_element(By.LINK_TEXT,"Home").click()
