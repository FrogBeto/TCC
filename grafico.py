import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('CSVs/Dados Finais/dados.csv', sep=';')

lista = []

for x in range(len(df)):
    lista.append(pd.Timestamp(df['Atualizado_em'][x]).year)

print(lista)
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