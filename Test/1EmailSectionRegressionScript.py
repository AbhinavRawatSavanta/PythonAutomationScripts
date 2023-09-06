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

driver.find_element(By.ID,"search-box").send_keys("6299")
time.sleep(2)

driver.find_element(By.XPATH, "(//table[@class='data-table']/descendant::tbody/descendant::a)[1]").click()
time.sleep(2)

# go to Email Sends Page
driver.find_element(By.XPATH, "(//*[@id='pageLinks']/div[1]/a[4])").click()
time.sleep(2)

"""

try:    
    driver.find_element(By.XPATH, "(/html/body/form/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/a[4])").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/div[4]/a[2])").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/div[2]/a[2])").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[2]/label)").click()
    time.sleep(2)
    # Selecting the Segment
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[2]/div/div/div/div/div/div[1]/div[2])").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"(//*[@id='react-select-3-option-0'])").click()
    time.sleep(2)
    # Selecting the "MAIN" Segment
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[2])").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"(//*[@id='react-select-4-option-0'])").click()
    time.sleep(2)
    # Click on Add Condition
    driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/form/div[2]/div/div/div/div[3]/a)").click()
    time.sleep(2)
    # Selecting the Email Address
    driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/form/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2])").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"(//div[text()='Email addresses'])").click()
    time.sleep(2)
    # Adding the Email Address
    driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/form/div[2]/div/div/div[2]/div[3]/textarea)").send_keys("abc2@xyz.com")
    time.sleep(2)
    # Click on NEXT button
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/a[2]").click()
    time.sleep(2)
    # Click on NEXT button
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[3]/a[2]").click()
    time.sleep(2)
    # CLick on Full Preview link
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/div[1]/div[1]/a").click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)
    # CLick on Send Emails Button
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[3]/a[2]").click()
    time.sleep(2)
    # Confirmation window click
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/a[2]").click()
    time.sleep(2)
    print("Email Send to MAIN segment and Specific user (Condition 1 Complete ) ✓")
except NoSuchElementException:
    print("*****Email cannot be send to MAIN segment and Specific user *****")


try:
    driver.find_element(By.XPATH, "(/html/body/form/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/a[4])").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/div[4]/a[2])").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/div[2]/a[2])").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[2]/label)").click()
    time.sleep(2)
    # Selecting the Email Addresses
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[2]/div/div/div/div/div/div[1]/div[2])").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(//*[@id='react-select-3-option-1'])").click()
    time.sleep(2)
    # Input Email Address
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[2]/div/div/div/div[2]/textarea)").send_keys("abc3@xyz.com")
    time.sleep(2)
    # Click on Add Condition
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[2]/div/div/div/div[3]/a)").click()
    time.sleep(2)
    # Selecting Language
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2])").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(//div[text()='Language'])").click()
    time.sleep(2)
    # Selecting "English" Language
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[2]/div/div/div[2]/div[3]/div/div/div[1]/div[2])").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(//div[text()='English'])").click()
    time.sleep(2)
    # Click on NEXT button
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/a[2]").click()
    time.sleep(2)
    # Click on NEXT button
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[3]/a[2]").click()
    time.sleep(2)
    # CLick on Full Preview link
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/div[1]/div[1]/a").click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)
    # CLick on Send Emails Button
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[3]/a[2]").click()
    time.sleep(2)
    # Confirmation window click
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/a[2]").click()
    time.sleep(2)
    print("Email Send to Specific user and having Specific Language (Condition 2 Complete ) ✓")
except NoSuchElementException:
    print("*****Email cannot be send to Specific user and having Specific Language *****")


try:
    driver.find_element(By.XPATH, "(/html/body/form/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/a[4])").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/div[4]/a[2])").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/div[2]/a[2])").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[2]/label)").click()
    time.sleep(2)
    # Selecting the Segment
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[2]/div/div/div/div/div/div[1]/div[2])").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"(//*[@id='react-select-3-option-0'])").click()
    time.sleep(2)
    # Selecting the "MAIN" Segment
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[2])").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"(//*[@id='react-select-4-option-0'])").click()
    time.sleep(2)
    # Click on Add Condition
    driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/form/div[2]/div/div/div/div[3]/a)").click()
    time.sleep(2)
    # Selecting Language
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2])").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(//div[text()='Language'])").click()
    time.sleep(2)
    # Selecting "English" Language
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[2]/div/div/div[2]/div[3]/div/div/div[1]/div[2])").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(//div[text()='English'])").click()
    time.sleep(2)
    # Click on NEXT button
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/a[2]").click()
    time.sleep(2)
    # Click on NEXT button
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[3]/a[2]").click()
    time.sleep(2)
    # CLick on Full Preview link
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/div[1]/div[1]/a").click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)
    # CLick on Send Emails Button
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[3]/a[2]").click()
    time.sleep(2)
    # Confirmation window click
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/a[2]").click()
    time.sleep(2)
    print("Email Send to MAIN segment and having Specific Language (Condition 3 Complete ) ✓")
except NoSuchElementException:
    print("*****Email cannot be send to MAIN segment and having Specific Language *****")

try:
    driver.find_element(By.XPATH, "(/html/body/form/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/a[4])").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/div[4]/a[2])").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/div[2]/a[2])").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[2]/label)").click()
    time.sleep(2)
    # Selecting the Company
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[2]/div/div/div/div/div/div[1]/div[2])").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(//*[@id='react-select-3-option-2'])").click()
    time.sleep(2)
    # Entering the Company Name
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[2]/div/div/div/div[2]/input)").send_keys("QA")
    time.sleep(2)
    # Click on Add Condition
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[2]/div/div/div/div[3]/a)").click()
    time.sleep(2)
    # Selecting Language
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2])").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(//div[text()='Precoded data'])").click()
    time.sleep(2)
    # Entering the Precoded Data
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[2]/div/div/div[2]/div[3]/input)").send_keys("11")
    time.sleep(2)
    # Click on NEXT button
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/a[2]").click()
    time.sleep(2)
    # Click on NEXT button
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[3]/a[2]").click()
    time.sleep(2)
    # CLick on Full Preview link
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/div[1]/div[1]/a").click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)
    # CLick on Send Emails Button
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[3]/a[2]").click()
    time.sleep(2)
    # Confirmation window click
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/a[2]").click()
    time.sleep(2)
    print("Email Send to Specific Company and having Specific Precoded Data (Condition 4 Complete ) ✓")
except NoSuchElementException:
    print("*****Email cannot be send to Specific Company and having Specific Precoded Data *****")



try:
    driver.find_element(By.XPATH, "(/html/body/form/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/a[4])").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/div[4]/a[2])").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/div[2]/a[2])").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[2]/label)").click()
    time.sleep(2)
    # Selecting the Segment
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[2]/div/div/div/div/div/div[1]/div[2])").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"(//*[@id='react-select-3-option-0'])").click()
    time.sleep(2)
    # Selecting the "MAIN" Segment
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[2])").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"(//*[@id='react-select-4-option-0'])").click()
    time.sleep(2)
    # Click on Add Condition
    driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/form/div[2]/div/div/div/div[3]/a)").click()
    time.sleep(2)
    # Selecting the Email Address
    driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/form/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2])").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"(//div[text()='Email addresses'])").click()
    time.sleep(2)
    # Adding the Email Address
    driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/form/div[2]/div/div/div[2]/div[3]/textarea)").send_keys("abc2@xyz.com")
    time.sleep(2)
    # Click on Add Condition
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[2]/div/div/div[2]/div[4]/a)").click()
    time.sleep(2)
    # Selecting Language
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[2]/div/div/div[3]/div[2]/div/div[1]/div[2])").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(//div[text()='Language'])").click()
    time.sleep(2)
    # Selecting "English" Language
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[2]/div/div/div[3]/div[3]/div/div/div[1]/div[2])").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(//div[text()='English'])").click()
    time.sleep(2)
    # Click on NEXT button
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/a[2]").click()
    time.sleep(2)
    # Click on NEXT button
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[3]/a[2]").click()
    time.sleep(2)
    # CLick on Full Preview link
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/div[1]/div[1]/a").click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)
    # CLick on Send Emails Button
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[3]/a[2]").click()
    time.sleep(2)
    # Confirmation window click
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/a[2]").click()
    time.sleep(2)
    print("Email Send to MAIN Segment and to Specific user and having Specific Language (Condition 5 Complete ) ✓")
except NoSuchElementException:
    print("*****Email cannot be send to MAIN Segment and to Specific user and having Specific Language *****")

"""

