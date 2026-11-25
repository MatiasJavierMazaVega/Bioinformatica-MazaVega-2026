-PARA PENSAR 🤔:¿Por qué una célula querría destruir sus propias proteínas?

La destrucción controlada de proteínas es un mecanismo regulador fundamental y de control de calidad en la célula. Permite:
1. Regulación del ciclo celular: Eliminar ciclinas y otras proteínas clave en momentos precisos para permitir la progresión celular.
2. Control de calidad: Degradar proteínas mal plegadas, mutadas o dañadas por estrés oxidativo para evitar agregados tóxicos.
3. Respuesta rápida a estímulos: Ajustar las concentraciones de enzimas o factores de transcripción según las necesidades metabólicas o ambientales.

-PARA PENSAR 🤔:¿Qué información nos provee esta página [PDB - 1UBQ]?

Provee metadatos completos sobre el experimento estructural: título de la publicación asociada, 
autores, método experimental utilizado (en este caso, Difracción de rayos X), resolución cristalográfica, 
organismo de origen (Homo sapiens), secuencia de aminoácidos, enlaces a otras bases de datos (ej, UniProt) 
y archivos descargables de coordenadas.

-PARA PENSAR 🤔:¿Cómo se determinó la estructura de esta proteína? A la izquierda vemos una representación de la estructura de ubiquitina. 
¿Qué significan las cintas, las flechas y las regiones angostas?

La estructura 1UBQ se determinó mediante Cristalografía de rayos X (a 1.8 Å de resolución). En la representación visual:
* Cintas anchas / espirales: Representan estructuras secundarias organizadas, específicamente hélices alfa (alpha-helices).
* Flechas: Representan hebras beta (beta-strands), que juntas forman hojas beta (beta-sheets).
* Regiones angostas / hilos: Corresponden a bucles (loops o turns) que conectan los elementos de estructura secundaria.

-PARA PENSAR 🤔:¿Representa esa imagen a la realidad del sistema biológico?

Es una aproximación estática y simplificada. No refleja la dinámica molecular real: ignora la agitación térmica, 
las fluctuaciones conformacionales, la interacción constante con moléculas de agua del solvente y el entorno celular dinámico. 
Es una fotografía congelada en tiempo y espacio.

-PARA PENSAR 🤔:La estructura 1UBQ fue “refinada a una resolución de 1.8 Angstroms”. 
Éste es el error asociado al experimento: mientras mayor es la resolución, menor es la certeza al determinar la posición de cada átomo 
¿Cuál es la utilidad y los condicionamientos de usar un modelo científico que sabemos inexacto?

* Utilidad: Permite inferir mecanismos catalíticos, identificar sitios de unión a ligandos, 
comprender la estabilidad termodinámica y diseñar experimentos o fármacos racionales.
* Condicionamientos: Al ser un modelo atómico derivado de datos experimentales indirectos con un margen de error (+-1.8Å), 
la posición exacta de cada átomo es una probabilidad ajustada a restricciones estereoquímicas, no una certeza absoluta.


-PARA PENSAR 🤔:¿Qué diferencias y similitudes notamos respecto de la representación inicial (comparacion con pestaño 3DView/Structure)? 

Las elices, hojas y bucles estan representadas de la misma forma, solo que de un solo color uniforme. 
Ademas se pueden ver moléculas de agaua representadas como esferas rojas.

-PARA PENSAR 🤔: En el menú de la izquierda hay opciones de distintos tipos de representación y 
formas de colorear la estructura tridimensional. ¿Para qué podría ser útil visualizar lo mismo de distintas maneras?

Las representaciones alternativas conservan las coordenadas espaciales pero resaltan propiedades distintas.
Cambiar la visualización permite enfocar el análisis en aspectos topográficos, electrostáticos o estereoquímicos particulares,
como por ejemplo la ubicación de cavidades.

-PARA PENSAR 🤔:¿Qué información esperaría encontrar como resultado un experimento destinado a determinar 
la estructura terciaria de una molécula biológica?

Las coordenadas cartesianas tridimensionales (x, y, z) de cada uno de los átomos que componen la macromolécula.

-PARA PENSAR 🤔: ¿En qué consiste un archivo PDB?

