DESAFÍO I: ¿Podrías buscar un ejemplo de macromoléculas que almacenen información 
sobre la ‘identidad’ de un organismo dado?

El ácido desoxirribonucleico (ADN) es la macromolécula principal que almacena la información sobre 
la "identidad" e instrucciones genéticas de un organismo. 
En ciertos organismos (como virus), el ARN cumple esta función.


DESAFÍO II: Proponé una forma de expresar la información contenida en la estructura primaria 
de las proteínas usando tipos de datos de los lenguajes de programación que conocés.

La estructura primaria es una secuencia lineal de aminoácidos. 
Se puede representar con un string (cadena de caracteres) usando el código de una sola letra:

Ejemplo en Python:
# Representación como String
secuencia_primaria = "MKTIIALSYIFCLVFA"

Tambien podria representarse con una list (lista) de strings si preferimos trabajar con el código de tres letras:

Ejemplo en Python:
# Representación como Lista
secuencia_lista = ["Met", "Lys", "Thr", "Ile", "Ile"]


DESAFÍO III: ¿ En qué tipo de datos podrías expresar la información de la estructura terciaria proteica?

Se podria utilizar un diccionario anidado que contenga el nombre del aminoacido 
y las coordenas tridimencionales de sus atomos

Ej:

aminoacidos_3d = {
    "ALA": {
        "nombre": "Alanina",
        "esqueleto": {
            "N":  (-0.525,  1.363,  0.000),  # Nitrógeno amino
            "CA": ( 0.000,  0.000,  0.000),  # Carbono Alfa (Origen 0,0,0)
            "C":  ( 1.520,  0.000,  0.000),  # Carbono carboxílico
            "O":  ( 2.131, -1.062,  0.000)   # Oxígeno carboxílico
        },
        "cadena_lateral_R": {
            "CB": (-0.510, -0.732, -1.215)  # Representa a todo el grupo -CH3
        }
    },
    "GLY": {
        "nombre": "Glicina",
        "esqueleto": {
            "N":  (-0.525,  1.363,  0.000),
            "CA": ( 0.000,  0.000,  0.000),
            "C":  ( 1.520,  0.000,  0.000),
            "O":  ( 2.131, -1.062,  0.000)
        },
        "cadena_lateral_R": {
            "H":  (-0.510, -0.732, -1.215)  # En la glicina, R es solo un hidrógeno
        }
    }
}


DESAFÍO IV: Rosalind Franklin es una científica muy relevante, que tuvo menos reconocimiento del merecido. 
¿Cuáles fueron sus contribuciones en este campo? ¿Qué nos cuenta su historia acerca del mundo de la ciencia?

Contribuciones: Mediante difracción de rayos X, descubrió que el ADN existía en dos formas (A y B) 
y obtuvo los datos críticos que demostraban su estructura helicoidal, las dimensiones de la hélice 
y la posición externa de los grupos fosfato.

Su historia refleja la desigualdad de género a lo largo de la historia de la ciencia 
(al punto de entregar sus datos sin concentimiento a dos colegas varones) y la falta de reconocimiento de su labor en vida.


DESAFÍO VI: ¿Qué hace distintos a dos individuos de una especie? 
Propone una forma de corroborar tu respuesta realizando un diagrama de un posible método computacional para dicho fin.

Lo que hace distintos a dos individuos son las variaciones en su secuencia de ADN.

Diagrama de un Método Computacional:

 ┌────────────────────────┐         ┌────────────────────────┐
 │ Muestra ADN Individuo A│         │ Muestra ADN Individuo B│
 └───────────┬────────────┘         └───────────┬────────────┘
             │                                  │
             ▼                                  ▼
 ┌────────────────────────┐         ┌────────────────────────┐
 │ Secuenciación (Reads)  │         │ Secuenciación (Reads)  │
 └───────────┬────────────┘         └───────────┬────────────┘
             │                                  │
             └────────────────┬─────────────────┘
                              │
                              ▼
            ┌───────────────────────────────────┐
            │ Alineamiento vs Genoma Referencia │
            └─────────────────┬─────────────────┘
                              │
                              ▼
            ┌───────────────────────────────────┐
            │ Detección de Variantes (Variants) │
            └─────────────────┬─────────────────┘
                              │
                              ▼
            ┌───────────────────────────────────┐
            │       Matriz de Diferencias       │
            └───────────────────────────────────┘

Paso a paso:
1. Entrada de datos (Muestras de ADN): Partimos del ADN extraído de dos personas o seres vivos distintos.

2. Obtención de secuencias (Secuenciación): Se usan secuenciadores para convertir la información química del ADN 
en archivos de texto con lecturas compuestas por las letras A, C, G y T.

3. Mapeo (Alineamiento vs. Genoma de Referencia): Las lecturas obtenidas se comparan y se "acomodan" utilizando como molde 
el genoma de referencia de esa especie (un genoma estándar ya ensamblado).

4. Identificación de cambios: Un programa analiza posición por posición para buscar dónde la secuencia
del individuo difiere del genoma de referencia (identificando mutaciones puntuales, inserciones o deleciones).

5. Resultado final (Matriz de Diferencias): Se comparan las variantes encontradas en el Individuo A 
contra las del Individuo B. El resultado es un reporte que detalla exactamente qué letras cambian entre un individuo y otro, 
respondiendo qué los hace genéticamente distintos.