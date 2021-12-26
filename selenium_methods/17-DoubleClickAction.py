from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Firefox(executable_path="C://Users//seker//Documents//driver//geckodriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)

ele = driver.find_element(By.CSS_SELECTOR,"button[ondblclick='myFunction1()']")
actions = ActionChains(driver)
actions.double_click(ele).perform()



