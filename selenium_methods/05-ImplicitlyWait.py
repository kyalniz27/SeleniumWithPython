from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C://Users//seker//Documents//driver//chromedriver.exe")

driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.delete_all_cookies()
driver.implicitly_wait(10)

driver.find_element(By.ID,"email").send_keys("kyalniz27@gmail.com")
driver.find_element(By.ID,"pass").send_keys("27mart85")
driver.find_element(By.XPATH,"(//*[text()='Log In'])[1]").click()
driver.find_element(By.XPATH,"//input[@placeholder='Search Facebook']").send_keys("Pala")
driver.find_element(By.XPATH,"//*[contains(text(),'Pala ')]").click()






