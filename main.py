from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Replace 'your_url' with the actual URL you want to scrape
url = 'https://www.realestate.com.au/buy/list-1'

# Replace 'your_class_name' with the actual class name you want to target
class_name = 'tiered-results'

# Set up the webdriver (make sure you have the appropriate webdriver installed and its path configured)
driver = webdriver.Chrome()

# Open the webpage
driver.get(url)

# Find elements by class name
elements = driver.find_element(By.CLASS_NAME, class_name)
page = driver.page_source
print(page)
exit()# Print or process the elements as needed
for element in elements:
    print(element.text)

time.sleep(10)
# Close the webdriver
# driver.quit()
