# distancia_imagenes
Ejercicios de simulación, detección de atípicos y detección de cercanías con imagenes.

Este Repositorio se parte en tres actividades:
1. Simulación de aleatorios para una distribución normal bivariada.
En este, se simulan 10000 aleatorios de una distribución Normal bivariante. Se calculan todas las distancias de cada dato a su media y se hace un plot, donde se
pinta de rojo los puntos cuya distancia a la media se encuentra en el 20 % de las mayores distancias.

2. Detección de atípicos
Con una BD que llamamos data38, se describa y ejecute un proceso de identificación de outliers en variables binarias.
Este se utiliza para identificar los meses que son considerados atípicos.
Binario siendo 1 si hay valor positivo.
Luego, se cálcula el número de condición de la matriz de covarianzas en su versión original.
Se implementan alternativas para mejorarlo y reducirlo a la cuarta parte. Esto se realiza con Análisis de los componentes principales PCA.

3. Coloco 4 imagénes de mi rostro y otras imágenes de personas aleatorias. Paso cada imagen a escala de grises. Para las cuatro normas
matriciales (1,2, ∞ y Frobenius). Calculo, con la métrica inducida por las normas, la distancia de cada persona a todas las personas.
Defino un indicador de lejanía del individuo j como el promedio de las distancias del individuo j a todos. Un concepto sencillo de imagen mediana fue 
aquel individuo cuyo indicador de lejanía es el menor. Obtengo con las cuatro métricas quién es la mediana, es decir, el más típico.
Con las cuatro métricas, determine quien del grupo es el más parecido a mi.
Luego, ensayo introduciendo en la base un par de fotos mías más.
Construyo una vecindad con centro en mi y un radio tal que la vecindad tenga 5 imágenes.
Muestro las imágenes. 
Finalmente, explico con buenos argumentos si mi imagen es punto interior, punto frontera o punto de acumulación del conjunto de imágenes del grupo.
