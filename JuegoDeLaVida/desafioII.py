import sys

# Diccionario estándar de aminoácidos a codones de ARNm
CODIGO_GENETICO = {
    'A': 'GCU', 'C': 'UGU', 'D': 'GAU', 'E': 'GAA', 'F': 'UUU',
    'G': 'GGU', 'H': 'CAU', 'I': 'AUU', 'K': 'AAA', 'L': 'UUA',
    'M': 'AUG', 'N': 'AAU', 'P': 'CCU', 'Q': 'CAA', 'R': 'CGU',
    'S': 'AGU', 'T': 'ACU', 'V': 'GUU', 'W': 'UGG', 'Y': 'UAU'
}

def proteina_a_arn(secuencia_prot):
    arn = []
    for aa in secuencia_prot.upper():
        if aa in CODIGO_GENETICO:
            arn.append(CODIGO_GENETICO[aa])
        else:
            arn.append('???')
    return " ".join(arn)

if __name__ == "__main__":
    secuencia_ejemplo = 'ATVEKGGKHKTGPNEKGKKIFVQKCSQCHTVLHGLFGRKTGQA'

    # Permite agregar el argumento en la linea de comando
    if len(sys.argv) > 1:
        secuencia_ejemplo = sys.argv[1]
        
    arn_resultado = proteina_a_arn(secuencia_ejemplo)
    print(f"Secuencia de Aminoácidos: {secuencia_ejemplo}")
    print(f"Secuencia de ARNm resultante: {arn_resultado}")