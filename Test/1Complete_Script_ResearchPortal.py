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

driver.find_element(By.ID,"search-box").send_keys("6300")
time.sleep(2)

print("############ STATUS PAGE ############")

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
    time.sleep(4)
    driver.find_element(By.XPATH, "/html/body/form/div[2]/div/div[2]/div/div[3]/div[3]/div[1]/ul/li[1]/a/div").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='salutation']").send_keys("Mr")
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='first-name']").send_keys("Test")
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='email']").send_keys("FullTest10@abc.com")
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
    time.sleep(4)
    driver.find_element(By.XPATH, "/html/body/form/div[2]/div/div[2]/div/div[3]/div[3]/div[1]/ul/li[1]/a/div").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='salutation']").send_keys("Mr")
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='first-name']").send_keys("Main")
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='email']").send_keys("FullMain10@abc.com")
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

print("############ QUOTA PAGE ############")

# go to Quota Page
try:
    driver.find_element(By.XPATH, "(//*[@id='pageLinks']/div[1]/a[2])").click()
    time.sleep(2)
    print("Quota Page Clicked ✓")
except NoSuchElementException:
    print("Error occurred in Going to Quota Page")

try:
    driver.find_element(By.XPATH, "//*[@id='quotas-page']/form/div[1]/div[1]/div[2]/div/div[1]/div[2]").click()
    time.sleep(2)
    driver.find_element(By.ID, "react-select-2-option-2").click()
    time.sleep(3)
    print("Drop-down Clicked ✓")
except NoSuchElementException:
    print("Error occurred in Clicking or selecting in Drop-down")


# to click on "Edit" button
try:
    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/div[2]/div[3]/a)").click()
    time.sleep(2)
    print('Edit button clicked ✓')
except NoSuchElementException:
    print("*****Edit button not clicked*****")

try:
    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/table/tbody/tr/td[4]/input)").send_keys("19")
    time.sleep(2)
    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/table/tbody/tr/td[7]/input)").send_keys("19")
    time.sleep(2)
    print('Input send ✓')
except NoSuchElementException:
    # Handle the error for Task 1
    print("*****Inputs not send*****")

try:
    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/div[2]/div[3]/a[3])").click()
    time.sleep(2)
#    print('"Save Changes" button clicked')
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/div/a[2])").click()
    time.sleep(4)
    print('Saved changes ✓')
except NoSuchElementException:
    print("*****Can't save changes*****")

# to click on "Edit" button
try:
    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/div[2]/div[3]/a)").click()
    time.sleep(2)
    print('Edit button clicked again ✓')
except NoSuchElementException:
    print("*****Edit button not clicked again*****")

# to click on "Show Advanced" button
try:
    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/div[2]/div[3]/a[1])").click()
    time.sleep(2)
    print('Show Advanced button clicked ✓')
except NoSuchElementException:
    print("*****Show Advanced button not clicked*****")

# to click on "Priority" drop-down
try:
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

    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/table/tbody/tr/td[8]/div/div/div[2])").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(//*[@id='react-select-4-input'])").send_keys("Standard")
    time.sleep(2)
    driver.find_element(By.ID, "react-select-4-listbox").click()
    time.sleep(3)

    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/table/tbody/tr/td[4]/input)").send_keys("25")
    time.sleep(2)
    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/table/tbody/tr/td[7]/input)").send_keys("25")
    time.sleep(2)

    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/div[2]/div[3]/a[3]/i)").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/div/a[2])").click()
    time.sleep(2)
    print('All priority drop-down clicked ✓')
except NoSuchElementException:
    print("*****Error with Priority drop-down*****")

# to click on "Show Advanced" button
try:
    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/div[2]/div[3]/a[1])").click()
    time.sleep(2)
    print('Show Advanced button clicked again ✓')
except NoSuchElementException:
    print("*****Show Advanced button not clicked again*****")

# to click on "Hide Advanced" button
try:
    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/div[2]/div[3]/a[1])").click()
    time.sleep(2)
    print('Hide Advanced button clicked ✓')
except NoSuchElementException:
    print("*****Hide Advanced button not clicked*****")

# to click on "Cancel" button
try:
    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/div[2]/div[3]/a[2])").click()
    time.sleep(2)
    print('Cancel button clicked ✓')
except NoSuchElementException:
    print("*****Cancel button not clicked*****")

# to click on "Download to Excel" button
try:
    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/div[1]/div[2]/a[1])").click()
    time.sleep(2)
    print('Download to Excel button clicked ✓')
except NoSuchElementException:
    print("*****Download to Excel button not clicked*****")

# to click on "Recalculate Quota" button
try:
    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/div[1]/div[2]/a[3])").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div[1]/div/a[2])").click()
    time.sleep(2)
    print('Recalculate Quota button clicked ✓')
