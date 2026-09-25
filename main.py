from pathlib import Path

CARPETA_FACTURAS = Path("facturas")

archivos = list(CARPETA_FACTURAS.iterdir())

for archivo in archivos: 
    print(archivo.name)




