import pandas as pd
import requests

token = ""
headers = {
    "Authorization": "access_token {}".format(token)
}

df = pd.read_csv('dados2.csv', sep=';')
locais = []

for x in df['location']:
    locais.append(x)

class Tratamento:
    def __init__(self, localizacao):
        self.localizacao = localizacao

    def requisicao(self):
        reposta = requests.get(
            f'https://api.mapbox.com/search/geocode/v6/forward?q={self.localizacao}&limit=1',
            headers=headers
        )

        return reposta.json()

    def gravacao(self):
        dados = self.requisicao()

        with open("dados3.csv", "a", encoding="utf-8") as f:
            f.write(
                self.localizacao + "\n"
            )