Es un archivo de texto plano estructurado en formato de columnas fijas que almacena los registros atómicos, metadatos experimentales, 
conexiones y secuencias de macromoléculas biológicas.

-PARA PENSAR 🤔:Desplacémonos por el archivo hasta encontrar las líneas que comienzan con la palabra ATOM. 
¿Qué tipo de información brinda esta sección?

Cada línea ATOM describe un átomo específico de la proteína e incluye: número de átomo, nombre del átomo (ej. CA, N, O), 
nombre del residuo aminoacídico, cadena, número de residuo, y sus coordenadas espaciales en Angstroms (X, Y, Z), 
además de la ocupancia y el factor B.

-PARA PENSAR 🤔:¿Podríamos extraer de este archivo información sobre la estructura primaria de la proteína en cuestión? 
¿Cómo se presenta dicha información y qué significa la representación? 
Desde el punto de vista computacional: ¿de qué tipo de dato se trata esta información?

La secuencia primaria se puede extraer ordenando los residuos secuencialmente a partir de los registros ATOM (o leyendo la sección SEQRES). 
Computacionalmente, se trata de una cadena de caracteres (string) o una lista ordenada de tuplas que representan los aminoácidos en orden N-terminal a C-terminal.

-PARA PENSAR 🤔: ¿Considera que el formato PDB es útil para presentar los resultados del experimento?

Si bien presenta una estructura bien definida que podría entenderse rápido si ya se sabe del tema, es díficil de entender a simple vista.

-PARA PENSAR 🤔: Observamos que la información respeta cierta estructura interna. 
¿Cuáles son los beneficios y las limitaciones de imponer una estructura para comunicar los resultados de un experimento?

* Beneficios: Estandarización internacional, interoperabilidad universal entre programas de visualización y software de cálculo, 
y facilidad para el procesamiento automatizado mediante scripts (ej. en Python).
* Limitaciones: Rigidez estructural de formato, dificultad para representar estados múltiples o ensamblajes macromoleculares altamente complejos.

-Hemos visto que las proteínas tienen estructura tridimensional y hemos podido observar algunas características de las mismas. 
¿Será igual con los ácidos nucléicos? Rosalind Franklin es una científica muy relevante, que tuvo menos reconocimiento del merecido. 
Contanos sobre los procedimientos que puso Rosalind.

Los ácidos nucleicos también poseen una estructura tridimensional compleja y definida que es esencial para su función biológica. 
Aunque comúnmente asociamos al ADN con su clásica doble hélice, tanto el ADN como el ARN adoptan plegamientos espaciales específicos 
estabilizados por puentes de hidrógeno, interacciones de apilamiento de bases e interacciones electrostáticas con iones como el magnesio.

Para dilucidar esta estructura tridimensional en el ADN a principios de la década de 1950 en el King's College de Londres, 
Rosalind Franklin perfeccionó y aplicó procedimientos experimentales de cristalografía y difracción de rayos X de fibras.



-DESAFÍO I: Compará el sitio activo de ambos confórmeros (posición 837) así como también los tamaños de los pockets. ¿Qué observás?

*Confórmero activo (1M14): El sitio activo se encuentra abierto y accesible. Los bucles reguladores adoptan una conformación que 
permite la entrada y unión de sustratos e inhibidores, presentando una cavidad (pocket) de volumen óptimo para catálisis.

*Confórmero inactivo (3W32): El sitio activo se muestra colapsado hacia dentro. El volumen del pocket se reduce significativamente, 
impidiendo la acomodación efectiva de ligandos activos.

-DESAFÍO II: Investigá la proteína (AKR1C4) usando la base de datos Uniprot y anotá los sitios relevantes biológicamente.

Proteína: Aldo-keto reductase family 1 member C4 (enzima humana clave en el metabolismo de esteroides).

Sitios biológicamente relevantes:
*Sitio catalítico / Tríada o tétrada catalítica: Involucra residuos conservados como Tyr55, Lys84, His117 y Asp50 (según la subfamilia), 
esenciales para la transferencia de protones durante la reducción de grupos ceto en hormonas esteroideas.
*Sitio de unión al cofactor: Región de interacción con el dinucleótido de nicotinamida y adenina fosfato reducido (NADPH).
*Sitio de unión al sustrato esteroideo: Cavidad hidrofóbica que acomoda esteroides como progesterona y andrógenos.

