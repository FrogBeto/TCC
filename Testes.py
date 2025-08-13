import pandas as pd

df = pd.read_csv('CSVs/Dados Finais/dados.csv', sep=';')

teste = df.groupby(['Projeto', 'Longitude', 'Latitude']).size().reset_index(name='Quantidade').sort_values('Quantidade', ascending=False).reset_index(drop=True)

teste2 = teste.groupby(['Projeto', 'Quantidade']).mean().reset_index()
teste3 = []
for x in teste2
print(teste2)