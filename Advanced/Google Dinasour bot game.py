"""
Google Dinosaur Game Bot
-------------------------
This script automates the Google Dinosaur Game using Selenium.

Requirements:
- Google Chrome browser
- ChromeDriver
- Selenium Python library

How it works:
1. Launches the Chrome browser in automation mode.
2. Opens the Google Dinosaur Game (accessible offline or by navigating to 'chrome://dino').
3. Simulates keypress events to control the dinosaur and avoid obstacles.

Note: This script is for educational purposes. Automation of games should be done responsibly.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def play_dino_game():
    """
    Automates the Google Dinosaur Game.
    """
    # Set up the Selenium WebDriver for Chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-infobars")
    options.add_argument("--mute-audio")
    options.add_argument("start-maximized")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)

    try:
        # Open the Dinosaur Game
        driver.get("chrome://dino")

        # Access the game's canvas element
        canvas = driver.find_element(By.ID, "t")

        # Start the game by simulating a SPACE key press
        canvas.send_keys(Keys.SPACE)
        print("Game started! Bot is now playing...")

        # Game loop: Continuously monitor and jump
        while True:
            # Simulate a SPACE key press every 0.5 seconds (adjust as needed)
            canvas.send_keys(Keys.SPACE)
            time.sleep(0.5)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    play_dino_game()
