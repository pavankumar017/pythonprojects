from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome() 

driver.get("https://www.facebook.com/")

    
driver.find_element(By.ID , "usrname")