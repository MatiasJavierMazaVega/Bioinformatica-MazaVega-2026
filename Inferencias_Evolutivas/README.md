DESAFÍO I:
Para determinar si el "niño-mosca" conserva características humanas o de insecto a nivel molecular, se debe seguir la siguiente estrategia:

-Recopilación y curación de datos: Obtener las secuencias completas u ortólogas del gen Cyt P450 (o Citocromo C) de referencias claras de humano (Homo sapiens), de la mosca de la fruta (Drosophila melanogaster) y de la secuencia problema del bartmosca provista en el caso.

-Alineamiento múltiple de secuencias: Alinear las secuencias para identificar posiciones homólogas conservadas y variables.

-Construcción de árboles filogenéticos: Estimar las distancias evolutivas y posicionar al bartmosca dentro de un árbol para ver con qué clado agrupa de manera más robusta.

*Criterios:
-Porcentaje de identidad y similitud de aminoácidos (alineando la secuencia de la proteína Cyt P450).
-Presencia de motivos conservados característicos de la familia de proteínas Cyt P450 o dominios específicos de vertebrados frente a insectos.

*Resultados esperados del análisis: Al comparar la secuencia de bartmosca mediante una alineación o herramientas de búsqueda de homología (como BLAST), se observará claramente si la secuencia comparte un mayor porcentaje de identidad con los cordados/humanos o con los dípteros, revelando de forma empírica la "proporción" de herencia biológica de cada organismo.

Si se incorpora el conjunto completo de secuencias del archivo —que incluye organismos filogenéticamente muy distantes como plantas, un alga parda y una bacteria— junto con el humano y la mosca, el análisis deja de ser una simple comparación binaria y pasa a resolverse en un contexto evolutivo global.   
Al construir el árbol filogenético con esta diversidad ampliada, las secuencias se agruparán en grandes dominios y reinos biológicos bien diferenciados: por un lado las plantas y el alga, por otro la bacteria, y por último el grupo de los animales (Metazoa), donde convergen el humano y la mosca. La secuencia del bartmosca se ubicará dentro de la rama de los animales, agrupándose estrechamente con los cordados (humanos) o los artrópodos (moscas).
Incluir esta amplia variedad de organismos actúa como un control biológico fundamental, permite demostrar con rigor estadístico y gráfico que la secuencia del bartmosca comparte un ancestro común exclusivo con los animales y descartar cualquier relación absurda con reinos distantes (como plantas o bacterias).

Desafio II:

Archivos de alineamiento entre humano, mosca y bartmosca, y de estos 3 junto con el resto de las especies estan incluidos dentro de la carpeta.

Desafio III:

Aclaración: La página de IQtree esta fuera de servicio, en su lugar encontré https://paperbanana.me/tools/phylogenetic-tree-generator como alternativa, pero no presenta las mismas opciones, además, el archivo Newick que descargue no necesitó que cambiara nada para poder visualizarlo en Figtree. De todas formas busqué como se supondría que debería funcionar IQtree y contesté la consigna en base a lo encontrado.

Cuando el servidor de IQ-TREE pide elegir o calcular un modelo de sustitución, se refiere al modelo matemático probabilístico que describe cómo un aminoácido (o nucleótido) muta o es sustituido por otro a lo largo del tiempo evolutivo (por ejemplo, modelos como WAG, JTT o Dayhoff para proteínas). Estos modelos ponderan la probabilidad de cambios bioquímicamente conservativos frente a cambios radicales.Cuando el servidor de IQ-TREE pide elegir o calcular un modelo de sustitución, se refiere al modelo matemático probabilístico que describe cómo un aminoácido (o nucleótido) muta o es sustituido por otro a lo largo del tiempo evolutivo (por ejemplo, modelos como WAG, JTT o Dayhoff para proteínas). Estos modelos ponderan la probabilidad de cambios bioquímicamente conservativos frente a cambios radicales.

Bootstrap: Es una técnica estadística de remuestreo (que suele realizarse en cientos o miles de réplicas, ej. 1000 iteraciones). Consiste en crear pseudo-alineamientos alterando las columnas al azar para evaluar qué tan robustas son las agrupaciones del árbol.

Calidad: Los valores de Bootstrap se expresan generalmente en porcentajes (de 0 a 100) en los nodos internos del árbol. Un valor alto (por ejemplo, mayor a 90 o 95) indica que esa rama y su clado aparecen de forma sostenida en casi todas las réplicas, lo que otorga alta confiabilidad estadística a esa relación evolutiva.

Antes de visualizar e interpretar el árbol en FigTree, por lo general es necesario enraizar el árbol (rooting) utilizando una secuencia externa o grupo externo (outgroup) adecuado que permita establecer una dirección temporal clara desde el ancestro común universal hacia las hojas del árbol.

-Los archivos .nwk de ambos árboles están incluídos en la carpeta, junto con imágenes en formato png 