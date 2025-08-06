import pandas as pd
import requests

#Leitura do CSV com todos os dados coletados e com tratamento prévio
df = pd.read_csv('Tratamento Inicial\dados2.csv', sep=';')
locais = []             #Vetor que vai armazenar os locais

#Criação da lista de localizações dos usuarios
for x in df['location']:
    locais.append(x)

#Classe responsavel por receber a localização e fazer uma requisição na API do MapBox
class Tratamento:
    def __init__(self, localizacao):
        self.localizacao = localizacao #Atribuindo a localização

    #Faz a requisição, retornando o resultado da busca, é necessário a chave de acesso do MapBox
    def requisicao(self):
        reposta = requests.get(
            f'https://api.mapbox.com/search/geocode/v6/forward?q={self.localizacao}&access_token='
        )

        return reposta.json()

    #Grava num arquivo o país onde o usuario está localizado, sua longitude e sua latitude
    def gravacao(self):
        dados = self.requisicao()

        with open("Tratamento Inicial\dados3.csv", "a", encoding="utf-8") as f:
            f.write(
                dados['features'][0]['properties']['context']['country']['name'] + ";" +
                str(dados['features'][0]['properties']['coordinates']['longitude']) + ";" +
                str(dados['features'][0]['properties']['coordinates']['latitude']) + "\n"
            )

#Percorre o vetor, caso seja uma localização nula, grava que é nulo e aponta para 0 0,
for x in range(len(locais)):
    if locais[x] == "<null>":
        with open("Tratamento Inicial\dados3.csv", "a", encoding="utf-8") as f:
            f.write(
                "<null>" + ";" + "0" + ";" + "0" + "\n"
            )

    # caso o usuario tenha definido apenas que está na Europa, grava como Europa e aponta para Mônaco
    elif locais[x] == "Europe":
        with open("Tratamento Inicial\dados3.csv", "a", encoding="utf-8") as f:
            f.write(
                "Europe" + ";" + "7.418962" + ";" + "43.732482" + "\n"
            )

    # caso nenhum dos dois primeiros cenários aconteça, faz efetivamente a consulta e gravação
    else:
        local = Tratamento(locais[x])
        local.gravacao()
        print("{:.2f}".format((x+1)/11610 * 100) + "% " + str(x+1) + " " + locais[x])
        #para acompanhar em caso de erro, o programa mostra a porcentagem já analisada,
        #qual é o número exato que esta sendo consultado e a localização em questão