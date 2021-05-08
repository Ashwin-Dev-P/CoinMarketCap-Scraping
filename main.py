from bs4 import BeautifulSoup
import requests
import csv



csv_file = open('coins.csv','w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['name','symbol','URL'])

def get_coins():
    url = "https://coinmarketcap.com/"
    source = requests.get(url).text
    soup = BeautifulSoup(source,'lxml')

    count = 0
    cmc_links = soup.find_all('a',class_='cmc-link')
    selected_divs = soup.find_all('div',class_='sc-16r8icm-0 dnwuAU') 
    for div in selected_divs:
        if(count >= 50):
            break
        else:
            name = div.find('p',class_='sc-1eb5slv-0 iJjGCS').text
            symbol = div.find('p',class_='sc-1eb5slv-0 gGIpIK coin-item-symbol').text
            URL = "coinmarketcap.com" + div.find('a',class_='cmc-link')['href']
            csv_writer.writerow([name,symbol,URL])
            count += 1

    for link in cmc_links:
        if(count >= 50):
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




def get_coin_data(coin_symbol):
    with open('coins.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            if(line[1] == coin_symbol ):
                print(line)
                target_url = "http://" + line[2]
                print(target_url)
                break
            
            
    url = target_url
    source = requests.get(url).text
    soup = BeautifulSoup(source,'lxml')
    
    watch_list = soup.find_all('div',class_="namePill___3p_Ii")[2].text.split()[1]
    print(watch_list)
    
get_coin_data('BTC')
    
    
    
    
    