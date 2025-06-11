import csv
import pandas as pd

df = pd.read_csv('teste.csv')
donos = []
projeto = []

#print(df['Dono'])
for x in df['Dono']:
    donos.append(x)
for x in df['Projeto']:
    projeto.append(x)

for x in range(len(donos)):
    print(donos[x] + " " + projeto[x])

