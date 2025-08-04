import pandas as pd
import requests

df = pd.read_csv('dados2.csv', sep=';')
aux = pd.read_csv('filtro.csv', sep=';')
locais = []
filtro = []

flag = True

for x in df['location']:
    locais.append(x)
for x in aux['location']:
    filtro.append(x)

class Tratamento:
    def __init__(self, localizacao):
        self.localizacao = localizacao

    def requisicao(self):
        reposta = requests.get(
            f'https://api.mapbox.com/search/geocode/v6/forward?q={self.localizacao}&access_token='
        )

        return reposta.json()

    def gravacao(self):
        dados = self.requisicao()

        with open("dados3.csv", "a", encoding="utf-8") as f:
            f.write(
                dados['features'][0]['properties']['context']['country']['name'] + ";" +
                dados['features'][0]['properties']['coordinates']['longitude'] + ";" +
                dados['features'][0]['properties']['coordinates']['latitude'] + "\n"
            )

for x in range(5):
    for y in range(len(filtro)):
        if locais[x] == "filtro[y]":
            with open("dados3.csv", "a", encoding="utf-8") as f:
                f.write(
                    "<null>" + ";" + "0" + ";" + "0" + "\n"
                )

            flag = False

            break
    if locais[x] is None:
        print(locais[x])
    else:
        print("locais[x]")

    if flag:
        #local = Tratamento(locais[x])
        #local.gravacao()
        print("\n")
    else:
        flag = True