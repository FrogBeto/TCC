import pandas as pd
import folium

df = pd.read_csv('CSVs/Dados Finais/dados.csv', sep=';')

pontosCalor = df.groupby(['Longitude', 'Latitude']).size().reset_index(name='Quantidade').sort_values('Quantidade', ascending=False).reset_index(drop=True)
pontosProjetos = df.groupby(['Projeto', 'Longitude', 'Latitude']).size().reset_index(name='Quantidade').sort_values('Projeto', ascending=False).reset_index(drop=True)
quantProjetos = pontosProjetos.groupby(['Projeto', 'Quantidade']).mean().reset_index()

m = folium.Map(
    [0,0],
    zoom_start=2,
    world_copy_jump=True,
    tiles="Cartodb Positron"
)

class Mapa:
    def __init__(self, longitude, latitude, quantidade):
        self.Longitude = longitude
        self.Latitude = latitude
        self.Quantidade = quantidade

    def adicionar_calor(self):
        folium.CircleMarker(
            location=[self.Latitude, self.Longitude],
            radius=(10 + int(self.Quantidade / 5)),
            color='red',
            stroke=False,
            fill=True,
            fill_opacity=(0.31 + (0.01 * self.Quantidade)),
        ).add_to(fg)

    def adicionar_ponto(self):
        folium.CircleMarker(
            location=[self.Latitude, self.Longitude],
            radius=(10 + self.Quantidade),
            color='green',
            stroke=False,
            fill=True,
            fill_opacity=(0.30 + (0.07 * self.Quantidade)),
        ).add_to(fg)

fg = folium.FeatureGroup(name='Mapa de Calor', show=True).add_to(m)
for x in range(len(pontosCalor)):
    aux = 0
    for y in pontosCalor.groupby('Quantidade').mean().reset_index().sort_values('Quantidade', ascending=True).reset_index(drop=True)['Quantidade']:
        if pontosCalor['Quantidade'][x] == y:
            ponto = Mapa(pontosCalor['Longitude'][x], pontosCalor['Latitude'][x], aux)
            ponto.adicionar_calor()
        else:
            aux = aux + 1

for x in range(len(pontosProjetos)):
    aux = 0
    if x == 0 or pontosProjetos['Projeto'][x] != pontosProjetos['Projeto'][x-1]:
        fg = folium.FeatureGroup(name=pontosProjetos['Projeto'][x], show=False).add_to(m)

    for y in range(len(quantProjetos)):
        if pontosProjetos['Quantidade'][x] == quantProjetos['Quantidade'][y] and pontosProjetos['Projeto'][x] == quantProjetos['Projeto'][y]:
            ponto = Mapa(pontosProjetos['Longitude'][x], pontosProjetos['Latitude'][x], aux)
            ponto.adicionar_ponto()
        elif pontosProjetos['Projeto'][x] == quantProjetos['Projeto'][y]:
            aux = aux + 1

folium.LayerControl().add_to(m)
m.save('Mapas/mapa.html')