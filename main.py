import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.x-kom.pl/szukaj?q=karta%20graficzna"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()


page_soup = soup(page_html, "html.parser")


graphics_cards = page_soup.findAll("div", {"class":"sc-162ysh3-1 ihpEDx sc-bwzfXH dXCVXY"})
len(graphics_cards)
