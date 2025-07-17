import os
import gdown 

import os
import gdown

def descargar_archivos():
    os.makedirs("data", exist_ok=True)

    archivos = [
        {
            "url": "https://drive.google.com/uc?id=1Pb8CFXazZQ4zLOPW_BLFyFiBKGawvoU3",
            "nombre": "imdb_dataset.csv"
        },
        {
            "url": "https://drive.google.com/uc?id=1ex1ucXsqtpCV4pFitiaO9oeD9zspUadF",
            "nombre": "imdb_episodios.csv"
        },
        {
            "url": "https://drive.google.com/uc?id=1MA7_9Kw5f6eIkS90PV4T39UPNy0x3CRS",
            "nombre": "title.basics.tsv"
        },
        {
            "url": "https://drive.google.com/uc?id=12ntBwyiGHRI6r0KhYRQ1AJ2wtj3gUZn0",
            "nombre": "title.episode.tsv"
        },
        {
            "url": "https://drive.google.com/uc?id=1klytyFnwldFyvkHPKUg-cmJjxBKOZ9l7",
            "nombre": "title.ratings.tsv"
        },
    ]

    for archivo in archivos:
        destino = os.path.join("data", archivo["nombre"])
        if not os.path.exists(destino):
            print(f"Descargando {archivo['nombre']}...")
            gdown.download(archivo["url"], destino, quiet=False)
        else:
            print(f"{archivo['nombre']} ya existe.")
