

import bs4 as bs
import sys
import urllib.request
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl

class Page(QWebEnginePage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.html = ''
        self.loadFinished.connect(self._on_load_finished)
        self.load(QUrl(url))
        self.app.exec_()

    def _on_load_finished(self):
        self.html = self.toHtml(self.Callable)
        print('Load finished')

    def Callable(self, html_str):
        self.html = html_str
        self.app.quit()

url = "https://coinmarketcap.com/"
def main():
    page = Page(url)
    soup = bs.BeautifulSoup(page.html, 'html.parser')
    
    cmc_links = soup.find_all('a',class_='cmc-link')
    selected_divs = soup.find_all('div',class_='sc-16r8icm-0 dnwuAU') 
    for div in selected_divs:
        name = div.find('p',class_='sc-1eb5slv-0 iJjGCS').text
        symbol = div.find('p',class_='sc-1eb5slv-0 gGIpIK coin-item-symbol').text
        URL = "coinmarketcap.com" + div.find('a',class_='cmc-link')['href']
        print(name,symbol,URL)
    for link in cmc_links:
        try:
            name = link.find('span',class_="").text
            symbol = link.find('span',class_='crypto-symbol').text
            URL = "coinmarketcap.com" + link['href']
            print(name,symbol,URL)
        except:
            pass
    

if __name__ == '__main__': main()
