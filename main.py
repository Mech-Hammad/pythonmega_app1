import folium
import pandas as pd

# CureMd_Coordinates = [31.55821737676591, 74.3389953]
CureMd_Coordinates = [38.58, -99.09]
map = folium.Map(location=CureMd_Coordinates, zoom_start=6, tiles = "Stamen Terrain") #Curemd lahore

fg = folium.FeatureGroup(name="My Locations")

fg.add_child(folium.Marker(location=CureMd_Coordinates, popup="Cure MD", icon=folium.Icon(color='green')))

map.add_child(fg)

html = """<h4>Volcano information:</h4>
Height: %s m
"""

df = pd.read_csv("./Volcanoes.txt")
# print(df.head())

lat = df['LAT']
long = df["LON"]
location = df['LOCATION']
fg2 = folium.FeatureGroup(name="Volcanos")
for lt, lg ,loc in zip(lat, long, location):
    iframe = folium.IFrame(html=html % loc, width=200, height=100)
    fg2.add_child(folium.CircleMarker(location=[lt, lg], radius=5,  popup=folium.Popup(iframe), icon=folium.Icon(color='green')))


fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), style_function= lambda x: {"fillColor": "yellow"}))

map.add_child(fg2)

map.add_child(folium.LayerControl()) # This line after feture groups have been added for it to work

map.save("Map1.html")
# df2 = pd.read_json("./world.json")
# print(df2.head(()))
# for val1, val2 in zip(lat,long):
#     print((val1, val2))
