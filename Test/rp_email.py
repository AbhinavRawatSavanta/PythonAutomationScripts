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
except NoSuchElementException:
    print("*****Email cannot be edited*****")

try:
    # Test Email
    driver.find_element(By.XPATH,"//*[@id='emails-page']/div[1]/div/div[2]/div[1]/div[1]/div[3]/div[1]/a[3]").click()
    time.sleep(4)

# Click on "View deliverability tests" link
#driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[1]").click()
#time.sleep(2)
#driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div[3]/a").click()
#time.sleep(2)

# Click on "View spam report" link
#driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]").click()
#time.sleep(2)
#driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div[3]/a").click()
#time.sleep(2)


    # Add respondent in Test Email
    driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/div[2]/div[3]/div[2]/div/a)").click()
    time.sleep(2)

    # Add inputs in "Add respondents"
    driver.find_element(By.ID,"salutation").send_keys("Mr")
    driver.find_element(By.ID,"first-name").send_keys("Test1")
    driver.find_element(By.ID,"email").send_keys("test1@xyz.com")
    time.sleep(2)
    driver.find_element(By.XPATH,"(/html/body/div[2]/div/div[2]/div/div/form/div/div[7]/a[2])").click()
    time.sleep(2)
except NoSuchElementException:
    print("*****Respondents cannot be added*****")

try:
    # CLick "Send test emails" button
    driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/div[2]/div[3]/a)").click()
    time.sleep(2)
    # Send now button
    driver.find_element(By.XPATH,"(/html/body/div[2]/div/div[2]/div/div/div/a[2])").click()
    time.sleep(4)
except NoSuchElementException:
    print("*****Email cannot be send*****")

try:
    # Edit email
    driver.find_element(By.XPATH,"(//*[@id='emails-page']/div[1]/div/div[2]/div[2]/div[2]/div/div/div[3]/div[1]/a[1])").click()
    time.sleep(2)
    # Entering name
    driver.find_element(By.ID,"(name)").send_keys("Test")
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
    driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/form/div[6]/fieldset[1]/div/label)").click()
    time.sleep(2)
    # CLick on "How to create an email" link
    driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/form/div[4]/fieldset/div/a)").click()
    time.sleep(2)
    # Click on "Save" button
    driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/form/div[8]/a[2])").click()
    time.sleep(2)
except NoSuchElementException:
    print("*****Follow up email cannot be created*****")

try:
    # CLick on "Preview"
    driver.find_element(By.XPATH,"(//*[@id='emails-page']/div[1]/div/div[2]/div[2]/div[2]/div/div/div[3]/div[1]/a[2])").click()
    time.sleep(2)
except NoSuchElementException:
    print("*****Preview cannot be shown*****")

try:
    # CLick on "Test"
    driver.find_element(By.XPATH,"(//*[@id='emails-page']/div[1]/div/div[2]/div[2]/div[2]/div/div/div[3]/div[1]/a[3])").click()
    time.sleep(2)
    # Add inputs in "Add respondents"
    driver.find_element(By.ID,"salutation").send_keys("Mrs")
    driver.find_element(By.ID,"first-name").send_keys("Test2")
    driver.find_element(By.ID,"email").send_keys("test2@xyz.com")
    time.sleep(2)
    driver.find_element(By.XPATH,"(/html/body/div[2]/div/div[2]/div/div/form/div/div[7]/a[2])").click()
    time.sleep(2)
except NoSuchElementException:
    print("*****Respondents cannot be added*****")

try:
    # CLick "Send test emails" button
    driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/div[2]/div[3]/a)").click()
    time.sleep(2)
    # Send now button
    driver.find_element(By.XPATH,"(/html/body/div[2]/div/div[2]/div/div/div/a[2])").click()
    time.sleep(4)
except NoSuchElementException:
    print("*****Cannot send email*****")

try:
    # Adding new "Follow up email"
    driver.find_element(By.XPATH,"(//*[@id='emails-page']/div[1]/div[1]/div[2]/div[2]/div[2]/a)").click()
    time.sleep(4)
    #
    driver.find_element(By.ID, "(name)").send_keys("ADDING")
    time.sleep(4)
    #
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[3]/fieldset/input)").send_keys("ADDING SUBJECT")
    time.sleep(4)
    #
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[4]/fieldset/textarea)").send_keys("ADDING TEXT AREA")
    time.sleep(4)
    #
    driver.find_element(By.ID, "(unsubscribeOverride)").click()
    time.sleep(4)
    #
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[8]/a[2])").click()
    time.sleep(4)
except NoSuchElementException:
    print("*****Cannot add follow-up email*****")

try:
    # Edit email
    driver.find_element(By.XPATH,"(//*[@id='emails-page']/div[1]/div/div[2]/div[2]/div[2]/div/div/div[3]/div[1]/a[1])").click()
    time.sleep(2)
    # Entering name
    driver.find_element(By.ID,"(name)").send_keys("Test NEW")
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
except NoSuchElementException:
    print("*****Cannot edit follow-up email*****")

#try:
    ## Click on "Download unsubscribes" button
    #driver.find_element(By.XPATH,"(//*[@id='emails-page']/div[1]/div[1]/div[1]/div[2]/a)").click()
    #time.sleep(2)
#except NoSuchElementException:
    #print("*****Cannot Download unsubscribes*****")

try:
    # CLICK on EDIT
    driver.find_element(By.XPATH,"(//*[@id='emails-page']/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div[3]/div[1]/a[1])").click()
    time.sleep(2)
    # CLICK on Delete
    driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/form/div[1]/div/a/i)").click()
    time.sleep(2)
except NoSuchElementException:
    print("*****Cannot Delete follow-up*****")