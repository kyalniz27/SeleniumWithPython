from XLUtils import ExcelDataFunctions
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path="C://Users//seker//Documents//driver//geckodriver.exe")
driver.get("https://www.rahulshettyacademy.com/#/index")
driver.maximize_window()
driver.implicitly_wait(10)

path = "C://Users//seker//Desktop//loginData.xlsx"
rows = ExcelDataFunctions.getRowCount(path,"Sheet1")

for r in range(2,rows+1):
    driver.find_element(By.XPATH,"//a[normalize-space()='Login']").click()
    email = ExcelDataFunctions.readData(path,"Sheet1",r,1)
    password = ExcelDataFunctions.readData(path,"Sheet1",r,2)

    driver.find_element(By.CSS_SELECTOR,"#email").send_keys(email)
    driver.find_element(By.CSS_SELECTOR,"#password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR,"input[value='Login']").click()

    userName = driver.find_element(By.XPATH,"//span[@class='navbar-current-user']").text

    if userName == "Mustafa Koklu":
        print("Test is passed")
        ExcelDataFunctions.writeData(path,"Sheet1",r,3,"Passed")
    else:
        print("Test is failed")
        ExcelDataFunctions.writeData(path, "Sheet1", r, 3, "Failed")

    driver.find_element(By.XPATH,"//a[normalize-space()='Home']").click()





