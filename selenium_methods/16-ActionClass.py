from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Firefox(executable_path="C://Users//seker//Documents//driver//geckodriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.CSS_SELECTOR,"#txtUsername").send_keys("Admin")
driver.find_element(By.CSS_SELECTOR,"#txtPassword").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR,"#btnLogin").click()

admin = driver.find_element(By.CSS_SELECTOR,"#menu_admin_viewAdminModule")
user_management = driver.find_element(By.CSS_SELECTOR,"#menu_admin_UserManagement")
users = driver.find_element(By.CSS_SELECTOR,"#menu_admin_viewSystemUsers")

actions = ActionChains(driver)
actions.move_to_element(admin).move_to_element(user_management).move_to_element(users).click().perform()

driver.quit()