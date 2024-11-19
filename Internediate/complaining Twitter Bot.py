#This an automated complaining twitter bot
# Our service provider is COMCAST
#whenever our internet speed is 250mbps or less, it will complain to our service provider
# we will also selenium to automate the process of doing our speed test from the internet
#we will then send the complain via our chatbot on twitter 

import time
from selenium import webdriver


class ComcastComplainerBot:
    def __init__(self, twitter_email, twitter_password):
        # Setting up my bot with Twitter credentials.
        self.driver = webdriver.Chrome()  # I need the Chrome WebDriver installed for this.
        self.email = twitter_email
        self.password = twitter_password

    def check_internet_speed(self):
        # Visiting an online speed test site to check my current internet speed.
        print("Checking internet speed...")
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)
        start_button = self.driver.find_element_by_class_name("start-text")
        start_button.click()
        time.sleep(60)  # I'm waiting for the speed test to complete.

        # Fetching the download speed from the results.
        download_speed = self.driver.find_element_by_class_name("download-speed").text
        print(f"Download speed: {download_speed} Mbps")
        return float(download_speed)

    def login_to_twitter(self):
        # logging into Twitter to send my complaint.
        print("Logging into Twitter...")
        self.driver.get("https://twitter.com/login")
        time.sleep(5)
        
        email_field = self.driver.find_element_by_name("session[username_or_email]")
        password_field = self.driver.find_element_by_name("session[password]")
        email_field.send_keys(self.email)
        password_field.send_keys(self.password)
        password_field.submit()
        time.sleep(5)

    def send_complaint(self, message):
        # Crafting and sending my complaint tweet.
        print("Sending complaint tweet...")
        tweet_box = self.driver.find_element_by_xpath("//div[@aria-label='Tweet text']")
        tweet_box.send_keys(message)
        tweet_button = self.driver.find_element_by_xpath("//div[@data-testid='tweetButton']")
        tweet_button.click()
        print("Complaint sent successfully!")
        time.sleep(5)

    def run(self):
        # This is where I tie everything together.
        speed = self.check_internet_speed()
        if speed < 250:
            self.login_to_twitter()
            complaint_message = f"Hey @comcast, my internet speed is only {speed} Mbps instead of the promised 1 Gbps. Please fix this ASAP! #ComcastFail"
            self.send_complaint(complaint_message)
        else:
            print("Internet speed is fine. No need to complain.")
        self.driver.quit()

#Initializing my bot with my Twitter credentials.
bot = ComcastComplainerBot("my_twitter_email", "my_twitter_password")
bot.run()



    

