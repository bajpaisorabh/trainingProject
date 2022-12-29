from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

"""Login to Page"""
driver.get('https://www.db4free.net/phpMyAdmin/')

"""Enter UserName"""
driver.find_element(By.ID, "input_username").send_keys("Admin")
"""Enter Password"""
driver.find_element(By.ID, "input_password").send_keys("admin123")

"""Click Login Button"""
driver.find_element(By.ID, "input_go").click()

"""Capture Error Message"""
print(driver.find_element(By.XPATH, "//div[contains(text(),'Access denied')]").text)

print(driver.title)

# driver.quit()
