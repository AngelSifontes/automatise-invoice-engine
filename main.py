from pathlib import Path
import shutil 

CARPETA_FACTURAS = Path("facturas")
CARPETA_PROCESADAS = Path("procesadas")

for archivo in CARPETA_FACTURAS.iterdir():

    print(f"procesando : {archivo.name}") 
  
    destino = CARPETA_PROCESADAS / archivo.name
    
    shutil.move (archivo, destino)

print(f"Procesando : {archivo.name}")





