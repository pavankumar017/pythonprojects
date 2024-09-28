from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions , Chrome
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = Chrome(options=opts)
driver.get("https://www.britannica.com/topic/list-of-countries-1993160")


# till a pixel
driver.execute_script("window.scrollTo(0, 2000)")

time.sleep(5)
# a particular element
elment = driver.find_element(By.LINK_TEXT,"India")
elment.location_once_scrolled_into_view

time.sleep(5)

WebDriverWait(driver, 10,poll_frequency=2, ignored_exceptions=[NoSuchElementException] ).wait.until(EC.presence_of_element_located((By.XPATH , "ASKHDJASH")))

