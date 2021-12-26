from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path="C://Users//seker//Documents//driver//geckodriver.exe")
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

status_radio1 = driver.find_element(By.XPATH,"//*[contains(@value,'radio1')]").is_selected()
print('is_selected',status_radio1)
driver.find_element(By.XPATH,"//*[contains(@value,'radio1')]").click()
status_radio1 = driver.find_element(By.XPATH,"//*[contains(@value,'radio1')]").is_selected()
print('is_selected',status_radio1)

driver.close()