except NoSuchElementException:
    print("*****Recalculate Quota button not clicked*****")

print("############ EMAIL PAGE - NEW EMAIL ############")

# go to Email Sends Page
driver.find_element(By.XPATH, "(//*[@id='pageLinks']/div[1]/a[4])").click()
time.sleep(2)

try:
    # click on "Create new email" button
    driver.find_element(By.XPATH, "(//*[@id='emails-page']/div[1]/div/div[1]/div[1]/a)").click()
    time.sleep(2)
    #
    driver.find_element(By.ID, "name").send_keys("ABC")
    time.sleep(2)
    #
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[3]/fieldset[1]/div[2]/div/div[2]/div)").click()
    driver.find_element(By.ID, "react-select-2-option-0-0").click()
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
    print("New Email created ✓")
except NoSuchElementException:
    print("*****New Email cannot be created*****")

try:
    # click on edit button
    driver.find_element(By.XPATH, "(//*[@id='emails-page']/div[1]/div/div[2]/div[1]/div[1]/div[3]/div[1]/a[1])").click()
    time.sleep(2)
    # click on "Request a new address" link
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[3]/fieldset[1]/div[1]/a)").click()
    time.sleep(2)
    # Click on "Upload an image"
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[5]/fieldset/div/div/a[1])").click()
    time.sleep(2)
    driver.find_element(By.ID,"image-upload-button").send_keys("C:\\Users\\AbhinavRawat\\Desktop\\AllVue\\Documents\\Automation Script\\Research Portal\\Test\\TEST.png")
    time.sleep(2)
    driver.find_element(By.XPATH, "(/html/body/div[2]/div/div[2]/div/button)").click()
    time.sleep(2)
    # Click on "How to create an email" link
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[5]/fieldset/div/div/a[2])").click()
    time.sleep(2)
    # Edit values
    # edit name
    driver.find_element(By.ID,"name").send_keys("QA")
    driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/form/div[3]/fieldset[2]/input").send_keys("Savanta Tech")
    driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/form/div[5]/fieldset/textarea").send_keys("Hi , this is test")
    driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/form/div[6]/fieldset/textarea").send_keys("This is second text area")
    driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/form/div[7]/fieldset[1]/div/label").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/form/div[9]/a[2]").click()
    time.sleep(2)
    print("Email Edited ✓")
except NoSuchElementException:
    print("*****Email cannot be edited*****")

try:
    # Test Email
    driver.find_element(By.XPATH,"//*[@id='emails-page']/div[1]/div/div[2]/div[1]/div[1]/div[3]/div[1]/a[3]").click()
    time.sleep(6)

    # Add respondent in Test Email
    driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/div[2]/div[3]/div[2]/div/a)").click()
    time.sleep(2)

    # Add inputs in "Add respondents"
    driver.find_element(By.ID,"salutation").send_keys("Mr")
    driver.find_element(By.ID,"first-name").send_keys("Test4")
    driver.find_element(By.ID,"email").send_keys("test16@xyz.com")
    time.sleep(2)
    driver.find_element(By.XPATH,"(/html/body/div[2]/div/div[2]/div/div/form/div/div[7]/a[2])").click()
    time.sleep(4)
    print("Respondent added ✓")
except NoSuchElementException:
    print("*****Respondents cannot be added*****")

try:
    # CLick "Send test emails" button
    driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/div[2]/div[3]/a)").click()
    time.sleep(2)
    # Send now button
    driver.find_element(By.XPATH,"(/html/body/div[2]/div/div[2]/div/div/div/a[2])").click()
    time.sleep(4)
    print("Email send ✓")
except NoSuchElementException:
    print("*****Email cannot be send*****")

print("############ EMAIL PAGE - FOLLOW-UP EMAIL ############")

# go to Email Sends Page
driver.find_element(By.XPATH, "(//*[@id='pageLinks']/div[1]/a[4])").click()
time.sleep(2)

try:
    # Add follow up email
    driver.find_element(By.XPATH,"(//*[@id='emails-page']/div[1]/div[1]/div[2]/div[2]/div[2]/a)").click()
    time.sleep(2)
    # Entering name
    driver.find_element(By.XPATH,"(//*[@id='name'])").send_keys("Test")
    time.sleep(2)
    # Entering Subject line
    driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/form/div[3]/fieldset/input)").send_keys("Testing the Follow up")
    time.sleep(2)
    # Entering the HTML Email
    driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/form/div[4]/fieldset/textarea)").send_keys("Hey, Tester is testing the testing area")
    time.sleep(2)
    # Entering the Plain Text
    driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/form/div[5]/fieldset/textarea)").send_keys("Tester is testing the testing area")
    time.sleep(2)
    # Click on radio button
    driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/form/div[6]/fieldset[1]/div/label").click()
    time.sleep(2)
    # CLick on "How to create an email" link
    driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/form/div[4]/fieldset/div/a)").click()
    time.sleep(2)
    # Click on "Save" button
    driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/form/div[8]/a[2])").click()
    time.sleep(2)
    print("Follow up email created ✓")
