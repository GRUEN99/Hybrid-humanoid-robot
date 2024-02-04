import requests
from bs4 import BeautifulSoup


def get_Weather_report():
    # creating url and requests instance
    url = "https://www.google.com/search?q="+"weather"
    html = requests.get(url).content

    # getting raw data
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

    # formatting data
    data = str.split('\n')
    time = data[0]
    sky = data[1]
    return temp , sky

#
# printing all data
# print("Temperature is", temp)
# print("Sky Description: ", sky)
