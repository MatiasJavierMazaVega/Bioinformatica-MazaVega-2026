import re
import ssl
import urllib.request

def resolver_rosalind_n_glicosilacion(ids_uniprot):
    patron = re.compile(r'(?=(N[^P][ST][^P]))')

    # Desactivar la verificación SSL estricta para evitar bloqueos locales
    contexto_ssl = ssl.create_default_context()
    contexto_ssl.check_hostname = False
    contexto_ssl.verify_mode = ssl.CERT_NONE

    for uniprot_id in ids_uniprot:
        uniprot_id = uniprot_id.strip()
        if not uniprot_id:
            continue

        id_base = uniprot_id.split('_')[0]
        url = f"https://rest.uniprot.org/uniprotkb/{id_base}.fasta"

        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, context=contexto_ssl) as response:
                lineas = response.read().decode('utf-8').splitlines()

                secuencia = "".join([linea for linea in lineas if not linea.startswith('>')])

                posiciones = [m.start() + 1 for m in patron.finditer(secuencia)]

                if posiciones:
                    print(uniprot_id)
                    print(" ".join(map(str, posiciones)))

        except Exception as e:
            print(f"Error procesando {uniprot_id}: {e}")

ids_15 = [
    "A2Z651",
    "B5ZC00",
    "P07204_TRFE_BOVIN",
    "P20840_R1A1_RAT",
    "P01892",
    "P00750_MGPT_PIG",
    "P10768",
    "P01008_ANT3_HUMAN",
    "P02751_FINC_HUMAN",
    "P19246",
    "P04083_ANXA1_HUMAN",
    "P12345",
    "P02769_ALBU_BOVIN",
    "P01012",
    "P10645_CMGA_HUMAN"
]

resolver_rosalind_n_glicosilacion(ids_15)