#The python time machine
# This App will give the user songs from a certain time/ year
#We will soup to scrap the top 100 songs
#We will use the spotify API to add the songs to our playlist 

import requests
from bs4 import BeautifulSoup
Input = input("What year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = "https://www.billboard.com/charts/hot-100/2000-08-12/" + Input
response = requests.get(URL)
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")
song_names = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate") 
song_list = [song.getText().strip() for song in song_names]
print(song_list) 








