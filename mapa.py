import pandas as pd
import folium

df = pd.read_csv('CSVs/Dados Finais/dados.csv', sep=';')

pontos = df.groupby(['Longitude', 'Latitude']).size().reset_index(name='Quantidade').sort_values('Quantidade', ascending=False).reset_index(drop=True)

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

    def adicionar(self):
        folium.CircleMarker(
            location=[self.Latitude, self.Longitude],
            radius=(10 + int(self.Quantidade / 5)),
            color='red',
            stroke=False,
            fill=True,
            fill_opacity=(0.31 + (0.01 * self.Quantidade)),
        ).add_to(m)

for x in range(len(pontos)):
    aux = 0
    for y in pontos.groupby('Quantidade').mean().reset_index().sort_values('Quantidade', ascending=True).reset_index(drop=True)['Quantidade']:
        if pontos['Quantidade'][x] == y:
            ponto = Mapa(pontos['Longitude'][x], pontos['Latitude'][x], aux)
            ponto.adicionar()
        else:
            aux = aux + 1

m.save('Mapas/mapa.html')