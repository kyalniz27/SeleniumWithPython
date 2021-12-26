from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path="C://Users//seker//Documents//driver//geckodriver.exe")
driver.get("https://www.amazon.com")
driver.maximize_window()
driver.implicitly_wait(10)

#Capture all the cookies created by browser and number
cookies = driver.get_cookies()
print('Number of cookies:',len(cookies))
print("Before adding cookie:",cookies)

# How to add a new cookie to the browser. Cookies are stored in key-value form
cookie = {'name':'MyCookie','value':'13579'}
driver.add_cookie(cookie)
cookies = driver.get_cookies()
print('Number of cookies:',len(cookies))
print("After adding cookie:",cookies)

#To delete the cookie you need to know the cookie name
driver.delete_cookie("MyCookie")
cookies = driver.get_cookies()
print('After deleting a cookie:',len(cookies))

driver.close()