import sys
import time

# --- COLORES ANSI PARA LA CONSOLA ---
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAGENTA = "\033[95m"

def texto_lento(texto, velocidad=0.04):
    """Efecto visual de maquina de escribir."""
    for caracter in texto:
        sys.stdout.write(caracter)
        sys.stdout.flush()
        time.sleep(velocidad)
    print()

def limpiar_pantalla():
    time.sleep(0.01) 
    print("\n" + "="*60 + "\n")



def presentacion():
    print(f"{BOLD}{MAGENTA}🎭 =========================================== 🎭{RESET}")
    texto_lento(f"{BOLD}{MAGENTA}      EXPRESIÓN GÉNICA: EL SHOW DE LA VIDA     {RESET}")
    print(f"{BOLD}{MAGENTA}🎭 =========================================== 🎭{RESET}")
    
    texto_lento(f"\n{BOLD}¡Bienvenido@ al Gran Teatro Celular!{RESET}")
    texto_lento("Hoy te ponés en el rol de director/a. Tu misión es lograr que el guión")
    texto_lento("almacenado en el ADN se convierta en una Proteína funcional.")
    texto_lento("Un solo error y la obra será un desastre biológico!!!")

def acto_1_transcripcion():
    limpiar_pantalla()
    texto_lento(f"{BOLD}{CYAN}--- ACTO 1: LA TRANSCRIPCIÓN ---{RESET}")
    texto_lento(f"{YELLOW}Escenario: El Núcleo (El camarín del ADN){RESET}\n")
    
    texto_lento("El ADN (Guionista) está cómodamente guardado en el núcleo,")
    texto_lento("fuertemente compactado alrededor de sus asistentes de vestuario: LAS HISTONAS.")
    texto_lento("Para comenzar la obra, el gen necesita ser leído por la ARN POLIMERASA.\n")

    texto_lento(f"{BOLD}Decisión 1: ¿Cómo accedemos al guión del ADN?{RESET}")
    texto_lento("1. Intentar copiar el ADN sin desarmar la estructura de la cromatina.")
    texto_lento("2. Aplicar modificaciones epigenéticas (desacetilación) para apretar más el ADN.")
    texto_lento("3. Relajar la cromatina (acetilación de Histonas) para desenrollar el ADN y exponer el promotor.")

    opcion = input(f"\n{BOLD}Elige una acción (1-3): {RESET}")

    if opcion == "3":
        texto_lento(f"\n{GREEN}¡EXCELENTE!{RESET} La acetilación reduce la carga positiva de las histonas,")
        texto_lento("permitiendo que el ADN se desenrolle. La ARN Polimerasa entra a la secuencia promotora.")
    else:
        texto_lento(f"\n{RED}❌ ERROR TÉCNICO:{RESET} El ADN estaba demasiado inaccesible.")
        texto_lento("Sin acceso al promotor, la ARN Polimerasa no puede unirse. Reintentando fase...")
        time.sleep(2)
        return acto_1_transcripcion()

    texto_lento(f"\n{CYAN}La ARN Polimerasa comienza a sintetizar el pre-ARN mensajero...{RESET}")
    texto_lento("Si la hebra de ADN tiene la secuencia:  [ T - A - C - G - A - T ]")
    
    texto_lento(f"\n{BOLD}Decisión 2: ¿Cuál es la cadena complementaria de ARN que debe sintetizar la Polimerasa?{RESET}")
    texto_lento("1. A - T - G - C - T - A ")
    texto_lento("2. A - U - G - C - U - A ")
    texto_lento("3. T - A - C - G - A - T ")

    opcion2 = input(f"\n{BOLD}Elige la secuencia correcta (1-3): {RESET}")

    if opcion2 == "2":
        texto_lento(f"\n{GREEN}¡IMPECABLE!{RESET} En el ARN, el Uracilo (U) reemplaza a la Timina (T).")
        texto_lento("El pre-ARNm (el borrador del guion) ha sido sintetizado exitosamente.")
    else:
        texto_lento(f"\n{RED}❌ ERROR DE TRANSCRIPCIÓN:{RESET} Recuerda que el ARN no usa Timina (T) sino Uracilo (U).")
        time.sleep(2)
        return acto_1_transcripcion()

def intermedio_splicing():
    limpiar_pantalla()
    texto_lento(f"{BOLD}{MAGENTA}--- INTERMEDIO: EL SPLICING (Edición de Guion) ---{RESET}")
    texto_lento(f"{YELLOW}Escenario: El Núcleo (Zona de Edición){RESET}\n")

    texto_lento("El pre-ARNm recién transcripto tiene partes útiles y fragmentos que son básicamente basura.")
    texto_lento("El Complejo de Corte y Empalme (Spliceosoma) entra en acción para editar la copia de trabajo.\n")

    texto_lento(f"{BOLD}Decisión 3: ¿Qué secciones debemos conservar para tener un ARNm maduro listo para salir al citoplasma?{RESET}")
    texto_lento("1. Cortar los EXONES y conservar únicamente los INTRONES.")
    texto_lento("2. Cortar los INTRONES y empalmar/pegar los EXONES.")
    texto_lento("3. Exportar todo el borrador intacto directamente al citoplasma sin cortar nada.")

    opcion = input(f"\n{BOLD}Elige la opción de edición (1-3): {RESET}")

    if opcion == "2":
        texto_lento(f"\n{GREEN}¡GUION EDITADO CON ÉXITO!{RESET}")
        texto_lento("Los INTRONES (secuencias no codificantes) son eliminados y los EXONES se unen.")
        texto_lento(f"{BOLD}El ARNm maduro (Cadete) sale triunfal hacia el Citoplasma.{RESET}")
    else:
        texto_lento(f"\n{RED}❌ PROCESO FALLIDO:{RESET} Si dejas los intrones o tiras los exones, la proteína resultante")
        texto_lento("no tendrá sentido y será degradada por la célula. Reintentando edición...")
        time.sleep(2)
        return intermedio_splicing()

