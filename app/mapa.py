import folium


m = folium.Map(
    location=[-22.239262, -54.837849],
    zoom_start = 14
)
folium.Marker(
        [-22.239490, -54.837697],
        popup = '<i>M.I. Studio</i>',
        tooltip = 'Clique aqui!'
    ).add_to(m)

m.save('mapa.html')