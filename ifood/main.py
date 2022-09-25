# Importar as bibliotecas necessarias 
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
produto = "Feijão 1K"
url = "https://www.ifood.com.br/busca?q=" + produto + "tab=1&sort=price_range%3Aasc&type=MARKET&term=" + produto + ""
retorno = requests.get(url, headers = headers)

soup = BeautifulSoup(retorno.content, 'html5lib')
print(soup.prettify())