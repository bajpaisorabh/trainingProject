import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

wait = WebDriverWait(driver, 20)

"""Login to Page"""
driver.get('https://netbanking.hdfcbank.com/netbanking/')

"""Switch to Frame"""
driver.switch_to.frame('login_page')

"""Enter User Name"""
wait.until(ec.presence_of_element_located((By.NAME, "fldLoginUserId")))
driver.find_element(By.NAME, "fldLoginUserId").send_keys("John")

"""Click on Continue"""
driver.find_element(By.LINK_TEXT, "CONTINUE")
driver.switch_to.default_content()
""""Switch back to default"""

time.sleep(5)
driver.quit()
