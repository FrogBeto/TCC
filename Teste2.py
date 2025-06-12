import pandas as pd
import requests
import json

df = pd.read_csv('teste.csv')
donos = []
projetos = []

token = ""
headers = {
    "Authorization": "token {}".format(token)
}

#print(df)
for x in df['Dono']:
    donos.append(x)
for x in df['Projeto']:
    projetos.append(x)

#for x in range(len(dono)):
    #print(dono[x] + " " + projeto[x])

#f = open("usuarios.csv", "a")

#f.write("aaaaaa,44,55555\n")
#f.write(dono[0] + "," + str(3) + "," + projeto[0] + "\n")

class Busca:
    def __init__(self, dono, projeto):
        self.dono = dono
        self.projeto = projeto
        self.valor = 1

    def requisicao(self):
        reposta = requests.get(
            f'https://api.github.com/repos/{self.dono}/{self.projeto}/contributors?per_page=100&page={self.valor}',
            headers=headers
        )

        if reposta.status_code == 200:
            return reposta.json()
        else:
            return reposta.status_code

    def gravacao(self):
        dados = self.requisicao()

        if type(dados) is not int:
            with open("usuarios.csv", "a") as f:
                while dados:
                    for i in range(len(dados)):
                        f.write(dados[i]['login'] + "," + str(dados[i]['contributions']) + "," + self.projeto + "\n")

                    self.valor += 1
                    dados = self.requisicao()