try:
    driver.find_element(By.XPATH, "(/html/body/form/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/a[4])").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/div[4]/a[2])").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/div[2]/a[2])").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[2]/label)").click()
    time.sleep(2)
    # Selecting the Segment
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[2]/div/div/div/div/div/div[1]/div[2])").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"(//*[@id='react-select-3-option-0'])").click()
    time.sleep(2)
    # Selecting the "MAIN" Segment
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[2])").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"(//*[@id='react-select-4-option-0'])").click()
    time.sleep(2)
    # Click on Add Condition
    driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/form/div[2]/div/div/div/div[3]/a)").click()
    time.sleep(2)
    # Selecting the Email Address
    driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/form/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2])").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"(//div[text()='Email addresses'])").click()
    time.sleep(2)
    # Adding the Email Address
    driver.find_element(By.XPATH,"(/html/body/div/div/div[2]/div/div/form/div[2]/div/div/div[2]/div[3]/textarea)").send_keys("abc2@xyz.com")
    time.sleep(2)
    # Click on Add Condition
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[2]/div/div/div[2]/div[4]/a)").click()
    time.sleep(2)
    # Selecting Language
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[2]/div/div/div[3]/div[2]/div/div[1]/div[2])").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(//div[text()='Language'])").click()
    time.sleep(2)
    # Selecting "English" Language
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[2]/div/div/div[3]/div[3]/div/div/div[1]/div[2])").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(//div[text()='English'])").click()
    time.sleep(2)
    # Click on Add Condition
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[2]/div/div/div[3]/div[4]/a)").click()
    time.sleep(2)
    # Selecting the Company
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/form/div[2]/div/div/div[4]/div[2]/div/div[1]/div[2])").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(//div[text()='Company'])").click()
    time.sleep(2)
    # Entering the Company Name
    driver.find_element(By.XPATH, "(/html/body/div[1]/div/div[2]/div/div/form/div[2]/div/div/div[4]/div[3]/input)").send_keys("QA")
    time.sleep(2)
    # Click on NEXT button
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/a[2]").click()
    time.sleep(2)
    # Click on NEXT button
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[3]/a[2]").click()
    time.sleep(2)
    # CLick on Full Preview link
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/div[1]/div[1]/a").click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)
    # CLick on Send Emails Button
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[3]/a[2]").click()
    time.sleep(2)
    # Confirmation window click
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/a[2]").click()
    time.sleep(2)
    print("Email Send to MAIN Segment and to Specific user and having Specific Language and to a Specific Company (Condition 6 Complete ) ✓")
except NoSuchElementException:
    print("*****Email cannot be send to MAIN Segment and to Specific user and having Specific Language and to a Specific Company *****")
