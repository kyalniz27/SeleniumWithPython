from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox(executable_path="C://Users//seker//Documents//driver//geckodriver.exe")
driver.get("https://www.amazon.com")
driver.maximize_window()

sleep(1)
# driver.save_screenshot("C://Users//seker//Desktop//screenshot//image.png")
driver.get_screenshot_as_file("C://Users//seker//Desktop//screenshot//amazonHomepage.jpg")

driver.close()