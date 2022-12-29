import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

"""1.  Launch the web site https://www.phptravels.net/home"""
driver.get('https://www.phptravels.net/')

"""2.  Goto Flights"""
driver.find_element(By.ID, "flights-tab").click()

"""3.  Choose "FROM" location as "Los Angeles" (LAX)"""
driver.find_element(By.XPATH, "//input[@name='from']").send_keys("LAX")
driver.find_element(By.XPATH, "//div[@data-index='0']").click()

"""4.  Choose "TO" as "Dallas" (DAL)"""
driver.find_element(By.XPATH, "//input[@name='to']").send_keys("DAL")
driver.find_element(By.XPATH, "//div[@data-index='0']").click()

"""5.  Set the travel date “2022-05-30”"""
driver.find_element(By.XPATH, "//input[@id='departure']").clear()
driver.find_element(By.XPATH, "//input[@id='departure']").send_keys("30-05-2022")
driver.find_element(By.XPATH, "//input[@id='departure']").click()

"""6.  Adult as 2"""
driver.find_element(By.XPATH, "//span[contains(@class, 'flight')]").click()
driver.find_element(By.XPATH, "//input[@id='fadults']").clear()
driver.find_element(By.XPATH, "//input[@id='fadults']").send_keys(2)
driver.find_element(By.XPATH, "//span[contains(@class, 'flight')]").click()

"""7.  Get the first flight details and print"""
driver.find_element(By.ID, "flights-search").click()
print(driver.find_element(By.XPATH, "//img[@alt='no results']").get_attribute('alt'))
img = driver.find_element(By.XPATH, "//img[@alt='no results']").get_attribute('src')
driver.get(img)
time.sleep(5)

"""8.  Close the browser"""
driver.quit()
