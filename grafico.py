import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

######################Tratamento das datas################################
#df = pd.read_csv('CSVs/Dados Finais/dados.csv', sep=';')

#df['Atualizado_em'] = pd.to_datetime(df['Atualizado_em'], format="%Y-%m-%d").dt.date

#df['Atualizado_em_Ano'] = pd.to_datetime(df['Atualizado_em']).dt.year
#df['Atualizado_em_Mes'] = pd.to_datetime(df['Atualizado_em']).dt.month
#df['Atualizado_em_Dia'] = pd.to_datetime(df['Atualizado_em']).dt.day

#df['Criado_em'] = pd.to_datetime(df['Criado_em'], format="%Y-%m-%d").dt.date

#df['Criado_em_Ano'] = pd.to_datetime(df['Criado_em']).dt.year
#df['Criado_em_Mes'] = pd.to_datetime(df['Criado_em']).dt.month
#df['Criado_em_Dia'] = pd.to_datetime(df['Criado_em']).dt.day

#for x in range(5):
#    print(df['Criado_em'][x], df['Criado_em_Ano'][x], df['Criado_em_Mes'][x], df['Criado_em_Dia'][x],
#          df['Atualizado_em'][x], df['Atualizado_em_Ano'][x], df['Atualizado_em_Mes'][x], df['Atualizado_em_Dia'][x])

#df.to_csv('CSVs/Dados Finais/dadosFinais2.csv', sep=';', index=False)
#################################################################

#################Grafico geral dos países########################
#paises = df.groupby(['País']).sum().reset_index().sort_values('Contribuições', ascending=False).reset_index(drop=True)

#for x in range(len(paises)):
    #print(paises['País'][x], paises['Contribuições'][x])

#plt.bar(paises['País'], paises['Contribuições'])
#plt.show()
###############################################################

############################Grafico dos projetos exceto os nulos##############################
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
###########################################################################################

################################Gráfico dos abandonos#########################
#df = pd.read_csv('CSVs/Dados Finais/dadosFinais.csv', sep=';')

#abandonos = df.groupby(['Ano']).size().reset_index(name='Quantidade').sort_values('Ano', ascending=False).reset_index(drop=True)

#print(abandonos)

#outros = 0

#for x in range(len(abandonos)):
#    if x != 0 and x != 1:
#        outros = outros + abandonos['Quantidade'][x]


#plt.pie(
#    [abandonos['Quantidade'][0], abandonos['Quantidade'][1], outros],
#    labels=('2025', '2024', 'Outros Anos'),
#    autopct='%1.1f%%',
#    explode=(0.2, 0.2, 0.2),
#)
#plt.show()
##########################################################################################

################################Abandonos por Projeto#####################################
#paises = df.groupby(['Projeto', 'Ano']).size().reset_index(name='Quantidade').sort_values(['Projeto', 'Ano'], ascending=False).reset_index(drop=True)

#temp = []
#temp2 = []
#outros = 0

#for x in range(len(paises)):
    #print(paises['Projeto'][x], paises['Ano'][x], paises['Quantidade'][x])

#    if x != 0 and paises['Projeto'][x] != paises['Projeto'][x-1]:
#        temp.append('Outros Anos')
#        temp2.append(outros)
#        plt.pie(
#            temp2,
#            labels=temp,
#            autopct='%1.1f%%',
#            explode=(0.2, 0.2, 0.2)
#        )
#        plt.title(paises['Projeto'][x-1])
#        plt.show()
#        temp = []
#        temp2 = []
#        outros = 0

#    if paises['Ano'][x] == 2025 or paises['Ano'][x] == 2024:
#        temp.append(paises['Ano'][x])
#        temp2.append(paises['Quantidade'][x])
#    else:
#        outros = outros + paises['Quantidade'][x]


#temp.append('Outros Anos')
#temp2.append(outros)
#plt.title(paises['Projeto'][len(paises)-1])
#plt.pie(
#    temp2,
#    labels=temp,
#    autopct='%1.1f%%',
#    explode=(0.2, 0.2, 0.2)
#)
#plt.show()

##########################################################################

################################Gráfico das Criações#########################
#df = pd.read_csv('CSVs/Dados Finais/dadosFinais2.csv', sep=';')