-DESAFÍO III :Analizá la estructura PDB (2FVLB) ¿Cuántas cavidades fueron predichas para dicha estructura? 
¿Hay alguna cavidad drogable? ¿Coincide con algún sitio de relavancia biológica?

La entrada 2FVLB no incluye un conteo fijo de cavidades predichas en sus metadatos cristalográficos. 
El número exacto de cavidades o pockets varía según la herramienta empleada Y los parámetros geométricos/energéticos.

Presenta cavidades potencialmente drogables, en particular la región del sitio activo y el bolsillo de unión a sustrato, 
que ofrecen volumen y cerramiento adecuados para moléculas pequeñas. Coinciden con el sitio catalítico.


💡 Para investigar: Investigá en qué consiste el docking, en qué ideas basa su funcionamiento 
¿Cómo podría aprovecharse este método para tratar esta patología?

El docking molecular (o acoplamiento molecular) es una técnica de simulación computacional en biología estructural y 
diseño de fármacos que predice cómo se orienta y se une una molécula pequeña —habitualmente un ligando o fármaco candidato— 
dentro del sitio de unión de una macromolécula biológica, como una proteína o receptor.

A partir de estructuras tridimensionales obtenidas por cristalografía de rayos X, criomicroscopía electrónica, RMN o predicción estructural, el docking realiza dos tareas principales:
*Búsqueda conformacional y posicional (sampling): Genera múltiples orientaciones, traslaciones y conformaciones flexibles del ligando 
dentro de un bolsillo o cavidad definida de la proteína receptora.
*Evaluación energética (scoring): Estima la afinidad de unión de cada postura mediante una función de puntuación (scoring function) 
que aproxima la energía libre de unión, ordenando los complejos según su estabilidad termodinámica.

El trastorno bipolar es multifactorial, con alteraciones en señalización sináptica, neuroplasticidad, vías intracelulares 
y modulación de neurotransmisores. El docking molecular aporta varias líneas de trabajo:
*Optimización de selectividad en receptores monoaminérgicos: Muchos antipsicóticos y estabilizadores del ánimo interactúan con receptores 
dopaminérgicos (DRD2) y serotoninérgicos (HTR1A, HTR2A, HTR7). El docking permite comparar cómo distintos ligandos se acomodan en estos 
bolsillos para buscar perfiles más equilibrados entre episodios maníacos y depresivos y reducir efectos adversos no deseados.   
*Exploración de dianas intracelulares y sinápticas emergentes: Más allá de las monoaminas clásicas, la investigación evalúa proteínas 
implicadas en cascadas de señalización y liberación vesicular —como la proteína quinasa C (PKC), GSK-3, vías MAPK / PI3K-AKT o 
reguladores sinápticos recientes como DOC2A— para identificar moléculas moduladoras.   
*Cribado virtual y reposicionamiento de fármacos: Permite evaluar bibliotecas de compuestos o fármacos ya aprobados frente a dianas 
asociadas al trastorno bipolar, priorizando candidatos con propiedades fisicoquímicas y farmacocinéticas favorables 
(como permeabilidad de barrera hematoencefálica y perfil ADMET) para validación experimental posterior.   
*Análisis de mecanismos y efectos secundarios: Combinado con farmacología de redes y datos transcriptómicos/proteómicos, 
ayuda a hipotetizar qué interacciones moleculares explican respuestas clínicas heterogéneas o virajes afectivos inducidos por fármacos.


-DESAFÍO IV: Investigá en CaviDB la las características estructurales de la Albúmina Humana sobre la estructura 1AO6A:

¿Cuántas cavidades fueron predichas para dicha estructura? ¿Cuáles son las pricipales cavidades en tanto a tamaño de la proteína? 
¿Existen cavidades que se solapen con los residuos descritos como relavantes para la actividad enzimática de la albúmina?

*Cavidades predichas y tamaño: Se identifican numerosas cavidades distribuidas en sus tres dominios homólogos (I, II y III). 
Las principales en términos de volumen corresponden a los famosos Sitios de Sudlow I (en el subdominio IIA) y Sitio de Sudlow II 
(en el subdominio IIIA), principales responsables del transporte de fármacos y ligandos endógenos.
*Solapamiento con residuos catalíticos: Varias cavidades solapan directamente con residuos descritos como clave para las actividades 
secundarias y de unión, tales como Lys199, Arg410, Tyr411, Cys34 y Lys195.

