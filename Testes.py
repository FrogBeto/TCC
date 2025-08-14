import pandas as pd
import folium

df = pd.read_csv('CSVs/Dados Finais/dados.csv', sep=';')

teste = df.groupby(['Projeto', 'Longitude', 'Latitude']).size().reset_index(name='Quantidade').sort_values('Projeto', ascending=False).reset_index(drop=True)

teste2 = teste.groupby(['Projeto', 'Quantidade']).mean().reset_index()
teste3 = []
for x in range(len(teste2)):
    print(teste2['Projeto'][x], teste2['Quantidade'][x])

m = folium.Map()

fg = folium.FeatureGroup(name="Icon collection", show=False).add_to(m)
folium.Marker(location=(0, 0), icon=folium.Icon(color="red")).add_to(fg)
folium.Marker(location=(1, 1), icon=folium.Icon(color="red")).add_to(fg)
folium.Marker(location=(2, 2), icon=folium.Icon(color="green")).add_to(fg)
folium.Marker(location=(3, 3), icon=folium.Icon(color="green")).add_to(fg)

fg = folium.FeatureGroup(name="Teste do Teste", show=False).add_to(m)
folium.Marker(location=(2, 2), icon=folium.Icon(color="green")).add_to(fg)
folium.Marker(location=(3, 3), icon=folium.Icon(color="green")).add_to(fg)


folium.LayerControl().add_to(m)

m.save('Mapas/Teste.html')

print(teste)
print(teste2)