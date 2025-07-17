import os
import gdown

def descargar_archivos():
    os.makedirs("data", exist_ok=True)

    archivos = [
        {
            "url": "https://drive.google.com/uc?id=1iJqgnN7y9_r82Wr-UT_efGhSFuIF0qWP",
            "nombre": "imdb_dataset.csv"
        },
        {
            "url": "https://drive.google.com/uc?id=1RKrL7Bd_qyINZT0mAaCOiXNPShtxUl6Q",
            "nombre": "imdb_episodios.csv"
        },
        {
            "url": "https://drive.google.com/uc?id=1s3TkbU_wEUdhEf30nGDx_RZj1g5E0HgP",
            "nombre": "title.basics.tsv"
        },
        {
            "url": "https://drive.google.com/uc?id=102-W0uUUU7Y0O7UfXsj3zSnYhcahOAQA",
            "nombre": "title.episode.tsv"
        },
        {
            "url": "https://drive.google.com/uc?id=1zSVm9X-R7e3mYFy2MgID53Gs9DGq56h7",
            "nombre": "title.ratings.tsv"
        },
    ]

    for archivo in archivos:
        destino = os.path.join("data", archivo["nombre"])
        if not os.path.exists(destino):
            print(f"Descargando {archivo['nombre']}...")
            gdown.download(url=archivo["url"], output=destino, quiet=False, fuzzy=True)
        else:
            print(f"{archivo['nombre']} ya existe.")
