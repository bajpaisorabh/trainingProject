from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

"""Login to Page"""
driver.get('https://nasscom.in/')

"""Click on Login Button"""
driver.find_element(By.CLASS_NAME, "login").click()

"""Click on Register Button"""
driver.find_element(By.XPATH, "//li[@data_get='register-app']").click()

"""Enter First Name"""
driver.find_element(By.ID, "edit-field-fname-reg-0-value").send_keys("John")

"""Enter First Name"""
driver.find_element(By.ID, "edit-field-lname-0-value").send_keys("Wick")

"""Enter email address"""
driver.find_element(By.ID, "edit-mail").send_keys("babayega@still-alive.com")

""""Enter Company Name"""
driver.find_element(By.ID, "edit-field-company-name-registration-0-value").send_keys("Continental, New York")

"""Enter Business Focus"""
set_bus_foc = Select(driver.find_element(By.ID, "edit-field-business-focus-reg"))
set_bus_foc.select_by_visible_text("IT Consulting")

# """Click Captcha"""
# driver.find_element(By.CLASS_NAME, "recaptcha-checkbox-border").click()

"""Click Register Button"""
driver.find_element(By.ID, "edit-submit--2").click()

print(driver.title.split(' | ')[0])

# driver.quit()
