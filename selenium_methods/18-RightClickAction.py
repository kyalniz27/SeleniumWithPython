from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Firefox(executable_path="C://Users//seker//Documents//driver//geckodriver.exe")
driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
driver.implicitly_wait(10)

right_click = driver.find_element(By.CSS_SELECTOR,".context-menu-one.btn.btn-neutral")
action = ActionChains(driver)
action.context_click(right_click).perform()