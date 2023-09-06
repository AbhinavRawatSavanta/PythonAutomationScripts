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
    driver.find_element(By.XPATH, "(//*[@id='pageLinks']/div[1]/a[2])").click()
    time.sleep(2)

except NoSuchElementException:
    print("Error occurred in Going to Quota Page")

# to click and select the "Quotas" drop-down
#try:
#    dropdown = driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/div[1]/div[1]/div[2]/div/div[1]/div[2])")
#    dropdown.click()
#    options_locator = (By.CLASS_NAME, "react-select-style__single-value css-qc6sy-singleValue")
#    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(options_locator))
#    option_text = "Gender"
#    option = driver.find_element(By.CLASS_NAME, f"quota-item' and text()='{option_text}']")
#    option.click()
#    time.sleep(2)

#except NoSuchElementException:
#    print("*****Can't open the drop-down*****")

#try:
#    DROPDOWN_ITEM = 1
#    dropdown_item_1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,f'//*[@id="quotas-page"]/form/div[1]/div[1]/div[2]/div/div[1]/div[2][{DROPDOWN_ITEM} + 2]')))
#    dropdown_item_1.click()


#except NoSuchElementException:
#    print("*****Can't open the drop-down*****")

######
driver.find_element(By.XPATH, "//*[@id='quotas-page']/form/div[1]/div[1]/div[2]/div/div[1]/div[2]").click()
driver.find_element(By.XPATH, "//*[@id='react-select-2-input']").send_keys("Gender")
driver.find_element(By.ID, "react-select-2-listbox").click()
time.sleep(3)

# to click on "Edit" button
try:
    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/div[2]/div[3]/a)").click()
    time.sleep(2)
    print('Edit button clicked')
except NoSuchElementException:
    print("*****Edit button not clicked*****")

try:
    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/table/tbody/tr/td[4]/input)").send_keys("11")
    time.sleep(2)
    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/table/tbody/tr/td[7]/input)").send_keys("11")
    time.sleep(2)
    print('Input send')

except NoSuchElementException:
    # Handle the error for Task 1
    print("*****Inputs not send*****")

try:
    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/div[2]/div[3]/a[3])").click()
    time.sleep(2)
#    print('"Save Changes" button clicked')
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div/div/a[2])").click()
    time.sleep(2)
    print('Saved changes')

except NoSuchElementException:
    print("*****Can't save changes*****")

# to click on "Edit" button
try:
    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/div[2]/div[3]/a)").click()
    time.sleep(2)
    print('Edit button clicked again')
except NoSuchElementException:
    print("*****Edit button not clicked again*****")


# to click on "Show Advanced" button
try:
    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/div[2]/div[3]/a[1])").click()
    time.sleep(2)
    print('Show Advanced button clicked')
except NoSuchElementException:
    print("*****Show Advanced button not clicked*****")

# to click on "Hide Advanced" button
try:
    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/div[2]/div[3]/a[1])").click()
    time.sleep(2)
    print('Hide Advanced button clicked')
except NoSuchElementException:
    print("*****Hide Advanced button not clicked*****")

# to click on "Cancel" button
try:
    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/div[2]/div[3]/a[2])").click()
    time.sleep(2)
    print('Cancel button clicked')
except NoSuchElementException:
    print("*****Cancel button not clicked*****")

# to click on "Download to Excel" button
try:
    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/div[1]/div[2]/a[1])").click()
    time.sleep(2)
    print('Download to Excel button clicked')
except NoSuchElementException:
    print("*****Download to Excel button not clicked*****")

# to click on "Recalculate Quota" button
try:
    driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/div[1]/div[2]/a[3])").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(/html/body/div/div/div[2]/div/div[1]/div/a[2])").click()
    time.sleep(2)
    print('Recalculate Quota button clicked')
except NoSuchElementException:
    print("*****Recalculate Quota button not clicked*****")


#driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/table/tbody/tr/td[8]/div/div)").click()
#time.sleep(2)

#dropdown = Select(driver.find_element(By.XPATH, "(//*[@id='quotas-page']/form/table/tbody/tr/td[8]/div/div/div[2]/div)"))
#dropdown.select_by_value("Priority 1 (Highest)")



#---------------------------------------------------------

# WORKING CLICK ON DROP-DOWN

#dropdown_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//*[@id='quotas-page']/form/table/tbody/tr/td[8]/div/div/div[2]/div)")))
#dropdown_element.click()

#-----------------------------------------------------------




#option_xpath = "//*[@id='quotas-page']/form/table/tbody/tr/td[8]/div/div/div[1]/div[1]"
#option_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
#actions = ActionChains(driver)
#actions.move_to_element(option_element).perform()
#option_element.click()

#wait = WebDriverWait(driver, 10)
#option_element = wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@id='quotas-page']/form/table/tbody/tr/td[8]/div/div/div[1]/div[1])"))).click()

