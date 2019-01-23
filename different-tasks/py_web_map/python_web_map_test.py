#!/usr/bin/env python3
import folium
from folium.plugins import MarkerCluster


def color_change(elev):
    if (elev < 1000):
        return ('green')
    elif (1000 <= elev < 3000):
        return ('orange')
    else:
        return ('red')

map = folium.Map(location=[37.296933, -121.9574983], zoom_start=5,
                 tiles="CartoDB dark_matter")

marker_cluster = MarkerCluster().add_to(map)

with open("Volcanoes_USA.txt") as f:
    for i, line in enumerate(f):
        if (i > 0):
            line = line.strip().split(',')
            lat = float(line[8])
            lon = float(line[9])
            elevation = int(line[5].split('.')[0])
            folium.CircleMarker(location=[lat, lon], radius=9,
                popup=str(elevation) + " m",
                fill_color=color_change(elevation),
                color="gray", fill_opacity=0.9).add_to(marker_cluster)

map.save("map2_test.html")
