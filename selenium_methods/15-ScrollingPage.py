from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox(executable_path="C://Users//seker//Documents//driver//geckodriver.exe")
driver.get("https://darksky.net")
driver.maximize_window()
driver.implicitly_wait(10)

# 1. Scroll down by pixel
#driver.execute_script("window.scrollBy(0,500)","")

# 2. Scroll down till find the element
#time_machine = driver.find_element(By.CSS_SELECTOR,"a[class='button']")
#driver.execute_script("arguments[0].scrollIntoView();",time_machine)

# 3. Scroll down till the bottom of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")


