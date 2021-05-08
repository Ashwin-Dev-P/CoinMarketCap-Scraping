from bs4 import BeautifulSoup
import requests

source = requests.get('https://coinmarketcap.com/').text
soup = BeautifulSoup(source,'lxml')


"""
#print(soup.prettify())
names = soup.find_all('p',class_='sc-1eb5slv-0 iJjGCS')
for name in names:
    print(name.text)
symbols = soup.find_all('p',class_='sc-1eb5slv-0 gGIpIK coin-item-symbol')
for symbol in symbols:
    print(symbol.text)    
    
urls = soup.find_all('a',class_='cmc-link')
for url in urls:
    print("https://coinmarketcap.com"+url['href'])    
"""

selected_divs = soup.find_all('div',class_='sc-16r8icm-0 dnwuAU') 
for div in selected_divs:
    name = div.find('p',class_='sc-1eb5slv-0 iJjGCS').text
    symbol = div.find('p',class_='sc-1eb5slv-0 gGIpIK coin-item-symbol').text
    URL = "coinmarketcap.com" + div.find('a',class_='cmc-link')['href']
    print(name,symbol,URL)