except NoSuchElementException:
    print("*****Follow up email cannot be created*****")

try:
    # Edit email
    driver.find_element(By.XPATH,"(//*[@id='emails-page']/div[1]/div/div[2]/div[2]/div[2]/div/div/div[3]/div[1]/a[1])").click()
    time.sleep(2)
    # Entering name
    driver.find_element(By.ID,"name").send_keys("Test NEW")
    time.sleep(2)
    # Entering Subject line
    driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/form/div[3]/fieldset/input)").send_keys("Testing the Follow up, NEW")
    time.sleep(2)
    # Entering the HTML Email
    driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/form/div[4]/fieldset/textarea)").send_keys("Hey, Tester is testing the testing area. NEW")
    time.sleep(2)
    # Entering the Plain Text
    driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/form/div[5]/fieldset/textarea)").send_keys("Tester is testing the testing area. NEW")
    time.sleep(2)
    # Click on radio button
    driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/form/div[6]/fieldset[1]/div/label)").click()
    time.sleep(2)
    # CLick on "How to create an email" link
    driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/form/div[4]/fieldset/div/a)").click()
    time.sleep(2)
    # Click on "Save" button
    driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/form/div[8]/a[2])").click()
    time.sleep(2)
    print("Follow up email edited ✓")
except NoSuchElementException:
    print("*****Cannot edit follow-up email*****")

try:
    # CLick on "Preview"
    driver.find_element(By.XPATH,"(//*[@id='emails-page']/div[1]/div/div[2]/div[2]/div[2]/div/div/div[3]/div[1]/a[2])").click()
    time.sleep(2)
    print("Preview clicked ✓")
except NoSuchElementException:
    print("*****Preview cannot be shown*****")

try:
    # CLick on "Test"
    driver.find_element(By.XPATH,"(//*[@id='emails-page']/div[1]/div/div[2]/div[2]/div[2]/div/div/div[3]/div[1]/a[3])").click()
    time.sleep(6)
    # Add inputs in "Add respondents"
    driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/div[2]/div[3]/div[2]/div/a)").click()
    time.sleep(2)
    driver.find_element(By.ID,"salutation").send_keys("Mr")
    driver.find_element(By.ID,"first-name").send_keys("Test4")
    driver.find_element(By.ID,"email").send_keys("test17@xyz.com")
    time.sleep(2)
    driver.find_element(By.XPATH,"(/html/body/div[2]/div/div[2]/div/div/form/div/div[7]/a[2])").click()
    time.sleep(4)
    print("Respondent added ✓")
except NoSuchElementException:
    print("*****Respondents cannot be added*****")

try:
    # CLick "Send test emails" button
    driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/div[2]/div[3]/a)").click()
    time.sleep(2)
    # Send now button
    driver.find_element(By.XPATH,"(/html/body/div[2]/div/div[2]/div/div/div/a[2])").click()
    time.sleep(4)
    print("Follow up email send ✓")
except NoSuchElementException:
    print("*****Cannot send email*****")

try:
    # Click on "Download unsubscribes" button
    driver.find_element(By.XPATH,"(//*[@id='emails-page']/div[1]/div[1]/div[1]/div[2]/a)").click()
    time.sleep(2)
    print("Download Unsubscribes clicked ✓")
except NoSuchElementException:
    print("*****Cannot Download unsubscribes*****")

try:
    # CLICK on EDIT
    driver.find_element(By.XPATH,"(//*[@id='emails-page']/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div[3]/div[1]/a[1])").click()
    time.sleep(2)
    # CLICK on Delete
    driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/form/div[1]/div/a/i)").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"(/html/body/div[2]/div/div[2]/div/div/div/a[2])").click()
    time.sleep(2)
    print("Follow-up email deleted ✓")
except NoSuchElementException:
    print("*****Cannot Delete follow-up*****")

try:
    # CLICK on EDIT
    driver.find_element(By.XPATH,"(/html/body/form/div[2]/div/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/div[3]/div[1]/a[1])").click()
    time.sleep(2)
    # CLICK on Delete
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[1]/div/a/i)").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(/html/body/div[2]/div/div[2]/div/div/div/a[2])").click()
    time.sleep(2)
    print("Email deleted ✓")
except NoSuchElementException:
    print("*****Cannot Delete Email*****")

print("############ ALL-VUE SECTION PAGE ############")

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

driver.switch_to.window(driver.window_handles[0])

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

driver.switch_to.window(driver.window_handles[0])

