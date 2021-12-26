from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C://Users//seker//Documents//driver//chromedriver.exe")

driver.get("https://www.salesforce.com")
print(driver.title)
driver.get("https://www.geeksforgeeks.org/")
print(driver.title)
driver.back()
print(driver.title)

