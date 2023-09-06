import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

serv_obj=Service("C:/Users/AbhinavRawat/WebDrivers/edgedriver_win64/msedgedriver.exe")
driver=webdriver.Edge(service=serv_obj)

driver.maximize_window()
driver.get("https://researchportal.beta.savanta.com/Surveys")
time.sleep(2)

driver.find_element(By.ID,"search-box").send_keys("6225")
time.sleep(2)

driver.find_element(By.XPATH, "(//table[@class='data-table']/descendant::tbody/descendant::a)[1]").click()
time.sleep(2)

# go to Quota Page
try:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@id='pageLinks']/div[1]/a[2])"))).click()
#    driver.find_element(By.XPATH, "(//*[@id='pageLinks']/div[1]/a[2])").click()
    time.sleep(2)
    print("Quota Page Clicked ✓")
except NoSuchElementException:
    print("Error occurred in Going to Quota Page")

try:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='quotas-page']/form/div[1]/div[1]/div[2]/div/div[1]/div[2]"))).click()
#    driver.find_element(By.XPATH, "//*[@id='quotas-page']/form/div[1]/div[1]/div[2]/div/div[1]/div[2]").click()
#    time.sleep(2)
    #driver.find_element(By.XPATH, "//*[@id='react-select-2-input']").send_keys("Gender")
    #time.sleep(2)
    #driver.find_element(By.ID, "react-select-2-listbox").click()
    #time.sleep(3)
    wait.until(EC.presence_of_element_located((By.ID, "react-select-2-option-2"))).click()
#    driver.find_element(By.ID, "react-select-2-option-2").click()
#    time.sleep(3)
    print("Drop-down Clicked ✓")
except NoSuchElementException:
    print("Error occurred in Clicking or selecting in Drop-down")


# to click on "Edit" button
try:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@id='quotas-page']/form/div[2]/div[3]/a)"))).click()
#    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/div[2]/div[3]/a)").click()
#    time.sleep(2)
    print('Edit button clicked ✓')
except NoSuchElementException:
    print("*****Edit button not clicked*****")

try:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@id='quotas-page']/form/table/tbody/tr/td[4]/input)"))).send_keys("19")
#    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/table/tbody/tr/td[4]/input)").send_keys("19")
#    time.sleep(2)
    wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@id='quotas-page']/form/table/tbody/tr/td[7]/input)"))).send_keys("19")
#    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/table/tbody/tr/td[7]/input)").send_keys("19")
#    time.sleep(2)
    print('Input send ✓')
except NoSuchElementException:
    # Handle the error for Task 1
    print("*****Inputs not send*****")

try:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@id='quotas-page']/form/div[2]/div[3]/a[3])"))).click()
#    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/div[2]/div[3]/a[3])").click()
#    time.sleep(2)
#    print('"Save Changes" button clicked')
    wait.until(EC.presence_of_element_located((By.XPATH, "(/html/body/div/div/div[2]/div/div/div/a[2])"))).click()
#    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/div/a[2])").click()
    time.sleep(2)
    print('Saved changes ✓')
except NoSuchElementException:
    print("*****Can't save changes*****")

# to click on "Edit" button
try:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@id='quotas-page']/form/div[2]/div[3]/a)"))).click()
#    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/div[2]/div[3]/a)").click()
#    time.sleep(2)
    print('Edit button clicked again ✓')
except NoSuchElementException:
    print("*****Edit button not clicked again*****")

# to click on "Show Advanced" button
try:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@id='quotas-page']/form/div[2]/div[3]/a[1])"))).click()
#    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/div[2]/div[3]/a[1])").click()
#    time.sleep(2)
    print('Show Advanced button clicked ✓')
except NoSuchElementException:
    print("*****Show Advanced button not clicked*****")

# to click on "Priority" drop-down
try:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@id='quotas-page']/form/table/tbody/tr/td[8]/div/div/div[2])"))).click()
#    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/table/tbody/tr/td[8]/div/div/div[2])").click()
#    time.sleep(2)
    wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@id='react-select-4-input'])"))).send_keys("Priority 1 (Highest)")
#    driver.find_element(By.XPATH, "(//*[@id='react-select-4-input'])").send_keys("Priority 1 (Highest)")
#    time.sleep(2)
    wait.until(EC.presence_of_element_located((By.ID, "react-select-4-listbox"))).click()
#    driver.find_element(By.ID, "react-select-4-listbox").click()
#    time.sleep(3)

    wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@id='quotas-page']/form/table/tbody/tr/td[8]/div/div/div[2])"))).click()
#    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/table/tbody/tr/td[8]/div/div/div[2])").click()
#    time.sleep(2)
    wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@id='react-select-4-input'])"))).send_keys("Priority 2")
#    driver.find_element(By.XPATH, "(//*[@id='react-select-4-input'])").send_keys("Priority 2")
#    time.sleep(2)
    wait.until(EC.presence_of_element_located((By.ID, "react-select-4-listbox"))).click()
#    driver.find_element(By.ID, "react-select-4-listbox").click()
#    time.sleep(3)

    wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@id='quotas-page']/form/table/tbody/tr/td[8]/div/div/div[2])"))).click()
