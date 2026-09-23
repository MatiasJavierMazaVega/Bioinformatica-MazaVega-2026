import re

def predecir_estructura_secundaria(secuencia):
    helices = set("MALEKQ")
    hojas_beta = set("VIYFTW")
    
    prediccion = []
    for aa in secuencia.upper():
        if aa in helices:
            prediccion.append("H")
        elif aa in hojas_beta:
            prediccion.append("B")
        else:
            prediccion.append("L")
            
    return "".join(prediccion)


secuencia_input = input("Ingresa la secuencia de aminoácidos: ").strip()

secuencia_limpia = re.sub(r"\s+", "", secuencia_input)

if secuencia_limpia:
    prediccion = predecir_estructura_secundaria(secuencia_limpia)

    print("\n--- Resultado ---")
    print(f"Secuencia:  {secuencia_limpia.upper()}")
    print(f"Predicción: {prediccion}")
else:
    print("No ingresaste ninguna secuencia válida.")