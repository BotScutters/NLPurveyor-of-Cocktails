from bs4 import BeautifulSoup
import urllib.request

url = "https://www.thespruceeats.com/a-to-z-cocktail-recipes-3962886"
resp = urllib.request.urlopen(url)
soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'))

# for link in soup.find_all('a', href=True):
#     print(link['href'])
print(resp)