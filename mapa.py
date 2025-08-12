import pandas as pd
import folium

df = pd.read_csv('CSVs/Dados Finais/dados.csv', sep=';')
longi = []
lati = []

for x in df['Longitude']:
    longi.append(x)
for x in df['Latitude']:
    lati.append(x)

m = folium.Map(
    [0,0],
    zoom_start=2,
    world_copy_jump=True,
    tiles="Cartodb Positron"
)

class Mapa:
    def __init__(self, longitude, latitude):
        self.Longitude = longitude
        self.Latitude = latitude

    def adicionar(self):
        folium.CircleMarker(
            location=[self.Latitude, self.Longitude],
            radius=20,
            color='red',
            stroke=False,
            fill=True,
            fill_opacity=0.01,
        ).add_to(m)

for x in range(len(longi)):
    ponto = Mapa(df['Longitude'][x], df['Latitude'][x])#longi[x], lati[x])
    ponto.adicionar()

m.save('Mapas/mapa.html')