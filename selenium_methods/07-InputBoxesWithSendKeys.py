from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C://Users//seker//Documents//driver//chromedriver.exe")
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.XPATH,"//a[text()='Create new account']").click()

input_boxes = driver.find_elements(By.XPATH,"//*[contains(@class,'_58mg')]")
print('Length of the elements:',len(input_boxes))
driver.find_element(By.XPATH,"(//*[contains(@class,'_58mg')])[1]").send_keys("Mustafa")
driver.find_element(By.XPATH,"(//*[contains(@class,'_58mg')])[2]").send_keys("Koklu")

driver.close()