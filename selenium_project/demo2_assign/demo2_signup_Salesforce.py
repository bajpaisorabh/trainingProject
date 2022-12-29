from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

"""Login to Page"""
driver.get('https://www.salesforce.com/in/form/signup/freetrial-sales/')

"""For Cookies Check"""
if driver.find_element(By.ID, 'onetrust-banner-sdk'):
    driver.find_element(By.ID, 'onetrust-reject-all-handler').click()

"""Enter First Name"""
driver.find_element(By.NAME, "UserFirstName").send_keys("John")

"""Enter Last Name"""
driver.find_element(By.NAME, "UserLastName").send_keys("Wick")

"""Enter email address"""
driver.find_element(By.NAME, "UserEmail").send_keys("babayega@still-alive.com")

"""Enter Job Title"""
set_job_title = Select(driver.find_element(By.NAME, "UserTitle"))
set_job_title.select_by_visible_text("IT Manager")

""""Enter Company Name"""
driver.find_element(By.NAME, "CompanyName").send_keys("Continental, New York")


"""Enter Company Employee no"""
set_employ = Select(driver.find_element(By.NAME, "CompanyEmployees"))
set_employ.select_by_value("250")

# """Enter Mobile no"""
# # driver.find_element(By.NAME, "UserPhone").send_keys("1800000000")

"""Enter Country"""
set_country = Select(driver.find_element(By.NAME, "CompanyCountry"))
set_country.select_by_value("US")
# set_country.select_by_visible_text("US")
# driver.find_element(By.XPATH, "//option[contains(.,'Kingdom')]")

"""Select CheckBox"""
driver.find_element(By.XPATH,
                    "//div[@class='msaCheckbox checkboxInput section']//div[@class='checkbox-ui']").click()
#
"""Click Start My Trail"""
# driver.find_element(By.NAME, "start my free trial").click()

print(driver.title.split(':')[0])

driver.quit()