#    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/table/tbody/tr/td[8]/div/div/div[2])").click()
#    time.sleep(2)
    wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@id='react-select-4-input'])"))).send_keys("Priority 3")
#    driver.find_element(By.XPATH, "(//*[@id='react-select-4-input'])").send_keys("Priority 3")
#    time.sleep(2)
    wait.until(EC.presence_of_element_located((By.ID, "react-select-4-listbox"))).click()
#    driver.find_element(By.ID, "react-select-4-listbox").click()
#    time.sleep(3)

    wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@id='quotas-page']/form/table/tbody/tr/td[8]/div/div/div[2])"))).click()
#    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/table/tbody/tr/td[8]/div/div/div[2])").click()
#    time.sleep(2)
    wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@id='react-select-4-input'])"))).send_keys("Priority 4")
#    driver.find_element(By.XPATH, "(//*[@id='react-select-4-input'])").send_keys("Priority 4")
#    time.sleep(2)
    wait.until(EC.presence_of_element_located((By.ID, "react-select-4-listbox"))).click()
#    driver.find_element(By.ID, "react-select-4-listbox").click()
#    time.sleep(3)

    wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@id='quotas-page']/form/table/tbody/tr/td[8]/div/div/div[2])"))).click()
#    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/table/tbody/tr/td[8]/div/div/div[2])").click()
#    time.sleep(2)
    wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@id='react-select-4-input'])"))).send_keys("Priority 5 (Lowest)")
#    driver.find_element(By.XPATH, "(//*[@id='react-select-4-input'])").send_keys("Priority 5 (Lowest)")
#    time.sleep(2)
    wait.until(EC.presence_of_element_located((By.ID, "react-select-4-listbox"))).click()
#    driver.find_element(By.ID, "react-select-4-listbox").click()
#    time.sleep(3)

    wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@id='quotas-page']/form/table/tbody/tr/td[8]/div/div/div[2])"))).click()
#    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/table/tbody/tr/td[8]/div/div/div[2])").click()
#    time.sleep(2)
    wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@id='react-select-4-input'])"))).send_keys("Standard")
#    driver.find_element(By.XPATH, "(//*[@id='react-select-4-input'])").send_keys("Standard")
#    time.sleep(2)
    wait.until(EC.presence_of_element_located((By.ID, "react-select-4-listbox"))).click()
#    driver.find_element(By.ID, "react-select-4-listbox").click()
#    time.sleep(3)

    wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@id='quotas-page']/form/table/tbody/tr/td[4]/input)"))).send_keys("25")
#    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/table/tbody/tr/td[4]/input)").send_keys("25")
#    time.sleep(2)
    wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@id='quotas-page']/form/table/tbody/tr/td[7]/input)"))).send_keys("25")
#    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/table/tbody/tr/td[7]/input)").send_keys("25")
#    time.sleep(2)

    wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@id='quotas-page']/form/div[2]/div[3]/a[3]/i)"))).click()
#    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/div[2]/div[3]/a[3]/i)").click()
#    time.sleep(2)

    wait.until(EC.presence_of_element_located((By.XPATH, "(/html/body/div/div/div[2]/div/div/div/a[2])"))).click()
#    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/div/a[2])").click()
    time.sleep(2)
    print('All priority drop-down clicked ✓')
except NoSuchElementException:
    print("*****Error with Priority drop-down*****")

# to click on "Show Advanced" button
try:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@id='quotas-page']/form/div[2]/div[3]/a[1])"))).click()
#    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/div[2]/div[3]/a[1])").click()
    time.sleep(2)
    print('Show Advanced button clicked again ✓')
except NoSuchElementException:
    print("*****Show Advanced button not clicked again*****")

# to click on "Hide Advanced" button
try:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@id='quotas-page']/form/div[2]/div[3]/a[1])"))).click()
#    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/div[2]/div[3]/a[1])").click()
    time.sleep(2)
    print('Hide Advanced button clicked ✓')
except NoSuchElementException:
    print("*****Hide Advanced button not clicked*****")

# to click on "Cancel" button
try:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@id='quotas-page']/form/div[2]/div[3]/a[2])"))).click()
#    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/div[2]/div[3]/a[2])").click()
    time.sleep(2)
    print('Cancel button clicked ✓')
except NoSuchElementException:
    print("*****Cancel button not clicked*****")

# to click on "Download to Excel" button
try:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@id='quotas-page']/form/div[1]/div[2]/a[1])"))).click()
#    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/div[1]/div[2]/a[1])").click()
    time.sleep(2)
    print('Download to Excel button clicked ✓')
except NoSuchElementException:
    print("*****Download to Excel button not clicked*****")

# to click on "Recalculate Quota" button
try:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@id='quotas-page']/form/div[1]/div[2]/a[3])"))).click()
#    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/div[1]/div[2]/a[3])").click()
#    time.sleep(2)
    wait.until(EC.presence_of_element_located((By.XPATH, "(/html/body/div/div/div[2]/div/div[1]/div/a[2])"))).click()
#    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div[1]/div/a[2])").click()
#    time.sleep(2)
    print('Recalculate Quota button clicked ✓')
except NoSuchElementException:
    print("*****Recalculate Quota button not clicked*****")