# Select Company drop-down
try:
    driver.find_element(By.XPATH, "(//*[@id='customerportal-page']/form/div[2]/a)").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div[2]/div)").click()
    time.sleep(2)
    driver.find_element(By.ID, "react-select-2-option-167").click()
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

# Removing Quota
try:
    driver.find_element(By.XPATH, "(//*[@id='customerportal-page']/form/div[2]/fieldset/fieldset/div[2]/div)").click()
    driver.find_element(By.XPATH,
                        "(//*[@id='customerportal-page']/form/div[2]/fieldset/fieldset/div[2]/div/div/button/i)").click()
    time.sleep(2)
    print("Quota removed ✓")
except NoSuchElementException:
    print("*****Quota not removed *****")

# Click on 'Share Files' button
try:
    driver.find_element(By.XPATH, "(//*[@id='customerportal-page']/form/div[2]/fieldset/div[4]/div[1]/a)").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/div/a)").click()
    time.sleep(2)
    print("Share Files button clicked ✓")
except NoSuchElementException:
    print("*****Share Files button not clicked *****")

driver.switch_to.window(driver.window_handles[0])

# Changing the notification email
try:
    driver.find_element(By.XPATH, "(//*[@id='customerportal-page']/form/div[2]/fieldset/div[4]/input)").clear()
    time.sleep(2)
    driver.find_element(By.XPATH, "(//*[@id='customerportal-page']/form/div[2]/fieldset/div[4]/input)").send_keys(
        "abhinav.rawat@savanta.com")
    time.sleep(2)
    print("Notification email changed ✓")
except NoSuchElementException:
    print("*****Notification email not changed *****")

print("############ LINK FEEDBACK  PAGE ############")

# go to Link feedback Page
driver.find_element(By.XPATH, "//*[@id='pageLinks']/div[1]/a[6]").click()
time.sleep(5)


# Upload button
try:
    driver.switch_to.frame("LinkFeedbackIFrame")
    driver.find_element(By.XPATH, "//*[@id='import_modal_button_b3f708008f']").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//*[@id='import_modal_close_b3f708008f']").click()
    time.sleep(2)
    print("Upload button clicked ✓")
except NoSuchElementException:
    print("*****Upload not clicked *****")

# Help button
try:
    driver.find_element(By.XPATH, "//*[@id='help_modal_button_b3f708008f']").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//*[@id='help_modal_close_b3f708008f']").click()
    time.sleep(2)
    print("Help button clicked ✓")
except NoSuchElementException:
    print("*****Help not clicked *****")

# add new button
try:
    button = driver.find_element(By.CLASS_NAME, "pgui-add")
    button.click()
    time.sleep(2)
    driver.find_element(By.NAME, "qid_edit").send_keys("11")
    time.sleep(2)
    driver.find_element(By.NAME, "details_edit").send_keys("Testing")
    time.sleep(2)
    driver.find_element(By.NAME, "details_ops_edit").send_keys("Testing Text Area 2")
    time.sleep(2)
    driver.find_element(By.NAME, "statusid_edit").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/div[1]/div/form/div[3]/fieldset/div[6]/div[2]/div/select/option[5]").click()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "btn.btn-primary.js-save.js-primary-save").click()
    time.sleep(2)
    print("Added new Feedback ✓")
except NoSuchElementException:
    print("*****Not abel to add new Feedback *****")


# External Button
try:
    driver.find_element(By.XPATH, "//*[@id='ext_modal_button_b3f708008f']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='ext_modal_b3f708008f']/div/a").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='ext_modal_close_b3f708008f']").click()
    time.sleep(2)
    print("External new button clicked ✓")
except NoSuchElementException:
    print("*****External button not clicked *****")


# Export Button
try:
    driver.find_element(By.CLASS_NAME, "btn.btn-default.dropdown-toggle").click()
    time.sleep(2)
    print("Export new button clicked ✓")
except NoSuchElementException:
    print("*****Export button not clicked *****")

# Filter Icon
try:
    driver.find_element(By.CLASS_NAME, "btn.btn-default.js-filter-builder-open").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[4]/div[5]/div/div/div[3]/button[1]").click()
    time.sleep(2)
    print("Filter Icon button clicked ✓")
except NoSuchElementException:
    print("*****Filter Icon button not clicked *****")

"""
# Sort Icon
driver.find_element(By.ID, "//*[@id='multi-sort-dbo_SurveyQCLog_feedbackGrid_64e3375ea8be9']").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[4]/div[4]/div/div/div[1]/button").click()
time.sleep(2)
"""

# Selection
try:
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[4]/table/thead/tr/th[1]/input").click()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "btn.btn-info.dropdown-toggle").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[4]/div[1]/div[1]/div[4]/div/ul/li[1]/a").click()
    time.sleep(2)
    print("All Selection clicked and removed ✓")
except NoSuchElementException:
    print("*****All selection not clicked or not removed *****")

