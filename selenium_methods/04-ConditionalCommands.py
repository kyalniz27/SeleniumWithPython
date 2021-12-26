from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(executable_path="C://Users//seker//Documents//driver//chromedriver.exe")

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.delete_all_cookies()
sleep(2)

print(driver.title)
logo = driver.find_element(By.CSS_SELECTOR,".logoClass")
print('Is logo displayed:', logo.is_displayed())
login = driver.find_element(By.XPATH,"//button[contains(text(),'Login')]")
print('Is login enabled:', login.is_enabled())
radio = driver.find_element(By.XPATH,"(//input[@name='radioButton'])[2]")
print('Is radio button selected:', radio.is_selected())

driver.close()





