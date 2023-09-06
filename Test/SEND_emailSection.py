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


# CLick on "Send" link
driver.find_element(By.XPATH,"(//*[@id='emails-page']/div[1]/div/div[2]/div[1]/div[1]/div[3]/div[1]/a[4])").click()
time.sleep(2)

# CLick on "Read the full guidelines" link
driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/a)").click()
time.sleep(2)

# CLick on "OK" button
driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/div[4]/a[2])").click()
time.sleep(2)

# Click on "radio buttons"
driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/form/div[2]/label)").click()
time.sleep(2)
driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/form/div[1]/label)").click()
time.sleep(2)

# Click on "NEXT" button
driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/div[2]/a[2])").click()
time.sleep(2)


# selecting the radio buttons
driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/form/div[2]/label)").click()
time.sleep(2)
driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/form/div[1]/label)").click()
time.sleep(2)

# tick and un-tick the radio button of emails
driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/form/div[3]/label)").click()
time.sleep(2)
driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/form/div[3]/label)").click()
time.sleep(2)

# Click on "NEXT" button
driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/div[2]/a[2])").click()
time.sleep(2)

# Closing
driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/button").click()
time.sleep(2)
