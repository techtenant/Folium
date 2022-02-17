import folium
import os
import json

# Create map object
m = folium.Map(location=[-1.0954547038574476,37.0155143737793], zoom_start=12)

# Global tooltip
tooltip = 'Click For More Info'

# Create custom marker icon


# Geojson Data
overlay = os.path.join('repo', 'juja.json')

# Create markers
folium.Marker([
            -1.0928212548467073,37.017982006073],
              popup='<strong>Jkuat Swimming Pool</strong>',
              tooltip=tooltip).add_to(m),
folium.Marker([-1.092579899933815,37.01794981956482],
              popup='<strong>Jkuat Dam</strong>',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),
folium.Marker([-1.0970851884395656,37.01416254043579],
              popup='<strong>Administration Block</strong>',
              tooltip=tooltip,
              icon=folium.Icon(color='purple')).add_to(m),
folium.Marker([-1.092783710750433,37.011587619781494],
              popup='<strong>Jkuat Botanical Garden</strong>',
              tooltip=tooltip,
              icon=folium.Icon(color='green', icon='leaf')).add_to(m)

# Circle marker
folium.CircleMarker(
    location=[-1.1634,37.0812
],
    radius=50,
    popup='Juja Farm',
    color='#428bca',
    fill=True,
    fill_color='#428bca'
).add_to(m)

# Geojson overlay
folium.GeoJson(overlay, name='Juja Farm').add_to(m)

# Generate map
m.save('map.html')
