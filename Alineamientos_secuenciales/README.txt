PARA PENSAR 🤔: Ingresá al servidor del NCBI y mirá los distintos programas derivados del BLAST que se ofrecen 
¿Para qué sirve cada uno? ¿En qué casos usarías cada uno?

Búsquedas principales 
Nucleotide query -> Nucleotide database (blastn): Compara una secuencia de nucleótidos (ADN o ARN) contra una base de datos de nucleótidos para encontrar similitudes.

Protein query -> Protein database (blastp): Compara una secuencia de aminoácidos (proteína) contra una base de datos de proteínas.

Translated Nucleotide query -> Protein database (blastx): Traduce una secuencia de nucleótidos de entrada y los compara contra una base de datos de proteínas.

Protein query -> Translated Nucleotide database (tblastn): Compara una secuencia de proteínas contra una base de datos de nucleótidos que es traducida automáticamente. 

Casos de uso: 
Usarías blastn o blastp cuando la secuencia consultada y la base de datos compartan la misma naturaleza (nucleótidos con nucleótidos, proteínas con proteínas).
Usarías blastx o tblastn cuando se necesita traducción de por medio.


DESAFIO VII: calculá el E-value y % identidad utilizando el programa Blast de la siguiente secuencia input usando 20000 hits, 
un e-value de 100 y tomando aquellos hits con un mínimo de 70% cobertura. 
Observe y discuta el comportamiento de : E-value vs. % id, Score vs % id, Score vs E-value

Hecho con 5000 hits (lo que permite la version web).

E-value vs. % Identidad: Presenta una relación exponencial inversa. 
A medida que aumenta el porcentaje de identidad, el E-value desciende hacia valores cercanos a cero. 
Las secuencias con alta identidad tienen menos probabilidad de encontrarse al azar.

Score vs. % Identidad: Muestra una correlación directamente proporcional. 
Un mayor porcentaje de identidad genera un puntaje (Score) más alto. 
Esto ocurre porque una mayor similitud genera más coincidencias positivas en la matriz de sustitución y menos penalizaciones por huecos (gaps).

Score vs. % E-value: También muestra una relación inversa exponencial. 
A mayor Score, menor es el E-value, es decir, si es menos probable haber obtenido resultados al azar, mayor es el puntaje.


DESAFIO VIII: Realizá nuevas búsquedas usando la mitad de la secuencia problema y para un cuarto de la secuencia original. 
Compará los gráficos obtenidos. ¿Qué conclusiones puede sacas?

Observaciones en los gráficos:
-Secuencia completa: se pueden encontrar puntajes de alineamiento mayores a 200
-Mitad de la secuencia: se pueden encontrar puntajes de alineamiento entre 80 y 200 como máximo
-Cuarto de secuencia: se pueden encontrar puntajes de alineamiento entre 50 y 80 como máximo

Conclusión: Miestras más larga es la cadena mayor es el score posible ya que representan secuencias más específicas,
a diferencia de cadenas más pequñas que tienen mas probabilidades de coincidir al azar (mayor e-value).

DESAFIO IX: Utilizando BLAST utilice búsquedas de similitud secuencial para identificar a la siguiente proteína:
MIDKSAFVHPTAIVEEGASIGANAHIGPFCIVGPHVEIGEGTVLKSHVVVNGHTKIGRDNEIYQFASIGEVNQDLKYAGEPTRVEIGDRNRIRESVTIHRGTVQGGGLTKVGSDNLLMINAHIAHDCTVGNRCILANNATLAGHVSVDDFAIIGGMTAVHQFCIIGAHVMVGGCSGVAQDVPPYVIAQGNHATPFGVNIEGLKRRGFSREAITAIRNAYKLIYRSGKTLDEVKPEIAELAETYPEVKAFTDFFARSTRGLIR

La proteina es: acyl-ACP--UDP-N-acetylglucosamine O-acyltransferase [Klebsiella spallanzanii] (también conocida frecuentemente como LpxA)

PARA PENSAR 🤔: ¿Cuál es la función de la proteína? ¿A qué grupo taxonómico pertenece? 
A un nivel de significancia estadística adecuado ¿cuántas secuencias similares se encuentran?

-Función: es una enzima fundamental en la biosíntesis del Lípido A, el cual constituye el anclaje hidrofóbico del lipopolisacárido (LPS) 
en la membrana externa de las bacterias gramnegativas.
-Grupo taxonómico: Pseudomonadota 
-A un nivel de significancia estadística adecuado, encontramos cientos de secuencias parientes repartidas en diferentes tipos y cepas de bacterias gramnegativas.

DESAFIO X: Realizá una nueva corrida del BLASTp, utilizando la misma secuencia , pero ahora contra la base de datos PDB. 
¿Se obtienen los mismos resultados? ¿Qué tipo de resultados(hits) se recuperan? ¿Cuándo nos podría ser útil este modo de corrida?

La base de datos PDB contiene modelos de estructuras tridimensionales de proteinas determinadas de forma experimental,
los resultados que se obtienen al hacer la búsqueda son muchos menos y corresponden a estructuras o modelos experimentales de la misma protína.
Nos es útil cuando necesitamos información estructural tridimensional de la proteína. 
Por ejemplo, si queremos realizar el modelado de la estructura 3D de nuestra proteína usando una plantilla con estructura ya resuelta.
