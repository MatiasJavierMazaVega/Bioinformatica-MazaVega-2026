import sys
import re

def buscar_promotores(archivo_path):
    try:
        with open(archivo_path, 'r') as f:
            secuencia_adn = f.read().replace('\n', '').replace('\r', '').upper()
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_path}' no fue encontrado.")
        return

    caja_tata = "TATAAA"
    
    patron = rf'(?=({caja_tata}(.*?){caja_tata}))'
    coincidencias = list(re.finditer(patron, secuencia_adn))
    
    if not coincidencias:
        print("No se encontraron regiones delimitadas entre dos cajas TATA.")
        return

    for idx, match in enumerate(coincidencias, 1):
        caja_inicio = caja_tata
        interna = match.group(2)
        caja_fin = caja_tata
        
        # Agrupa la secuencia interna en bloques de 3 caracteres
        interna_tripletos = " ".join([interna[i:i+3] for i in range(0, len(interna), 3)])
        
        # Arma la cadena formateada solo con espacios
        if interna_tripletos:
            region_formateada = f"{caja_inicio} {interna_tripletos} {caja_fin}"
        else:
            region_formateada = f"{caja_inicio} {caja_fin}"
            
        print(f"Región {idx}: {region_formateada}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python desafioIII.py archivoAdn.txt")
    else:
        buscar_promotores(sys.argv[1])