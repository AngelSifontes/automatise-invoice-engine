from pathlib import Path
import shutil 

CARPETA_FACTURAS = Path("facturas")
CARPETA_PROCESADAS = Path("procesadas")

for archivo in CARPETA_FACTURAS.iterdir():

   if archivo.suffix.lower() != ".pdf":
    
       print(f"Ignorado : {archivo.name}")
       continue


   print(f"Procesando: {archivo.name}") 
  
   destino = CARPETA_PROCESADAS / archivo.name
    
   shutil.move(archivo, destino)

   print(f"Procesado : {archivo.name}")





