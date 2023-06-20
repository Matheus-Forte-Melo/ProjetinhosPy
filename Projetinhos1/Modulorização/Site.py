import urllib.request
import urllib.error
import requests
from bs4 import BeautifulSoup


site = str(input('Digite o URL de um site: '))

try:  # O programa vai tentar atribuir essa variavel com o resultado desse request
    siteOpen = urllib.request.urlopen(site)
except ValueError:
    print(f'\033[33mSite ou URL inválida!\033[m, talvez você quis digitar "https://www.{site}(.com;.net;.br)?"')
except urllib.error.URLError as e:  # Se não conseguir ele manda isso
    print('\033[;31mSite inacessível!\033[m', e)
else:  # Se conseguir ele manda isso

    print('\033[;32mSite acessível!\033[m')

