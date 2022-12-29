import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

wait = WebDriverWait(driver, 20)

"""Login to Page"""
driver.get('https://nasscom.in/')

action = webdriver.ActionChains(driver)

action.move_to_element(driver.find_element(By.LINK_TEXT, "Membership")).pause(1).move_to_element(
    driver.find_element(By.XPATH,
                        "//a[text() = 'Become a Member']")).perform()
driver.find_element(By.LINK_TEXT, "Membership Benefits").click()
