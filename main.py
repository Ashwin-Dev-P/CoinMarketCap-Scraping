from bs4 import BeautifulSoup
import requests
import csv

url = "https://coinmarketcap.com/"
source = requests.get(url).text
soup = BeautifulSoup(source,'lxml')

csv_file = open('coins.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['name','symbol','URL'])

def get_coins():
    count = 0
    cmc_links = soup.find_all('a',class_='cmc-link')
    selected_divs = soup.find_all('div',class_='sc-16r8icm-0 dnwuAU') 
    for div in selected_divs:
        if(count > 50):
            break
        else:
            name = div.find('p',class_='sc-1eb5slv-0 iJjGCS').text
            symbol = div.find('p',class_='sc-1eb5slv-0 gGIpIK coin-item-symbol').text
            URL = "coinmarketcap.com" + div.find('a',class_='cmc-link')['href']
            csv_writer.writerow([name,symbol,URL])
            count += 1

    for link in cmc_links:
        if(count > 50):
            break
        else:
            try:
                name = link.find('span',class_="").text
                symbol = link.find('span',class_='crypto-symbol').text
                URL = "coinmarketcap.com" + link['href']
                csv_writer.writerow([name,symbol,URL])
                count += 1
            except:
                pass
    csv_file.close()
get_coins()