from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl

#from PyQt4.QtWebKit import QWebPage
from PyQt5.QtWebEngineWidgets import QWebEnginePage

class Client(QWebEnginePage):
    def __init__(self,url):
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        
    def on_page_load(self):
        self.app.quit()
        
url = "https://coinmarketcap.com/"
client_response = Client(url)
source = client_response.mainFrame().toHtml()

def get_coins():
    source = requests.get('https://coinmarketcap.com/')
    source = source.text
    """
    browser = webdriver.PhantomJS("C:\phantomjs-2.1.1-windows\bin")
    browser.get(source)
    html = browser.page_source
    """
    
    soup = BeautifulSoup(source,'lxml')
    selected_divs = soup.find_all('div',class_='sc-16r8icm-0 dnwuAU') 
    for div in selected_divs:
        name = div.find('p',class_='sc-1eb5slv-0 iJjGCS').text
        symbol = div.find('p',class_='sc-1eb5slv-0 gGIpIK coin-item-symbol').text
        URL = "coinmarketcap.com" + div.find('a',class_='cmc-link')['href']
        print(name,symbol,URL)
get_coins()