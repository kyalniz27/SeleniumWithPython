from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(executable_path="C://Users//seker//Documents//driver//chromedriver.exe")

driver.get("https://www.salesforce.com")
print("Title of the page:", driver.title)
sleep(2)
driver.find_element(By.LINK_TEXT, "Find out how").click()
print("Title of the page:", driver.title)

driver.close()







