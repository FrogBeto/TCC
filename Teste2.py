import csv
import pandas as pd
import requests
import json

df = pd.read_csv('teste.csv')
dono = []
projeto = []

#print(df['Dono'])
for x in df['Dono']:
    dono.append(x)
for x in df['Projeto']:
    projeto.append(x)

for x in range(len(dono)):
    print(dono[x] + " " + projeto[x])

class Busca():
    def __init__(self, dono, projeto):
        self.dono = dono
        self.projeto = projeto

    def requisicao(self):
        reposta = requests.get(
            f'https://api.github.com/repos/{}'
        )