import pandas as pd
import requests

df = pd.read_csv('dados2.csv', sep=';')
locais = []
y = 6775
flag = True

for x in df['location']:
    locais.append(x)

class Tratamento:
    def __init__(self, localizacao):
        self.localizacao = localizacao

    def requisicao(self):
        reposta = requests.get(
            f'https://api.mapbox.com/search/geocode/v6/forward?q={self.localizacao}&access_token=pk.eyJ1IjoiZnJvZ2JldG8iLCJhIjoiY21ja3dyd2FhMDR0dTJrcTFsOWJ4bmtpbCJ9.2NqjRFjSstc5gHSpmZctyw'
        )

        return reposta.json()

    def gravacao(self):
        dados = self.requisicao()

        with open("dados3.csv", "a", encoding="utf-8") as f:
            f.write(
                dados['features'][0]['properties']['context']['country']['name'] + ";" +
                str(dados['features'][0]['properties']['coordinates']['longitude']) + ";" +
                str(dados['features'][0]['properties']['coordinates']['latitude']) + "\n"
            )

for x in range(len(locais)):
    x = y
    if locais[x] == "<null>":
        with open("dados3.csv", "a", encoding="utf-8") as f:
            f.write(
                "<null>" + ";" + "0" + ";" + "0" + "\n"
            )

        flag = False
    elif locais[x] == "Europe":
        with open("dados3.csv", "a", encoding="utf-8") as f:
            f.write(
                "Europe" + ";" + "7.418962" + ";" + "43.732482" + "\n"
            )

        flag = False

    if flag:
        local = Tratamento(locais[x])
        local.gravacao()
        print("{:.2f}".format((x+1)/11610 * 100) + "% " + str(x+1) + " " + locais[x])
    else:
        flag = True

    y += 1