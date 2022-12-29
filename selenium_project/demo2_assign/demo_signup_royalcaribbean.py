import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

wait = WebDriverWait(driver, 20)

"""1.  Navigate onto https://www.royalcaribbean.com/"""
driver.get('https://www.royalcaribbean.com/')

"""2.  Close if any pop up. or load create an account page directly and do from step 4"""
driver.find_element(By.XPATH, "//div[@class='notification-banner__close']").click()

"""3.  Click Sign in and Click Create an account"""
driver.find_element(By.CSS_SELECTOR, "#rciHeaderSignIn").click()
driver.find_element(By.XPATH, "//a[contains(text(), 'Create')]").click()

"""4.  First Name as Dennis """
driver.find_element(By.CSS_SELECTOR, "#mat-input-3").send_keys("Dennis")

"""5.  Last Name as Rich"""
driver.find_element(By.CSS_SELECTOR, "#mat-input-4").send_keys("Rich")

"""6.  Select Month as April"""
driver.find_element(By.CSS_SELECTOR, "#mat-select-0").click()
driver.execute_script("document.getElementById('mat-option-3').click()")

"""7.  Day as 4"""
driver.find_element(By.CSS_SELECTOR, "#mat-select-2").click()
driver.execute_script("document.getElementById('mat-option-15').click()")

"""8.  Year as 1990"""
wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@data-placeholder='Year']")))
driver.find_element(By.XPATH, "//input[@data-placeholder='Year']").send_keys("1990")

"""9.  Country as India"""
driver.find_element(By.CSS_SELECTOR, "#mat-select-4").click()
driver.execute_script("document.getElementById('mat-option-145').click()")

"""10. Any email address and password """
# wait.until(ec.element_to_be_clickable(driver.find_element(By.XPATH, "//input[@data-placeholder='Email address']")))
driver.find_element(By.XPATH, "//input[@data-placeholder='Email address']").click()
driver.find_element(By.XPATH, "//input[@data-placeholder='Email address']").send_keys("drich@richierich.com")

driver.find_element(By.XPATH, "//input[@data-placeholder='Create new password']").send_keys("Mypassw0rd")

"""11. Select as “What was your first car's make or model?”"""
driver.find_element(By.CSS_SELECTOR, "#mat-select-6").click()
driver.execute_script("document.getElementById('mat-option-298').click()")

"""12. Type answer """
driver.find_element(By.CSS_SELECTOR, "#mat-input-7").send_keys(
    "Lamborghini Gallardo India Serie Speciale Edition (2013)")

"""13. Accept the terms and condition """
driver.find_element(By.XPATH, "//input[@aria-labelledby='agreements']/..").click()
time.sleep(5)

"""14. Click done"""
driver.find_element(By.XPATH, "//button[contains(text(), ' Done ')]").click()

driver.quit()
