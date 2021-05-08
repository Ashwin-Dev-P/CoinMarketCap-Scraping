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
                #print(line)
                target_url = "http://" + line[2]
                #print(target_url)
                name = line[0]
                print(coin_symbol)
                print(name)
                website_url = target_url
                print(website_url)
                break
            
            
    url = target_url
    source = requests.get(url).text
    soup = BeautifulSoup(source,'lxml')
    
    watch_list = soup.find_all('div',class_="namePill___3p_Ii")[2].text.split()[1]
    print(watch_list)
    circulating_supply = soup.find('div',class_="supplyBlockPercentage___1g1SF").text
    print(circulating_supply)    
    table = soup.find('div',class_='sc-16r8icm-0 fIhwvd')
    price = table.find('td').text
    print(price)
    market_cap = table.find_all('tr')[4].td.text
    print(market_cap)
    market_dominance = table.find_all('tr')[5].td.span.text
    print(market_dominance)
    rank = table.find_all('tr')[6].td.text
    print(rank)
    
    table2 = soup.find_all('div',class_='sc-16r8icm-0 fIhwvd')[1]
    market_cap = table2.find('td').span.text
    print(market_cap)
    over_all_div = soup.find('div',class_='sc-1lt0cju-0 srvSa').div
    
    
    
    what_is_coin_name = []
    who_are_the_founders = []
    what_makes_it_unique = []
    q1_flag = False
    q2_flag = False
    q3_flag = False
    
    for tag in over_all_div:
        if(tag.name == 'h3' ):
            q1_flag = True
        if(not q1_flag and tag.name == 'p'):
            what_is_coin_name.append(tag.text)
        
        
        if(tag.name == 'h4'):
            q2_flag = True
        if(not q2_flag and q1_flag and tag.name == 'p'):
            who_are_the_founders.append(tag.text)
            
        if(tag.name == 'h5'):
            q3_flag = True
        if(not q3_flag and q1_flag and q2_flag and tag.name == 'p'):
            what_makes_it_unique.append(tag.text)
            
            
    print(what_is_coin_name)
    print(who_are_the_founders)
    print(what_makes_it_unique)
    
    table3 = soup.find_all('div',class_="sc-16r8icm-0 fIhwvd")[3].tbody
    all_time_high_price = table3.find_all('tr')[4].td.span.text
    print(all_time_high_price) 
    all_time_low_price = table3.find_all('tr')[5].td.span.text
    print(all_time_low_price)
    all_time_high_date = table3.find('small',class_='smallHeading___3DNdQ').text.split('(')[0]
    print(all_time_high_date)
    all_time_low_date = table3.find_all('small',class_='smallHeading___3DNdQ')[1].text.split('(')[0]
    print(all_time_low_date)
get_coin_data('BTC')
    
    
    
    
    