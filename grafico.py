import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('CSVs/Dados Finais/dadosFinais2.csv', sep=';')

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


#################Grafico geral dos países########################
paises = df.groupby(['País']).sum().reset_index().sort_values('Contribuições', ascending=False).reset_index(drop=True)

plt.bar(paises['País'], paises['Contribuições'], zorder=2)
plt.title("Contribuições por País")
plt.xlabel("Países")
plt.ylabel("Número de contribuições")
plt.grid(axis='y', linestyle='--', zorder=1)
plt.show()
###############################################################

############################Grafico dos projetos exceto os nulos##############################
paises = df.groupby(['País', 'Projeto']).sum().reset_index().sort_values(['Projeto', 'Contribuições'], ascending=False).reset_index(drop=True)

temp = []
temp2 = []

for x in range(len(paises)):

    if x != 0 and paises['Projeto'][x] != paises['Projeto'][x-1]:
        plt.bar(temp, temp2, zorder=2)
        plt.title("Contribuições por País - " + paises['Projeto'][x-1])
        plt.xlabel("Países")
        plt.ylabel("Número de contribuições")
        plt.grid(axis='y', linestyle='--', zorder=1)
        plt.show()
        temp = []
        temp2 = []

    temp.append(paises['País'][x])
    temp2.append(paises['Contribuições'][x])


plt.title("Contribuições por País - " + paises['Projeto'][len(paises)-1])
plt.bar(temp, temp2, zorder=2)
plt.xlabel("Países")
plt.ylabel("Número de contribuições")
plt.grid(axis='y', linestyle='--', zorder=1)
plt.show()
###########################################################################################

################################Gráfico dos abandonos#########################
abandonos = df.groupby(['Atualizado_em_Ano']).size().reset_index(name='Quantidade').sort_values('Atualizado_em_Ano', ascending=False).reset_index(drop=True)

outros = 0

for x in range(len(abandonos)):
    if x != 0 and x != 1:
        outros = outros + abandonos['Quantidade'][x]

plt.title("Último Ano de Atividade")
plt.pie(
    [abandonos['Quantidade'][0], abandonos['Quantidade'][1], outros],
    labels=('2025', '2024', 'Outros Anos'),
    autopct='%1.1f%%',
)
plt.show()
##########################################################################################

################################Abandonos por Projeto#####################################
paises = df.groupby(['Projeto', 'Atualizado_em_Ano']).size().reset_index(name='Quantidade').sort_values(['Projeto', 'Atualizado_em_Ano'], ascending=False).reset_index(drop=True)

temp = []
temp2 = []
outros = 0

for x in range(len(paises)):
    if x != 0 and paises['Projeto'][x] != paises['Projeto'][x-1]:
        temp.append('Outros Anos')
        temp2.append(outros)
        plt.pie(
            temp2,
            labels=temp,
            autopct='%1.1f%%',
        )
        plt.title("Último Ano de Atividade - " + paises['Projeto'][x-1])
        plt.show()
        temp = []
        temp2 = []
        outros = 0

    if paises['Atualizado_em_Ano'][x] == 2025 or paises['Atualizado_em_Ano'][x] == 2024:
        temp.append(paises['Atualizado_em_Ano'][x])
        temp2.append(paises['Quantidade'][x])
    else:
        outros = outros + paises['Quantidade'][x]

temp.append('Outros Anos')
temp2.append(outros)
plt.title("Último Ano de Atividade - " + paises['Projeto'][len(paises)-1])
plt.pie(
    temp2,
    labels=temp,
    autopct='%1.1f%%',
)
plt.show()
##########################################################################

################################Gráfico das Criações#########################
criacao = df.groupby(['Criado_em_Ano']).size().reset_index(name='Quantidade').sort_values('Criado_em_Ano', ascending=False).reset_index(drop=True)

plt.bar(criacao['Criado_em_Ano'],criacao['Quantidade'], zorder=2)
plt.title("Idade das Contas")
plt.xlabel("Ano de Criação")
plt.ylabel("Número de Contas")
plt.grid(axis='y', linestyle='--', zorder=1)
plt.show()
##########################################################################################

