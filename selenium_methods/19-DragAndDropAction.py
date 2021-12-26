from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Firefox(executable_path="C://Users//seker//Documents//driver//geckodriver.exe")
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
driver.implicitly_wait(10)

source = driver.find_element(By.CSS_SELECTOR,"#box6")
target = driver.find_element(By.CSS_SELECTOR,"#box106")

action = ActionChains(driver)
action.drag_and_drop(source,target).perform()

