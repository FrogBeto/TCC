import pandas as pd

df = pd.read_csv('CSVs/Dados Finais/dados.csv', sep=';')

teste = df.groupby(['Longitude', 'Latitude']).size().reset_index(name='Quantidade').sort_values('Quantidade', ascending=False).reset_index(drop=True)

teste2 = []

for x in teste.groupby('Quantidade').mean().reset_index().sort_values('Quantidade', ascending=False).reset_index(drop=True)['Quantidade']:
    teste2.append(x)

print(teste2)