from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://csreis.github.io/tests/cross-site-iframe.html")
driver.switch_to.frame('frame1')
txt = driver.find_element(By.XPATH, "//body").text
print(txt)

driver.switch_to.default_content()
fram12 = driver.find_element(By.XPATH , "//iframe")
driver.switch_to.frame(fram12)
txt = driver.find_element(By.XPATH, "//body").text
print(txt)