#criacao = df.groupby(['Criado_em_Ano']).size().reset_index(name='Quantidade').sort_values('Criado_em_Ano', ascending=False).reset_index(drop=True)

#print(criacao)

#plt.bar(criacao['Criado_em_Ano'],criacao['Quantidade'])
#plt.show()
##########################################################################################

################################Criações por Projeto#####################################
#criacao = df.groupby(['Projeto', 'Criado_em_Ano']).size().reset_index(name='Quantidade').sort_values('Projeto', ascending=False).reset_index(drop=True)

#temp = []
#temp2 = []

#for x in range(len(criacao)):
#    print(criacao['Projeto'][x], criacao['Criado_em_Ano'][x], criacao['Quantidade'][x])

#    if x != 0 and criacao['Projeto'][x] != criacao['Projeto'][x-1]:
#        plt.bar(temp, temp2)
#        plt.title(criacao['Projeto'][x-1])
#        plt.show()
#        temp = []
#        temp2 = []

#    temp.append(criacao['Criado_em_Ano'][x])
#    temp2.append(criacao['Quantidade'][x])

#plt.title(criacao['Projeto'][len(criacao)-1])
#plt.bar(temp, temp2)
#plt.show()
##########################################################################

#############################Contribuição po Ano de criação#########################
df = pd.read_csv('CSVs/Dados Finais/dadosFinais2.csv', sep=';')

#criacao = df.groupby(['Criado_em_Ano', 'Contribuições']).size().reset_index(name='Quantidade')

#print(criacao)

#aux = 0
#outro = 0
#temp = []
#temp2 = []
#temp.append(0)
#temp2.append(criacao['Criado_em_Ano'][0])

#for x in range(len(criacao)):
#    if criacao['Criado_em_Ano'][x] >= 2019:
#        outro += (int(criacao['Quantidade'][x]) * int(criacao['Contribuições'][x]))
#    elif x != 0 and criacao['Criado_em_Ano'][x] != criacao['Criado_em_Ano'][x-1]:
#        aux += 1
#        temp.append(0)
#        temp2.append(criacao['Criado_em_Ano'][x])
#    else:
#        temp[aux] = temp[aux] + (int(criacao['Quantidade'][x]) * int(criacao['Contribuições'][x]))


#temp2.append('Outros Anos')
#temp.append(outro)

#plt.pie(
#    temp,
#    labels=temp2,
#    autopct='%1.1f%%'
#)
#plt.show()

##################################################################################

####################################Contribuição po Ano de criação por projeto #######################################
criacao = df.groupby(['Criado_em_Ano', 'Contribuições', 'Projeto']).size().reset_index(name='Quantidade').sort_values(by=['Projeto', 'Criado_em_Ano'], ascending=False).reset_index(drop=True)

#print(criacao)

temp = []
temp2 = []

#aux = 0
#outro = 0
#temp.append(0)
#temp2.append(criacao['Criado_em_Ano'][0])

for x in range(len(criacao)):
#    if x != 0 and criacao['Projeto'][x] != criacao['Projeto'][x-1]:
#        plt.pie(
#            temp,
#            labels=temp2,
#            autopct='%1.1f%%'
#        )
#        plt.title(criacao['Projeto'][x - 1])
#        plt.show()
#        aux = 0
#        outro = 0
#        temp = []
#        temp2 = []
#        temp.append(0)

#    if x != 0 and criacao['Criado_em_Ano'][x] != criacao['Criado_em_Ano'][x-1]:
#        aux += 1
#        temp.append(0)
#        temp2.append(criacao['Criado_em_Ano'][x])
#        temp[aux] = temp[aux] + (int(criacao['Quantidade'][x]) * int(criacao['Contribuições'][x]))
#    else:
#        temp[aux] = temp[aux] + (int(criacao['Quantidade'][x]) * int(criacao['Contribuições'][x]))

    if x != 0 and criacao['Projeto'][x] != criacao['Projeto'][x-1]:
        plt.bar(temp, temp2)
        plt.title(criacao['Projeto'][x-1])
        plt.show()
        temp = []
        temp2 = []


    temp.append(criacao['Criado_em_Ano'][x])
    temp2.append(criacao['Quantidade'][x])

plt.title(criacao['Projeto'][len(criacao)-1])
plt.bar(temp, temp2)
plt.show()