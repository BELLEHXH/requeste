import requests
from bs4 import BeautifulSoup

# URL que você deseja acessar
url = "https://sp.senai.br/unidade/santanadeparnaiba/"

# Realiza uma requisição HTTP GET
response = requests.get(url)
if response.status_code != 200:
    print(f"Falha ao acessar a página: status code {response.status_code}")
    exit()

# Cria o objeto BeautifulSoup para parsing
soup = BeautifulSoup(response.text, "html.parser")

# Busca por todas as tags <h1>
h1_tags = soup.find_all("h1")

# Se houver alguma, imprime o texto da primeira (ou todas, se quiser)
if h1_tags:
    print("Conteúdo da primeira tag <h1> encontrada:")
    print(h1_tags[0].get_text(strip=True))
else:
    print("Nenhuma tag <h1> foi encontrada.")