################################Criações por Projeto#####################################
criacao = df.groupby(['Projeto', 'Criado_em_Ano']).size().reset_index(name='Quantidade').sort_values('Projeto', ascending=False).reset_index(drop=True)

temp = []
temp2 = []

for x in range(len(criacao)):
    if x != 0 and criacao['Projeto'][x] != criacao['Projeto'][x-1]:
        plt.bar(temp, temp2, zorder=2)
        plt.title("Idade das Contas - " + criacao['Projeto'][x-1])
        plt.xlabel("Ano de Criação")
        plt.ylabel("Número de Contas")
        plt.grid(axis='y', linestyle='--', zorder=1)
        plt.show()
        temp = []
        temp2 = []

    temp.append(criacao['Criado_em_Ano'][x])
    temp2.append(criacao['Quantidade'][x])

plt.title("Idade das Contas - " + criacao['Projeto'][len(criacao)-1])
plt.bar(temp, temp2, zorder=2)
plt.xlabel("Ano de Criação")
plt.ylabel("Número de Contas")
plt.grid(axis='y', linestyle='--', zorder=1)
plt.show()
##########################################################################

#############################Contribuição po Ano de criação#########################
criacao = df.groupby(['Criado_em_Ano', 'Contribuições']).size().reset_index(name='Quantidade')

aux = 0
outro = 0
temp = []
temp2 = []
temp.append(0)
temp2.append(criacao['Criado_em_Ano'][0])

for x in range(len(criacao)):
    if criacao['Criado_em_Ano'][x] >= 2019:
        outro += (int(criacao['Quantidade'][x]) * int(criacao['Contribuições'][x]))
    elif x != 0 and criacao['Criado_em_Ano'][x] != criacao['Criado_em_Ano'][x-1]:
        aux += 1
        temp.append(0)
        temp2.append(criacao['Criado_em_Ano'][x])
    else:
        temp[aux] = temp[aux] + (int(criacao['Quantidade'][x]) * int(criacao['Contribuições'][x]))

temp2.append('Outros Anos')
temp.append(outro)

plt.title("Porcentagem de Contribuições por Idade de Conta")
plt.pie(
    temp,
    labels=temp2,
    autopct='%1.1f%%'
)
plt.show()

##################################################################################

####################################Contribuição po Ano de criação por projeto #######################################
criacao = df.groupby(['Criado_em_Ano', 'Contribuições', 'Projeto']).size().reset_index(name='Quantidade').sort_values(by=['Projeto', 'Criado_em_Ano'], ascending=False).reset_index(drop=True)

temp = []
temp2 = []
aux = 0

for x in range(len(criacao)):
    if x != 0 and criacao['Projeto'][x] != criacao['Projeto'][x-1]:
        plt.title("Contribuições por Idade de Conta - " + criacao['Projeto'][x-1])
        plt.bar(temp, temp2, zorder=2)
        plt.grid(axis='y', linestyle='--', zorder=1)
        plt.xlabel("Ano de Criação")
        plt.ylabel("Número de contribuições")
        plt.show()
        temp = []
        temp2 = []
        aux = 0
        temp.append(criacao['Criado_em_Ano'][x])
        temp2.append(int(criacao['Quantidade'][x]) * int(criacao['Contribuições'][x]))
    elif x == 0:
        temp.append(criacao['Criado_em_Ano'][x])
        temp2.append(int(criacao['Quantidade'][x]) * int(criacao['Contribuições'][x]))
    elif criacao['Criado_em_Ano'][x] != criacao['Criado_em_Ano'][x-1]:
        temp.append(criacao['Criado_em_Ano'][x])
        temp2.append(int(criacao['Quantidade'][x]) * int(criacao['Contribuições'][x]))
        aux += 1
    else:
        temp2[aux] = temp2[aux] + (int(criacao['Quantidade'][x]) * int(criacao['Contribuições'][x]))

plt.title("Contribuições por Idade de Conta - " + criacao['Projeto'][len(criacao)-1])
plt.bar(temp, temp2, zorder=2)
plt.grid(axis='y', linestyle='--', zorder=1)
plt.xlabel("Ano de Criação")
plt.ylabel("Número de contribuições")
plt.show()

######################################################################################################