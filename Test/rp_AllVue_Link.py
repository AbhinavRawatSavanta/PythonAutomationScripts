import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

serv_obj=Service("C:/Users/AbhinavRawat/WebDrivers/edgedriver_win64/msedgedriver.exe")
driver=webdriver.Edge(service=serv_obj)

driver.maximize_window()
driver.get("https://researchportal.beta.savanta.com/Surveys")
time.sleep(2)

driver.find_element(By.ID,"search-box").send_keys("6184")
time.sleep(2)

driver.find_element(By.XPATH, "(//table[@class='data-table']/descendant::tbody/descendant::a)[1]").click()
time.sleep(2)

# go to AllVue Page
driver.find_element(By.XPATH, "(//*[@id='pageLinks']/div[1]/a[5])").click()
time.sleep(2)


# click on "Open Survey in AllVue"
try:
    driver.find_element(By.XPATH, "(//*[@id='customerportal-page']/form/div[1]/a[1])").click()
    time.sleep(2)
    print("Open Survey in AllVue clicked ✓")
except NoSuchElementException:
    print("*****Open Survey in AllVue not clicked *****")

# click on Resync Responses
try:
    driver.find_element(By.XPATH, "(//*[@id='customerportal-page']/form/div[1]/a[2])").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/div/div/a[2])").click()
    time.sleep(3)
    print("Resync Responses clicked ✓")
except NoSuchElementException:
    print("*****Resync Responses not clicked *****")

# Click on AllVue projects settings link
try:
    driver.find_element(By.XPATH, "(//*[@id='customerportal-page']/form/div[2]/div[1]/div[2]/a)").click()
    time.sleep(2)
    print("AllVue projects settings link clicked ✓")
except NoSuchElementException:
    print("*****AllVue projects settings link not clicked *****")

# Select Company drop-down
try:
    driver.find_element(By.XPATH, "(//*[@id='customerportal-page']/form/div[2]/a)").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div[2]/div)").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(//*[@id='react-select-3-input'])").send_keys('Savanta Tech')
    time.sleep(2)
    driver.find_element(By.ID, "react-select-3-listbox").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div[3]/a[2])").click()
    time.sleep(2)
    print("Select Company drop-down clicked ✓")
except NoSuchElementException:
    print("*****Select Company drop-down not clicked *****")

# Changing Survey Display Name
try:
    driver.find_element(By.XPATH, "(//*[@id='customerportal-page']/form/div[2]/fieldset/input)").send_keys('TEST')
    time.sleep(2)
    print("Survey Display Name changed ✓")
except NoSuchElementException:
    print("*****Survey Display Name not changed *****")

# Adding Quota
try:
    driver.find_element(By.XPATH, "(//*[@id='customerportal-page']/form/div[2]/fieldset/a)").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/div[2]/div[1]/div/input)").send_keys('Total')
    time.sleep(3)
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/label)").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/div[3]/a[2])").click()
    time.sleep(3)
    print("Quota added ✓")
except NoSuchElementException:
    print("*****Quota not added *****")

# CLick on Share files button --- Need Egnyte login
#driver.find_element(By.XPATH, "(//*[@id='customerportal-page']/form/div[2]/fieldset/div[4]/div[1]/a)").click()
#time.sleep(2)

# Removing Quota
try:
    driver.find_element(By.XPATH, "(//*[@id='customerportal-page']/form/div[2]/fieldset/fieldset/div[2]/div)").click()
    driver.find_element(By.XPATH, "(//*[@id='customerportal-page']/form/div[2]/fieldset/fieldset/div[2]/div/div/button/i)").click()
    time.sleep(2)
    print("Quota removed ✓")
except NoSuchElementException:
    print("*****Quota not removed *****")

#
try:
    driver.find_element(By.XPATH, "(//*[@id='customerportal-page']/form/div[2]/fieldset/div[4]/input)").clear()
    time.sleep(2)
    driver.find_element(By.XPATH, "(//*[@id='customerportal-page']/form/div[2]/fieldset/div[4]/input)").send_keys("abhinav.rawat@savanta.com")
    time.sleep(2)
    print("Notification email changed ✓")
except NoSuchElementException:
    print("*****Notification email not changed *****")