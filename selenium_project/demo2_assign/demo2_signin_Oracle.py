from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)

"""Login to Page"""
driver.get('https://www.oracle.com/in/database/')

"""For Cookies Check"""
# driver.switch_to.frame()
# if driver.find_element(By.XPATH, "//iframe[@class='truste_popframe']"):
#     time.sleep(5)
#     driver.find_element(By.XPATH, "//a[contains(text(), 'Accept all')]").click()

"""Click Login Button"""
driver.find_element(By.ID, "acctBtnLabel").click()

"""Click on Sign in"""
driver.find_element(By.XPATH, "//a[contains(text(),'Sign-In')]").click()

print(driver.title)
print(driver.current_url)

print(driver.find_element(By.XPATH, "//h2[contains(text(),'acc')]").text)

"""Enter UserName"""
driver.find_element(By.ID, "sso_username").send_keys("John")

"""Enter Password"""
driver.find_element(By.ID, "ssopassword").send_keys("John123")

"""Sign In"""

driver.find_element(By.ID, "signin_button").click()

time.sleep(5)
"""check with explict wait"""

"""Capture Error Message"""
err = driver.find_element(By.XPATH, "//div[contains(text(),'Invalid')]").text
print(err)

print(driver.title)

driver.quit()