def acto_2_traduccion():
    limpiar_pantalla()
    texto_lento(f"{BOLD}{GREEN}--- ACTO 2: LA TRADUCCIÓN ---{RESET}")
    texto_lento(f"{YELLOW}Escenario: El Citoplasma (El Gran Escenario / Taller de Ensamble){RESET}\n")

    texto_lento("El ARNm (Cadete) llega al Citoplasma y se incorpora a la fábrica:")
    texto_lento("¡EL RIBOSOMA!")
    texto_lento("El ribosoma va leyendo el guión en secciones de tres nucleótidos, llamadas CODONES.\n")

    texto_lento(f"{BOLD}Decisión 4: ¿Cuál es el codón de inicio que marca el comienzo de la traducción?{RESET}")
    texto_lento("1. AUG (que codifica para Metionina)")
    texto_lento("2. UAA (codón de parada)")
    texto_lento("3. CCC (que codifica para Prolina)")

    opcion = input(f"\n{BOLD}Elige el codón de inicio (1-3): {RESET}")

    if opcion == "1":
        texto_lento(f"\n{GREEN}¡TELÓN ARRIBA!{RESET} El ARNt de transferencia (El Peón) con el anticodón UAC")
        texto_lento("trae el primer ladrillo: la Metionina.")
    else:
        texto_lento(f"\n{RED}EL RIBOSOMA NO ARRANCA:{RESET} La traducción siempre inicia con el codón AUG.")
        time.sleep(2)
        return acto_2_traduccion()

    texto_lento(f"\n{CYAN}El Ribosoma avanza, los ARNt continúan trayendo aminoácidos y formando enlaces peptídicos...{RESET}")
    texto_lento("De repente, el Ribosoma se topa con un codón UAG (Codón de Parada).\n")

    texto_lento(f"{BOLD}Decisión 5: ¿Qué debe ocurrir al detectar el codón de parada?{RESET}")
    texto_lento("1. Traer un ARNt especial cargado con un aminoácido extra de seguridad.")
    texto_lento("2. Ignorar el codón y seguir traduciendo hasta agotar el ARNm.")
    texto_lento("3. Reclutar un Factor de Liberación para desacoplar el complejo y liberar la cadena polipeptídica.")

    opcion2 = input(f"\n{BOLD}Elige la instrucción de cierre (1-3): {RESET}")

    if opcion2 == "3":
        texto_lento(f"\n{GREEN}¡TRADUCCIÓN COMPLETA!{RESET} La cadena lineal de aminoácidos ha sido liberada.")
    else:
        texto_lento(f"\n{RED}ERROR DE TERMINACIÓN:{RESET} Los codones de parada no codifican aminoácidos,")
        texto_lento("sino que unen factores de liberación. Reintentando finalización...")
        time.sleep(2)
        return acto_2_traduccion()

def gran_final():
    limpiar_pantalla()
    texto_lento(f"{BOLD}{YELLOW}--- EL GRAN FINAL: EL PLEGAMIENTO PROTEICO ---{RESET}\n")

    texto_lento("La cadena de aminoácidos recién sintetizada no puede actuar de forma lineal.")
    texto_lento("Necesita adoptar su estructura tridimensional activa (Terciaria/Cuaternaria).")
    texto_lento("Las proteínas de plegamiento ayudan a que se adapte correctamente.\n")

    texto_lento(f"{BOLD}{GREEN}✨ ¡APLAUSOS DE PIE EN EL TEATRO CELULAR! ✨{RESET}")
    texto_lento(f"{BOLD}La Proteína está perfectamente plegada, funcional y lista para trabajar!{RESET}\n")

    texto_lento("RECAPITULACIÓN DEL SHOW:")
    texto_lento(" - ADN + Histonas ➡️  Transcripción en el Núcleo (vía ARN Polimerasa)")
    texto_lento(" - Pre-ARNm ➡️  Splicing (Corte de Intrones / Empalme de Exones)")
    texto_lento(" - ARNm maduro ➡️  Viaje al Citoplasma")
    texto_lento(" - Ribosomas + ARNt + Aminoácidos ➡️  Traducción por Codones")
    texto_lento(" - Plegamiento ➡️  Proteína Funcional en 3D\n")
    
    texto_lento(f"{BOLD}{MAGENTA}¡Felicitaciones! Has completado la obra con éxito.{RESET}\n")

def ejecutar_juego():
    presentacion()
    acto_1_transcripcion()
    intermedio_splicing()
    acto_2_traduccion()
    gran_final()

if __name__ == "__main__":
    ejecutar_juego()