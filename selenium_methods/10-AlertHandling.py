from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path="C://Users//seker//Documents//driver//geckodriver.exe")
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.CSS_SELECTOR,"#name").send_keys("Yade")
driver.find_element(By.CSS_SELECTOR,"#confirmbtn").click()

driver.switch_to_alert().accept()

driver.close()
