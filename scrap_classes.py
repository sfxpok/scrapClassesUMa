import os
import requests
from bs4 import BeautifulSoup as bs
import urllib2

startingURL = 'www.uma.pt/ensino/'
# courseCycles = ['1o-ciclo', '2o-ciclo', '3o-ciclo', 'pos-graduacoes', 'ctesp']

webPage = urllib2.urlopen(startingURL)
soup = bs(webPage, 'html.parser')
