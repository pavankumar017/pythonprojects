from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions , Chrome
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = Chrome(options=opts)
driver.get("https://demo.nopcommerce.com/login")

title = driver.title
url = driver.current_url
print(url)
print(title)


# print(driver.find_element(By.XPATH, "//button[contains(text(),'Search')]").is_displayed())

# print(driver.find_element(By.XPATH, "//button[contains(text(),'Search')]").is_enabled())
# # driver.find_element(By.ID, "pollanswers-1").click()
# print(driver.find_element(By.ID, "pollanswers-1").is_selected())

driver.find_element(By.CSS_SELECTOR , "input#Email").send_keys("asdas@gmail.com")

print(driver.find_element(By.CSS_SELECTOR , "input#Email").get_attribute("value"))


# GETTING attribute value of other 
print(driver.find_element(By.CSS_SELECTOR , "input#Email").get_attribute("data-val-required"))  
