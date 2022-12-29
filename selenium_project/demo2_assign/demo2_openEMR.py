from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
#import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://demo.openemr.io/b/openemr')
driver.find_element(By.ID, "authUser").send_keys("admin")
driver.find_element(By.ID, "clearPass").send_keys("pass")

sel_lang = Select(driver.find_element(By.XPATH, "//select[@name='languageChoice']"))
sel_lang.select_by_visible_text("English (Indian)")

driver.find_element(By.ID, "login-button").click()

print(driver.title)

#time.sleep(1)

driver.close()
