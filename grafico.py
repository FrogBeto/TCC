import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('CSVs/Dados Finais/dados.csv', sep=';')

df['Atualizado_em'] = pd.to_datetime(df['Atualizado_em'], format="%Y-%m-%d")

df['Ano'] = df['Atualizado_em'].dt.year
df['Mes'] = df['Atualizado_em'].dt.month
df['Dia'] = df['Atualizado_em'].dt.day

for x in range(5):
    print(df['Atualizado_em'][x], df['Ano'][x], df['Mes'][x], df['Dia'][x])

#paises = df.groupby(['País']).sum().reset_index().sort_values('Contribuições', ascending=False).reset_index(drop=True)

#for x in range(len(paises)):
    #print(paises['País'][x], paises['Contribuições'][x])

#plt.bar(paises['País'], paises['Contribuições'])
#plt.show()

#paises = df.groupby(['País', 'Projeto']).sum().reset_index().sort_values(['Projeto', 'Contribuições'], ascending=False).reset_index(drop=True)

#temp = []
#temp2 = []

#for x in range(len(paises)):
    #print(paises['Projeto'][x], paises['Contribuições'][x], paises['País'][x])

#    if x != 0 and paises['Projeto'][x] != paises['Projeto'][x-1]:
#        plt.bar(temp, temp2)
#        plt.title(paises['Projeto'][x-1])
#        plt.show()
#        temp = []
#        temp2 = []


#    if paises['País'][x] != "<null>":
#        temp.append(paises['País'][x])
#        temp2.append(paises['Contribuições'][x])


#plt.title(paises['Projeto'][len(paises)-1])
#plt.bar(temp, temp2)
#plt.show()
#temp = []
#temp2 = []