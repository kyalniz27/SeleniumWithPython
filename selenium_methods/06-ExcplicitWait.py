from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C://Users//seker//Documents//driver//chromedriver.exe")

driver.get("https://www.expedia.com")
driver.maximize_window()
driver.implicitly_wait(10)

#driver.find_element(By.CSS_SELECTOR,".uitk-tab-anchor.uitk-tab-anchor-selected").click()
driver.find_element(By.XPATH,"//*[@id='wizardMainRegionV2']/div/div/div/div/ul/li[2]/a").click()


driver.find_element(By.XPATH,"//*[@id='wizard-flight-tab-roundtrip']/div[2]/div[1]/div/div[1]").click()
driver.find_element(By.CSS_SELECTOR,"#location-field-leg1-origin").send_keys("jfk")

wait = WebDriverWait(driver,10)

wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@class='uitk-typeahead-results']/ul/li[1]"))).click()




