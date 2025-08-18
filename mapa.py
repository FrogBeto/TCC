import pandas as pd
import folium

df = pd.read_csv('CSVs/Dados Finais/dados.csv', sep=';')

pontosCalor = df.groupby(['Longitude', 'Latitude']).size().reset_index(name='Quantidade').sort_values('Quantidade', ascending=False).reset_index(drop=True)
pontosProjetos = df.groupby(['Projeto', 'Longitude', 'Latitude']).size().reset_index(name='Quantidade').sort_values('Projeto', ascending=False).reset_index(drop=True)
quantProjetos = pontosProjetos.groupby(['Projeto', 'Quantidade']).mean().reset_index()
listaCor = [
    'red', '#D60270', '#9B4F96', '#0038A8', '#D52D00',
    '#EF7627', '#FF9A56', '#D162A4', '#B55690', '#A30262',
    '#5BCEFA', '#F5A9B8', '#000000', '#A3A3A3', '#800080',
    '#FF218C', '#FFD800', '#21B1FF', '#078D70', '#26CEAA',
    '#98E8C1', '#7BADE2', '#5049CC', '#3D1A78', '#FCF434',
    '#9C59D1', '#2C2C2C', '#FF8C00', '#FFED00', '#008026',
    '#004CFF', '#732982'
]

m = folium.Map(
    [0,0],
    zoom_start=2,
    world_copy_jump=True,
    tiles="Cartodb Positron",
    attributionControl=False
)

#Codigo respondavel por fazer radio button
# (necessario mudar o overlay
#folium.raster_layers.TileLayer(
#    tiles="CartoDB Positron",
#    overlay=False,
#    control=False,
#    show=True
#).add_to(m)

class Mapa:
    def __init__(self, longitude, latitude, quantidade, cor):
        self.Longitude = longitude
        self.Latitude = latitude
        self.Quantidade = quantidade
        self.Cor = cor

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
            color=self.Cor,
            stroke=False,
            fill=True,
            fill_opacity=(0.30 + (0.07 * self.Quantidade)),
        ).add_to(fg)

fg = folium.FeatureGroup(name='Mapa de Calor', show=True, overlay=True).add_to(m)
for x in range(len(pontosCalor)):
    aux = 0
    for y in pontosCalor.groupby('Quantidade').mean().reset_index().sort_values('Quantidade', ascending=True).reset_index(drop=True)['Quantidade']:
        if pontosCalor['Quantidade'][x] == y:
            ponto = Mapa(pontosCalor['Longitude'][x], pontosCalor['Latitude'][x], aux, listaCor[0])
            ponto.adicionar_calor()
        else:
            aux = aux + 1

ref = 0
for x in range(len(pontosProjetos)):
    aux = 0
    if x == 0 or pontosProjetos['Projeto'][x] != pontosProjetos['Projeto'][x-1]:
        fg = folium.FeatureGroup(name=pontosProjetos['Projeto'][x], show=False, overlay=True).add_to(m)
        ref = ref + 1

    for y in range(len(quantProjetos)):
        if pontosProjetos['Quantidade'][x] == quantProjetos['Quantidade'][y] and pontosProjetos['Projeto'][x] == quantProjetos['Projeto'][y]:
            ponto = Mapa(pontosProjetos['Longitude'][x], pontosProjetos['Latitude'][x], aux, listaCor[ref])
            ponto.adicionar_ponto()
        elif pontosProjetos['Projeto'][x] == quantProjetos['Projeto'][y]:
            aux = aux + 1

folium.LayerControl(sortLayers=True, hideSingleBase=True).add_to(m)
m.save('Mapas/mapa.html')