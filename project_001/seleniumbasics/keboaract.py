from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions , Chrome
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = Chrome(options=opts)
driver.get("https://en.key-test.ru/")


time.sleep(2)
act = ActionChains(driver)
act.key_down(Keys.CONTROL)
act.send_keys("A")
act.perform()