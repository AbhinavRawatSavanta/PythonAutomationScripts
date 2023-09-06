import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

serv_obj=Service("C:/Users/AbhinavRawat/WebDrivers/edgedriver_win64/msedgedriver.exe")
driver=webdriver.Edge(service=serv_obj)

driver.maximize_window()
driver.get("https://researchportal.beta.savanta.com/Surveys")
time.sleep(2)

driver.find_element(By.ID,"search-box").send_keys("6128")
time.sleep(2)

driver.find_element(By.XPATH, "(//table[@class='data-table']/descendant::tbody/descendant::a)[1]").click()
time.sleep(2)

# go to Quota Page
try:
    driver.find_element(By.XPATH, "(//*[@id='pageLinks']/div[1]/a[2])").click()
    time.sleep(2)

except NoSuchElementException:
    print("Error occurred in Going to Quota Page")


driver.find_element(By.XPATH, "//*[@id='quotas-page']/form/div[1]/div[1]/div[2]/div/div[1]/div[2]").click()
time.sleep(3)
#driver.find_element(By.XPATH, "//*[@id='react-select-2-input']").send_keys("Age")
#time.sleep(3)
#driver.find_element(By.ID, "react-select-2-listbox").click()
#time.sleep(3)

driver.find_element(By.ID, "react-select-2-option-2").click()
time.sleep(3)

# to click on "Edit" button
try:
    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/div[2]/div[3]/a)").click()
    time.sleep(2)
    print('Edit button clicked again')
except NoSuchElementException:
    print("*****Edit button not clicked again*****")

# to click on "Show Advanced" button
try:
    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/div[2]/div[3]/a[1])").click()
    time.sleep(2)
    print('Show Advanced button clicked')
except NoSuchElementException:
    print("*****Show Advanced button not clicked*****")

# to click on "Priority" drop-down
driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/table/tbody/tr/td[8]/div/div/div[2])").click()
time.sleep(2)
driver.find_element(By.XPATH, "(//*[@id='react-select-4-input'])").send_keys("Priority 1 (Highest)")
time.sleep(2)
driver.find_element(By.ID, "react-select-4-listbox").click()
time.sleep(3)

driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/table/tbody/tr/td[8]/div/div/div[2])").click()
time.sleep(2)
driver.find_element(By.XPATH, "(//*[@id='react-select-4-input'])").send_keys("Priority 2")
time.sleep(2)
driver.find_element(By.ID, "react-select-4-listbox").click()
time.sleep(3)

driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/table/tbody/tr/td[8]/div/div/div[2])").click()
time.sleep(2)
driver.find_element(By.XPATH, "(//*[@id='react-select-4-input'])").send_keys("Priority 3")
time.sleep(2)
driver.find_element(By.ID, "react-select-4-listbox").click()
time.sleep(3)

driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/table/tbody/tr/td[8]/div/div/div[2])").click()
time.sleep(2)
driver.find_element(By.XPATH, "(//*[@id='react-select-4-input'])").send_keys("Priority 4")
time.sleep(2)
driver.find_element(By.ID, "react-select-4-listbox").click()
time.sleep(3)

driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/table/tbody/tr/td[8]/div/div/div[2])").click()
time.sleep(2)
driver.find_element(By.XPATH, "(//*[@id='react-select-4-input'])").send_keys("Priority 5 (Lowest)")
time.sleep(2)
driver.find_element(By.ID, "react-select-4-listbox").click()
time.sleep(3)


driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/table/tbody/tr/td[4]/input)").send_keys("12")
time.sleep(2)
driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/table/tbody/tr/td[7]/input)").send_keys("12")
time.sleep(2)

driver.find_element(By.XPATH, "(//*[@id='quotas-page]/form/div[2]/div[3]/a[3])").click()
time.sleep(2)