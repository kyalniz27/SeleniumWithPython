from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox(executable_path="C://Users//seker//Documents//driver//geckodriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")
driver.maximize_window()

driver.find_element(By.XPATH,"(//*[@class='btn btn-info'])[1]").click()

handles = driver.window_handles # Return all the handle values of opened browser windows

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title == "Frames & windows":
        driver.close() # Close only the parent window

driver.find_element(By.XPATH,"//span[normalize-space()='Downloads']").click()
