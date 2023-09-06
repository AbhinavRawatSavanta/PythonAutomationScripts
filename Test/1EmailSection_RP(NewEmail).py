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

driver.find_element(By.ID,"search-box").send_keys("6128")
time.sleep(2)

driver.find_element(By.XPATH, "(//table[@class='data-table']/descendant::tbody/descendant::a)[1]").click()
time.sleep(2)

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
    #driver.find_element(By.XPATH, "(//*[@id='react-select-3-input'])").send_keys("surveys@savanta-mail.com")
    #driver.find_element(By.ID, "react-select-3-listbox").click()
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
    time.sleep(4)

    # Add respondent in Test Email
    driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/div[2]/div[3]/div[2]/div/a)").click()
    time.sleep(2)

    # Add inputs in "Add respondents"
    driver.find_element(By.ID,"salutation").send_keys("Mr")
    driver.find_element(By.ID,"first-name").send_keys("Test3")
    driver.find_element(By.ID,"email").send_keys("test4@xyz.com")
    time.sleep(2)
    driver.find_element(By.XPATH,"(/html/body/div[2]/div/div[2]/div/div/form/div/div[7]/a[2])").click()
    time.sleep(2)
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

try:
    # CLICK on EDIT
    driver.find_element(By.XPATH,"(/html/body/form/div[2]/div/div[2]/div/div[1]/div/div[2]/div[1]/div/div[3]/div[1]/a[1])").click()
    time.sleep(2)
    # CLICK on Delete
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[1]/div/a/i)").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(/html/body/div[2]/div/div[2]/div/div/div/a[2])").click()
    time.sleep(2)
    print("Follow-up email deleted ✓")
except NoSuchElementException:
    print("*****Cannot Delete follow-up*****")