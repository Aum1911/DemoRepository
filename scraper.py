import requests
from bs4 import BeautifulSoup
import smtplib

URL='https://www.amazon.in/gp/product/B07TNVBLNT'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}

def check_price():
 page = requests.get(URL, headers=headers)

 soup =BeautifulSoup(page.content, 'html.parser')

 title = soup.find(id="productTitle").get_text()
 price = soup.find(id="priceblock_dealprice").get_text()
 converted_price = float(price[2:7].replace(",",""))  

 if(converted_price < 9000.00):
    send_mail()

 print(price)
 print(title.strip())
 print(converted_price)


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('aumthecrazyshukla@gmail.com', 'clnfzsbxhvabfgkn')

    subject = 'The Price fell down!'
    body = ' Check the product NOW! https://www.amazon.in/gp/product/B07TNVBLNT '

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'aumthecrazyshukla@gmail.com',
        'aug23_aks@hotmail.com',
        msg                
    ) 
    print('Hey, the mail has been sent!')

    server.quit()

check_price()


