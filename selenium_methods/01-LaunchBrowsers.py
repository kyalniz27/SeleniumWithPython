from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C://Users//seker//Documents//driver//chromedriver.exe")
#driver = webdriver.Firefox(executable_path="C://Users//seker//Documents//driver//geckodriver.exe")

driver.get("https://www.salesforce.com")
print(driver.title)
print('URL of the page: ',driver.current_url)


driver.close()


