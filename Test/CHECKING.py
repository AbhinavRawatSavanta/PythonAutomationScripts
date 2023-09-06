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
    print("Add new button clicked ✓")
except NoSuchElementException:
    print("*****Add new button not clicked *****")
