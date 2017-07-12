import folium
import pandas

data = pandas.read_csv("gm_major_cities.csv")

lat = list(data['lat'])
lon = list(data['lng'])
city = list(data['city'])
country = list(data['country'])

def color_picker(country):
    if country == 'Ghana':
        return 'red'
    elif country == 'Mexico':
        return 'green'
    else:
        return 'black'
map = folium.Map(location=[5.6, 0.1780], zoom_start = 8, tiles = "Mapbox Bright")

major_cities_fg = folium.FeatureGroup(name = 'Major Cities')

for lt, ln, ci, co in zip(lat,lon,city, country):
    major_cities_fg.add_child(folium.CircleMarker(location = [lt,ln],
                                                  popup = ci,
                                                  radius = 6,
                                                  fill_color = color_picker(co),
                                                  color = 'black',
                                                  fill_opacity=0.6
                                                  )
                            )

population_fg = folium.FeatureGroup(name = 'Population')

population_fg.add_child(folium.GeoJson(
    data = open('world.json', 'r', encoding = 'utf-8-sig'),
    style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
        else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(major_cities_fg)
map.add_child(population_fg)
map.add_child(folium.LayerControl() )

map.save("Map1.html")
