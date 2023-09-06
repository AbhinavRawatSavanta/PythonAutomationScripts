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

