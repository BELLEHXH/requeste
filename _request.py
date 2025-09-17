import requests

try:
     url = "https://sp.senai.br/unidade/santanadeparnaiba/"
     resposta = requests.get (url)
     status = resposta .status_code
     if status == 200
        print("site encontrado! status:",status)
     else:
          print("site nao encontrado:",status)

except:
     print(f"seu site nao foi encontrado")
