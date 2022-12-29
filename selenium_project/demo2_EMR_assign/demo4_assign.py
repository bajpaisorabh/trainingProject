from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

wait = WebDriverWait(driver, 50)

action = webdriver.ActionChains(driver)

"""1.  Navigate onto http://demo.openemr.io/b/openemr/"""
driver.get('http://demo.openemr.io/b/openemr/')

"""2.  Update username as admin"""
driver.find_element(By.ID, "authUser").send_keys("admin")

"""3.  Update password as pass"""
driver.find_element(By.ID, "clearPass").send_keys("pass")

"""4.  Select language as English (Indian)"""
sel_lang = Select(driver.find_element(By.XPATH, "//select[@name='languageChoice']"))
sel_lang.select_by_visible_text("English (Indian)")

"""5.  Click on the login button"""
driver.find_element(By.ID, "login-button").click()

"""6.  Click on Patient  Click New Search"""
action.move_to_element(driver.find_element(By.XPATH, "//div[text()='Patient']")).perform()
driver.find_element(By.XPATH, "//div[text()='New/Search']").click()

"""7.  Add the first name, last name"""
driver.switch_to.frame("pat")
driver.find_element(By.ID, "form_fname").send_keys("John")
driver.find_element(By.ID, "form_lname").send_keys("Wick")

"""8.  Update DOB as today's date driver.findElement(By.id("form_DOB")).sendKeys("2021-12-21");"""
driver.execute_script("document.querySelector('#form_DOB').value = '2021-12-21'")

"""9.  Update the gender"""
driver.find_element(By.XPATH, "(//option[text()='Male'])[1]").click()

"""10. Click on the create new patient button above the form"""
driver.find_element(By.ID, 'create').click()
driver.switch_to.default_content()

"""11. Click on confirm create new patient button."""
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[contains(@src,  'new_search_popup')]"))
driver.find_element(By.XPATH, "//input[@class='btn btn-primary' and @value='Confirm Create New Patient']").click()

"""12. Print the text from alert box (if any error before handling alert add 5 sec wait)"""
wait.until(ec.alert_is_present())
print("Alert Message:\n", driver.switch_to.alert.text, "\n")

"""13. Handle alert"""
driver.switch_to.alert.accept()
driver.switch_to.default_content()

"""14. Close the Happy Birthday popup"""
if len(driver.find_elements(By.XPATH, "//div[@class= 'closeDlgIframe']")) > 0:
    driver.find_element(By.XPATH, "//div[@class= 'closeDlgIframe']").click()

"""15. Get the added patient name and print in the console."""
driver.switch_to.frame("pat")
print("Medical Records of: ",
      driver.find_element(By.XPATH, "//h2[contains(text(),'Medical Record Dashboard')]").text.split(" - ")[1], "\n")

print("Site: ", driver.title)

driver.quit()
