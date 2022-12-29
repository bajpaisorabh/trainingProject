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
driver.get('https://netbanking.hdfcbank.com/netbanking/IpinResetUsingOTP.htm')

"""Click on Go"""
driver.find_element(By.XPATH, "//img[@alt='Go']").click()

wait.until(expected_conditions.alert_is_present())

print(driver.switch_to.alert.text)

driver.switch_to.alert.accept()

"""Enter Customer Id"""
driver.find_element(By.XPATH, "//input[@name='fldLoginUserId']").send_keys("919854")
driver.find_element(By.XPATH, "//img[@alt='Go']").click()
