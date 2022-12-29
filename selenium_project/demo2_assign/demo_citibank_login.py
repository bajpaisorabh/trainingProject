import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

wait = WebDriverWait(driver, 20)

"""Login to Page"""
driver.get('https://www.online.citibank.co.in/')

"""For Cookies Check"""
driver.find_element(By.XPATH, "//a[@class= 'fancybox-item fancybox-close']").click()

"""Click on Login"""
driver.find_element(By.XPATH, "//span[@class= 'txtSign']").click()

"""Click on Forgot User ID"""
driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.XPATH, "//div[@onclick='ForgotUserID();']").click()

"""Choose Credit Card Option"""
driver.find_element(By.XPATH, "//div[@class='sbHolder']").click()
driver.find_element(By.XPATH, "//li/a[@rel='Credit Card']").click()

# driver.switch_to.alert.accept()

"""Enter Credit Card No as 4545 5656 8887 9998 """
driver.find_element(By.ID, "citiCard1").send_keys(4545)
driver.find_element(By.ID, "citiCard2").send_keys(5656)
driver.find_element(By.ID, "citiCard3").send_keys(8887)
driver.find_element(By.ID, "citiCard4").send_keys(9998)
# driver.find_element(By.XPATH, "//input[@name='fldLoginUserId']").send_keys("919854")
# driver.find_element(By.XPATH, "//img[@alt='Go']").click()

"""Enter CVV"""
driver.find_element(By.ID, "cvvnumber").send_keys(123)

"""Enter Date 14.4.2022 """
#driver.find_element(By.ID, "bill-date-long").send_keys("14/04/2022")
driver.execute_script("document.querySelector('#bill-date-long').value = '14/04/2022'")

"""Click on Footer Logo"""
driver.find_element(By.XPATH, "//div[@class='footerLogo']").click()

"""Print Terms and Cond"""
print(driver.find_element(By.XPATH, "//div[@class='TermsAndConditions']").text)

"""Click on Proceed"""
driver.find_element(By.XPATH, "//div/input[@value='PROCEED']").click()

print(driver.title.split('-')[0])
