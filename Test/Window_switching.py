import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


serv_obj=Service("C:/Users/AbhinavRawat/WebDrivers/edgedriver_win64/msedgedriver.exe")
driver=webdriver.Edge(service=serv_obj)

driver.maximize_window()
driver.get("https://researchportal.beta.savanta.com/Surveys")
time.sleep(2)

driver.find_element(By.ID,"search-box").send_keys("6184")
time.sleep(2)

driver.find_element(By.XPATH, "(//table[@class='data-table']/descendant::tbody/descendant::a)[1]").click()
time.sleep(2)


driver.find_element(By.XPATH, "/html/body/form/div[2]/div/div[2]/div/div[3]/div[3]/div[2]/a/i").click()
time.sleep(2)

driver.switch_to.window(driver.window_handles[0])

# Click on Pause Survey
try:
    driver.find_element(By.XPATH, "/html/body/form/div[2]/div/div[2]/div/div[1]/div[2]/a[2]/i").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/a[2]").click()
    time.sleep(2)
    print("Survey Paused ✓")
except NoSuchElementException:
    print("*****Survey not paused *****")