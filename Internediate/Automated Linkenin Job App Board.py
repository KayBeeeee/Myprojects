#This App automates applying for Jobs on Linkedin
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Enter your Linkedin credentials here
username = "XXXXXXXXXXXXX"
password = "XXXX_password"

#Enter the job you want to apply for here
job = "job_title"

#Enter the location you want to apply for here
location = "location"

#Enter the number of jobs you want to apply for here
num_jobs = 10

#Enter the number of seconds you want to wait between each job application here
wait_time = 5

#Enter the number of seconds you want to wait between each job application here
driver = webdriver.Chrome()

driver.get("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

username_field = driver.find_element_by_id("username")
username_field.send_keys(username)

password_field = driver.find_element_by_id("password")
password_field.send_keys(password)

password_field.send_keys(Keys.RETURN)

time.sleep(5)

driver.get("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"+job+"&location="+location)

time.sleep(5)

for i in range(num_jobs):
    try:
        apply_button = driver.find_element_by_xpath("//button[contains(text(), 'Apply')]")
        apply_button.click()
        time.sleep(wait_time)
        driver.get("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"+job+"&location="+location)
    except:
        print("No more jobs to apply for")
        break

driver.quit()