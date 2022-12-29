import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

"""Login to Page"""
driver.get('https://www.db4free.net/')

"""Click on PHP My Admin"""
driver.find_element(By.PARTIAL_LINK_TEXT, "phpMyAdmin").click()

time.sleep(5)

# switch to tab
driver.switch_to.window(driver.window_handles[1])

"""Enter UserName"""
driver.find_element(By.ID, "input_username").send_keys("Admin")
"""Enter Password"""
driver.find_element(By.ID, "input_password").send_keys("admin123")

"""Click Login Button"""
driver.find_element(By.ID, "input_go").click()

"""Capture Error Message"""
print(driver.find_element(By.XPATH, "//div[contains(text(),'Access denied')]").text)

print(driver.title.split(' - ')[0])

# check
driver.close()

# switch back
driver.switch_to.window(driver.window_handles[0])

print(driver.title.split(' - ')[0])

driver.quit()
