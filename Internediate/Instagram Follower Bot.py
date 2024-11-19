#This App is an instagram follower bot that will follow the followers of a specific account
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("XXXXXXXXXXXXXXXXXXXXXXXXXX")
username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)
password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "password"))
)
username.clear()
username.send_keys("username")
password.clear()
password.send_keys("password")
password.send_keys(Keys.RETURN)
search = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']"))
)
search.send_keys("account")
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(1)
followers = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[contains(@href,'/followers')]"))
)
followers.click()
time.sleep(1)
for i in range(1, 100):
    follow = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Follow')]"))
    )
    follow.click()
    time.sleep(1)
driver.quit()