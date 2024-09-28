from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions , Chrome
import requests as request
import time
from selenium.webdriver.support.ui import Select


opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = Chrome(options=opts)
driver.get("https://jqueryui.com/datepicker/")

driver.switch_to.frame(0)  
# going to frame 0 

driver.find_element(By.ID, "datepicker").send_keys("01/01/1999")

# driver.close()