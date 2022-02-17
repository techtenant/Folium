
import geojson
import os
import folium
stima = os.path.join('repo', 'kenyagrid.geojson')
m = folium.Map(
    location=[-1.2886,36.8229],
    tiles='Mapbox Bright',
    zoom_start=2
)

folium.GeoJson(
    stima,
    name='geojson'
).add_to(m)



folium.LayerControl().add_to(m)

m.save('stima.html')

