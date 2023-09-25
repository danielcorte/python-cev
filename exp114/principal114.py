# Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

"""import requests
url = "https://www.youtube.com"

if requests.get(url).status_code == 200:
    print("\033[0;34mO servidor está disponível.\033[m")
else:
    print("\033[0;31mO servidor está indisponível.\033[m")"""

import urllib.request

try:
    url = urllib.request.urlopen("https://www.youtube.com")
except urllib.error.URLError:
    print("\033[0;31mO servidor está indisponível.\033[m")
else:
    print("\033[0;34mO servidor está disponível.\033[m")
