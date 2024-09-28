from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions , Chrome
import requests as request
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = Chrome(options=opts)
driver.get("https://deadlinkcity.com")

url =  driver.find_element(By.TAG_NAME, "a")
for link in url:
    url_link = link.get_attribute("href")
    res = request.head(url_link)
    if res.status_code >= 400:
        print(url_link, "is broken link ")