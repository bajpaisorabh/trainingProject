from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://google.com')

print("The title of current page", driver.title)

print("You can access this by:", driver.current_url)

print("Source Code:\n", driver.page_source)
