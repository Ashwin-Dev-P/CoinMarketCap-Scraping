from bs4 import BeautifulSoup
import dryscrape
session = dryscrape.Session()
my_url = "https://ypa.herokuapp.com/"
session.visit(my_url)
response = session.body()
soup = BeautifulSoup(response)
x = soup.find(id="target")
print(x)