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


# Click on Pause Survey
try:
    driver.find_element(By.XPATH, "/html/body/form/div[2]/div/div[2]/div/div[1]/div[2]/a[2]/i").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/a[2]").click()
    time.sleep(2)
    print("Survey Paused ✓")
except NoSuchElementException:
    print("*****Survey not paused *****")

# Reopen Survey
try:
    driver.find_element(By.XPATH, "/html/body/form/div[2]/div/div[2]/div/div[1]/div[2]/a[2]/i").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/a[2]").click()
    time.sleep(2)
    print("Survey Reopened ✓")
except NoSuchElementException:
    print("*****Survey not reopened *****")

# Close Survey
try:
    driver.find_element(By.XPATH, "/html/body/form/div[2]/div/div[2]/div/div[1]/div[2]/a[3]/i").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/a[2]").click()
    time.sleep(2)
    print("Survey Closed ✓")
except NoSuchElementException:
    print("*****Survey not closed *****")

# Reopen Survey again
try:
    driver.find_element(By.XPATH, "/html/body/form/div[2]/div/div[2]/div/div[1]/div[2]/a[2]/i").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/a[2]").click()
    time.sleep(2)
    print("Survey Reopened again ✓")
except NoSuchElementException:
    print("*****Survey not reopened again *****")

# Version History
try:
    driver.find_element(By.XPATH, "/html/body/form/div[2]/div/div[2]/div/div[1]/div[2]/a[4]/i").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/a").click()
    time.sleep(2)
    print("Version History clicked ✓")
except NoSuchElementException:
    print("*****Version History not clicked *****")

# Settings
try:
    driver.find_element(By.XPATH, "/html/body/form/div[2]/div/div[2]/div/div[1]/div[2]/a[5]/i").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='Survey name']").clear()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='Survey name']").send_keys("Testing")
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/form/fieldset/div[2]/div[3]/label[2]/div/div[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/form/div/a[2]").click()
    time.sleep(2)
    print("Settings clicked and changed ✓")
except NoSuchElementException:
    print("*****Settings not clicked and can't changed *****")


# Adding respondents ( Test and Main )
try:
    driver.find_element(By.XPATH, "/html/body/form/div[2]/div/div[2]/div/div[3]/div[3]/div[1]/a").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/form/div[2]/div/div[2]/div/div[3]/div[3]/div[1]/ul/li[1]/a/div").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='salutation']").send_keys("Mr")
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='first-name']").send_keys("Test")
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='email']").send_keys("CheckTest1@abc.com")
    time.sleep(2)

    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/form/div/div[4]/fieldset[2]/div/div").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='react-select-3-input']").send_keys("Test")
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='react-select-3-listbox']").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/form/div/div[7]/a[2]").click()
    time.sleep(2)
    print("Respondent added in TEST segment ✓")
except NoSuchElementException:
    print("*****Respondent not added in TEST segment *****")

try:
    driver.find_element(By.XPATH, "/html/body/form/div[2]/div/div[2]/div/div[3]/div[3]/div[1]/a").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/form/div[2]/div/div[2]/div/div[3]/div[3]/div[1]/ul/li[1]/a/div").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='salutation']").send_keys("Mr")
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='first-name']").send_keys("Main")
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='email']").send_keys("CheckMain1@abc.com")
    time.sleep(2)

    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/form/div/div[4]/fieldset[2]/div/div").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='react-select-5-input']").send_keys("Main")
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='react-select-5-listbox']").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/form/div/div[7]/a[2]").click()
    time.sleep(2)
    print("Respondent added in MAIN segment ✓")
except NoSuchElementException:
    print("*****Respondent not added in MAIN segment *****")


# CLick on Bulk Edit
try:
    driver.find_element(By.XPATH, "//*[@id='status-page']/div[3]/div[3]/a[1]/i").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/button").click()
    time.sleep(2)
    print("Clicked on Bulk Edit ✓")
except NoSuchElementException:
    print("*****Bulk edit button not clicked *****")

# Archiving respondents
try:
    driver.find_element(By.XPATH, "//*[@id='status-page']/div[3]/div[3]/a[2]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div[2]/div[1]/div[3]/a").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/div/a[2]").click()
    time.sleep(2)
    print("Respondents Archived ✓")
except NoSuchElementException:
    print("*****Respondents not Archived *****")

# Restoring respondents
try:
    driver.find_element(By.XPATH, "//*[@id='status-page']/div[3]/div[3]/a[2]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div[2]/div[2]/div/div[1]/div[1]/label").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div[3]/a[2]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/div/a[2]").click()
    time.sleep(2)
    print("Respondents Restoring ✓")
except NoSuchElementException:
    print("*****Respondents not Restored ***")

# CLick on Preview Data
try:
    driver.find_element(By.XPATH, "//*[@id='status-page']/div[3]/div[3]/div[2]/a").click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)
    print("Clicked on Preview Data ✓")
except NoSuchElementException:
    print("*****Preview data not clicked ***")

# Click on Download
try:
    driver.find_element(By.XPATH, "//*[@id='status-page']/div[3]/div[3]/div[2]/div/a").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='status-page']/div[3]/div[3]/div[2]/div/ul/li[1]/a/div").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='status-page']/div[3]/div[3]/div[2]/div/a").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='status-page']/div[3]/div[3]/div[2]/div/ul/li[2]/a/div").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='status-page']/div[3]/div[3]/div[2]/div/a").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='status-page']/div[3]/div[3]/div[2]/div/ul/li[3]/a/div").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='status-page']/div[3]/div[3]/div[2]/div/a").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='status-page']/div[3]/div[3]/div[2]/div/ul/li[4]/a/div").click()
    time.sleep(2)
    print("Downloaded all available files ✓")
except NoSuchElementException:
    print("*****Couldn't download available files ***")