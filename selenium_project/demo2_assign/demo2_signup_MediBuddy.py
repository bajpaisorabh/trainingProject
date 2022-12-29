import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 40)

"""Login to Page"""
driver.get('https://www.medibuddy.in/')

"""Click on Login"""
driver.find_element(By.LINK_TEXT, "Login").click()

"""Click on I have a Corporate Account"""
# wait.until(expected_conditions.visibility_of_any_elements_located(By.XPATH, "//div[@class='coperate']"))
driver.find_element(By.XPATH, "//div[text()='I have an Insurance/Corporate Account']").click()

"""CLick on Login using Username and Password"""
driver.find_element(By.XPATH, "//div[text()='Login using Username & Password']").click()

"""Enter UserName"""
driver.find_element(By.XPATH, "//input[@name= 'userName']").send_keys("John")

"""Click on Proceed"""
driver.find_element(By.XPATH, "//button[text()='Proceed']").click()

time.sleep(2)

"""Enter Password"""
# wait.until(expected_conditions.presence_of_element_located(By.XPATH, "//input[@name='password']")).send_keys("Pass")
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Pass")

"""Check Show Password Box"""
driver.find_element(By.XPATH, "//input[@ng-model= 'showMBLoginPassword']").click()

"""Click on Login Button"""
driver.find_element(By.XPATH, "//button[text()= 'Log in']").click()

"""Print Error Message"""
print(driver.find_element(By.XPATH, "//div[@ng-if='isPasswordWrong']").text)

print(driver.title.split('|')[1])

# driver.quit()
