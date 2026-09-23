import logomaker
import pandas as pd
import matplotlib.pyplot as plt

# 1. Lista de secuencias del desafío
secuencias = [
    "MLPGLALLLLAAWTMRALEVPTDGNAPLLVEPQIAMFCGRLNMHMNVQNGKWDSDPSGTKTCIDTKEGILQYCQEVYPELQITNVVEANQPVTIQNWCKRGRAQCKTHPHFVIPYRCLVGEFVSDALLAPDKCKFLHQERMDVCETHLHWHTV",
    "MLPGLALLLLAAWTARALEVPTDGNAGLLAEPQIAMFCGRLNMHMNVQNGKWDSDPSGTKTCIDTKEGILQYCQEVYPELQITNVVEANQPVTIQNWCKRGRKQCKTHPHFVIPYRCLVGEFVSDALLVPDKCKFLHQERMDVCETHLHWHTV",
    "MLPGLALLLLAAWTARALEVPTDGNAGLLAEPQIAMFCGRLNMHMNVQNGKWDSDPSGTKTCIDTKEGILQYCQEVYPELQITNVVEANQPVTIQNWCKRGRKQCKTHPHFVIPYRCLVGEFVSDALLVPDKCKFLHQERMDVCETHLHWHTV"
]

# 2. Generar matriz de conteos
counts_mat = logomaker.alignment_to_matrix(secuencias)

# 3. Transformar a matriz de información (bits)
info_mat = logomaker.transform_matrix(counts_mat, from_type='counts', to_type='information')

# 4. Crear el Sequence Logo
fig, ax = plt.subplots(figsize=(16, 4))
logo = logomaker.Logo(info_mat, ax=ax)

# 5. Personalización estética
logo.ax.set_ylabel('Información (bits)', fontsize=12)
logo.ax.set_xlabel('Posición en la secuencia', fontsize=12)
logo.ax.set_title('Sequence Logo - Desafío VIII', fontsize=14, fontweight='bold')

# Guardar y mostrar
plt.tight_layout()
plt.savefig('desafio_VIII_logo.png', dpi=300)
plt.show()