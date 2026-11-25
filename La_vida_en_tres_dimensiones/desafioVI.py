import json
import matplotlib.pyplot as plt

# Ruta al archivo JSON de métricas del modelo
json_filename = 'test_3b510_scores_rank_003_alphafold2_ptm_model_1_seed_000.json'  # Reemplazar con el nombre real del archivo

# Cargar los datos pLDDT
try:
    with open(json_filename, 'r') as f:
        data = json.load(f)
    
    # Dependiendo de la versión de salida, el pLDDT por residuo suele estar en la clave 'plddt'
    plddt_scores = data.get('plddt', [])
    
    if not plddt_scores:
        # Alternativa para formatos donde se extrae de las métricas por residuo
        plddt_scores = data.get('per_residue_confidence', [])

    if plddt_scores:
        residue_positions = list(range(1, len(plddt_scores) + 1))

        # Generar el gráfico
        plt.figure(figsize=(10, 5))
        plt.plot(residue_positions, plddt_scores, color='blue', linewidth=1.5)
        plt.axhline(y=70, color='orange', linestyle='--', label='Confianza media (70)')
        plt.axhline(y=90, color='green', linestyle='--', label='Alta confianza (90)')
        
        plt.title('Confianza Local (pLDDT) por Posición de Residuo - VE7_HPV16', fontsize=12)
        plt.xlabel('Posición del Residuo (Número de Secuencia)', fontsize=10)
        plt.ylabel('Puntaje pLDDT (0 - 100)', fontsize=10)
        plt.ylim(0, 105)
        plt.legend(loc='lower right')
        plt.grid(True, linestyle=':', alpha=0.6)
        plt.tight_layout()
        plt.show()
    else:
        print("No se encontraron datos de pLDDT en el archivo JSON especificado.")

except FileNotFoundError:
    print(f"No se pudo encontrar el archivo: {json_filename}. Verifique la ruta.")