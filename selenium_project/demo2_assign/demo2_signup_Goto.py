from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

"""Login to Page"""
driver.get('https://www.goto.com/meeting')

"""For Cookies Check"""
driver.find_element(By.ID, 'truste-consent-button').click()
#driver.find_element(By.LINK_TEXT, "Try Free").location_once_scrolled_into_view
driver.find_element(By.LINK_TEXT, "Try Free").click()

"""Enter First Name"""
driver.find_element(By.ID, "first-name").send_keys("John")

"""Enter Last Name"""
driver.find_element(By.ID, "last-name").send_keys("Wick")

"""Enter email address"""
driver.find_element(By.ID, "login__email").send_keys("babayega@still-alive.com")

"""Enter Company Size"""
set_comp_size = Select(driver.find_element(By.ID, "CompanySize"))
set_comp_size.select_by_visible_text("10 - 99")

"""Click Start My Trail"""
driver.find_element(By.XPATH, "//button[@data-button='trial-submit']").click()

if driver.find_element(By.CLASS_NAME, 'trial__error-box'):
    print("\nSomething Wrong :( - Please enter Password also\n")

# if driver.find_element(By.XPATH, "//div[@class='inputField__requirements']/span/img[@src,'ment-alert']"):
#     print("\nPassword not Correct\n")

print(driver.title.split(' - ')[0])

driver.quit()
