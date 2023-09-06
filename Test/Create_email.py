import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


serv_obj=Service("C:/Users/AbhinavRawat/WebDrivers/edgedriver_win64/msedgedriver.exe")
driver=webdriver.Edge(service=serv_obj)

driver.maximize_window()
driver.get("https://researchportal.beta.savanta.com/Surveys")
time.sleep(2)

driver.find_element(By.ID,"search-box").send_keys("6225")
time.sleep(2)

driver.find_element(By.XPATH, "(//table[@class='data-table']/descendant::tbody/descendant::a)[1]").click()
time.sleep(2)

# go to Email Sends Page
driver.find_element(By.XPATH, "(//*[@id='pageLinks']/div[1]/a[4])").click()
time.sleep(2)

# click on "Create new email" button
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@id='emails-page']/div[1]/div/div[1]/div[1]/a)"))).click()
#driver.find_element(By.XPATH, "(//*[@id='emails-page']/div[1]/div/div[1]/div[1]/a)").click()
time.sleep(2)

#
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "name"))).send_keys("ABC")
#driver.find_element(By.ID, "name").send_keys("ABC")
time.sleep(2)

#
driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[3]/fieldset[1]/div[2]/div/div[2]/div)").click()
driver.find_element(By.XPATH, "(//*[@id='react-select-3-input'])").send_keys("surveys@savanta-mail.com")
driver.find_element(By.ID, "react-select-3-listbox").click()
time.sleep(2)

#
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/form/div[3]/fieldset[2]/input").send_keys("TESTER")
time.sleep(2)

#
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/form/div[4]/fieldset/input").send_keys("TESTING")
time.sleep(2)

# Click on "Upload an image"
driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[5]/fieldset/div/div/a[1])").click()
time.sleep(2)
driver.find_element(By.ID,"image-upload-button").send_keys("C:\\Users\\AbhinavRawat\\Desktop\\AllVue\\Documents\\Automation Script\\Research Portal\\Test\\Test1.jpg")
time.sleep(2)
driver.find_element(By.XPATH, "(/html/body/div[2]/div/div[2]/div/button)").click()
time.sleep(2)

#
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/form/div[5]/fieldset/textarea").send_keys("PLAIN HTML TEXT")
time.sleep(2)

#
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/form/div[6]/fieldset/textarea").send_keys("PLAIN TEXT")
time.sleep(2)

#
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/form/div[7]/fieldset[1]/div/label").click()
time.sleep(2)

#
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/form/div[9]/a[2]").click()
time.sleep(2)