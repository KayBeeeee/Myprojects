#The Amazon Price Tracker
#This program will check the price of an item on Amazon and send you an email if the price has dropped below a certain threshold.


import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:7].replace(',',''))

    if(converted_price < 60000):
        send_mail()

    print(converted_price)
    print(title.strip())

    if(converted_price < 60000):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('XXXXXXXXXXXXXXXXXXXX', 'your_password')

    subject = 'Price fell down!'
    body = 'Check the amazon link XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'XXXXXXXXXXXXXXXXXXXX',
        'XXXXXXXXXXXXXXXXXXXX',
        msg
    )
    print('HEY EMAIL HAS BEEN SENT!')

    server.quit()

check_price()