¿Alguna de las cavidades catalíticamente activas se encuentran activadas? ¿Qué rangos de pKa se observan en dichas cavidades?

Ciertas cavidades muestran microambientes con aminoácidos que exhiben pKas anómalos (desplazados respecto a su valor en solución acuosa libre), 
favoreciendo estados ionizados en entornos mayoritariamente hidrofóbicos, lo que propicia su modesta capacidad catalítica.


-DESAFÍO V: Se sabe que en la albúmina bovina el sitio activo se encuentra corrido respecto del humano, aunque también 
involucra un aminoácido cargado (Lys 221). Investigá en CaviDB las características estructurales de la estructura de albúmina bovina 4JK4A 
y compará las características de su sitio activo con las características del sitio activo de la albúmina humana (Lys 199)

Aunque la arquitectura global de dominios se conserva fuertemente entre mamíferos (conservación evolutiva), el sitio activo principal 
sufre sutiles desplazamientos espaciales. Mientras que en la albúmina humana el residuo crítico en el sitio de unión/interacción 
es la Lys199, en la albúmina bovina (estructura 4JK4A) este rol equivalente se encuentra desplazado posicionalmente hacia la Lys221, 
lo que altera las afinidades relativas y la estereoselectividad frente a ciertos fármacos y ligandos exógenos.


💡 Para investigar: Leé más sobre los hallazgos hechos por l@s investigadores/as de la Universidad Nacional de Quilmes 
sobre la evolución de albúminas y contrastalo con lo que pusidte observar.

Mientras que en los Desafíos IV y V analizamos las cavidades de las albúminas humana (1AO6A) y bovina (4JK4A) desde su función transportadora, 
microambientes con posibles pKa anómalos y el desplazamiento posicional de residuos clave como Lys199 (humana) frente a Lys221 (bovina), 
los hallazgos de los investigadores de la UNQ amplían esta perspectiva al demostrar que una actividad catalítica promiscua 
—la condensación aldólica cruzada entre acetona y p-formilbenzonitrilo— se conserva en mamíferos, ocurre en una cavidad conectada a 
la superficie mediante un túnel también conservado y muestra señales de selección positiva junto con asociaciones a enfermedades humanas, 
lo que sugiere que estos rasgos podrían responder a una función biológica o adaptación evolutiva aún no del todo esclarecida 
más allá de su rol como transportadoras o de su uso biotecnológico.

-DESAFÍO VI: En el campo sequence query ingresá la sigueinte sequencia colab, usando num_relax = 1 y template_mode = pdb100:
sp|P03129|VE7_HPV16 Protein E7 OS=Human papillomavirus type 16 OX=333760 GN=E7 PE=1 SV=1 MHGDTPTLHEYMLDLQPETTDLYCYEQLNDSSEEEDEIDGPAGQAEPDRAHYNIVTFCCKCDSTLRLCVQSTHVDIRTLEDLLMGTLGIVCPICSQKP

¿Qué el campo template_mode? ¿Qué opciones pueden ser utilizadas?

template_mode es el parámetro que define si el algoritmo de AlphaFold2 buscará y utilizará estructuras experimentales conocidas 
depositadas en bases de datos (como el PDB) para guiar el modelado estructural. Opciones principales:
*pdb100: Busca alineamientos contra secuencias en el PDB para extraer plantillas estructurales de referencia cuando existe similitud evolutiva.
*none: Omite completamente el uso de plantillas externas, forzando al modelo a predecir la estructura exclusivamente mediante su red neuronal 
basada en la coevolución de los alineamientos múltiples de secuencias.

¿Qué regiones de la estructura resultante tienen una mayor confianza? Desarrollar un script que permita graficar los pLDDT por posición.

En la proteína E7 del HPV16 (VE7_HPV16, 98 residuos), la región con mayor confianza estructural (pLDDT más alto) 
es aproximadamente entre los residuos 50 y 98.

Scrip desarrollado en desafioVI.py



