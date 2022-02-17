import os
import folium
import json

# Vega data
veg = os.path.join('repo', 'vega.json')
vg = folium.Map(location=[42.3601, -71.0589], zoom_start=12)
folium.Marker([42.315140, -71.072450],
              popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(veg)), width=450, height=250))).add_to(vg)
vg.save('vegamap.html')
