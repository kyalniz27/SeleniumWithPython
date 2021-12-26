from selenium import webdriver
from selenium.webdriver.common.by import By

fp = webdriver.FirefoxProfile()
fp.set_preference("browser.helperApps.neverAsk.saveToDisk","text/plain,application/pdf")
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir","C://Users//seker//Documents")
fp.set_preference("browser.download.folderList",2)
fp.set_preference("pdfjs.disabled",True)

driver = webdriver.Firefox(executable_path="C://Users//seker//Documents//driver//geckodriver.exe",
                           firefox_profile=fp)

driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.CSS_SELECTOR,"#textbox").send_keys("Downloading a file through FireFox browser which is different than Chrome")
driver.find_element(By.CSS_SELECTOR,"#createTxt").click()
driver.find_element(By.CSS_SELECTOR,"#link-to-download").click()

driver.close()