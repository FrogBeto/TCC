import folium

raio = 10

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
            radius=raio,
            color='red',
            stroke=False,
            fill=True,
            fill_opacity=0.1,
        ).add_to(m)