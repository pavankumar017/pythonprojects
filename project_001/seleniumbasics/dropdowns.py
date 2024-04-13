from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions , Chrome
import requests as request
import time
from selenium.webdriver.support.ui import Select


opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = Chrome(options=opts)
driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")


drp_down = Select(driver.find_element(By.TAG_NAME, "select"))

drp_down.select_by_visible_text("Algeria")
drp_down.select_by_index(11)
drp_down.select_by_value("BRN")