from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox(executable_path="C://Users//seker//Documents//driver//geckodriver.exe")
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.maximize_window()

driver.switch_to.frame("packageListFrame") # first frame
driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()
sleep(2)

# You need to go to page level at each time before jump into next frame
driver.switch_to.default_content()
driver.switch_to.frame("packageFrame") # second frame
driver.find_element(By.XPATH,"//*[text()='WebDriver']").click()
sleep(2)

driver.switch_to.default_content()
driver.switch_to.frame("classFrame") # Third frame
driver.find_element(By.XPATH,"/html[1]/body[1]/header[1]/nav[1]/div[1]/div[1]/ul[1]/li[6]/a[1]").click()
sleep(2)

driver.close()


