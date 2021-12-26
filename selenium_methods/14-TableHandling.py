from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox(executable_path="C://Users//seker//Documents//driver//geckodriver.exe")
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(10)

row = len(driver.find_elements(By.XPATH,"//table/tbody/tr"))
col = len(driver.find_elements(By.XPATH,"//table/tbody/tr/th"))

print('Number of the rows:', row)
print('Number of the col :', col)

for r in range(2,row+1):
    for c in range(1,col+1):
        value = driver.find_element(By.XPATH,"//body[1]/div[3]/div[1]/fieldset[1]/table[1]/tbody[1]/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value,end='   ')
    print()

driver.quit()