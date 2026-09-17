# Resultados del laboratorio - Análisis Big O

## Integrantes
- Nombre: Rene Rafael Palacios
Joe Jafet Hernandez
Juan Rene Arevalo
- Carnet: 202301811
202301858
202300957
  
## URL RAW utilizada
`https://raw.githubusercontent.com/202301811/big-o-estructuras-datos/main/data/estudiantes.csv`

## Mediciones

| n | List O(n) | Set O(1) promedio | Dict O(1) promedio |
|---:|---:|---:|---:|
| 100 | 0.00000413 s | 0.00000016 s | 0.00000017 s |
| 1,000 | 0.00003870 s | 0.00000016 s | 0.00000016 s |
| 10,000 | 0.00044595 s | 0.00000015 s | 0.00000018 s |
| 50,000 | 0.00266386 s | 0.00000016 s | 0.00000017 s |
| 100,000 | 0.00609619 s | 0.00000016 s | 0.00000017 s |

### Mediciones complementarias obtenidas:
- **Lista Enlazada (n = 10,000 - peor caso):** `0.00081263 s` -> $O(n)$
- **Árbol BST balanceado (n = 5,000):** `0.00000261 s` -> $O(\log n)$
- **Búsqueda de carnet inexistente ('EST999999' en n = 100,000):**
  - **List:** `0.00548227 s` (recorre los 100,000 registros completos antes de fallar)
  - **Set:** `0.00000015 s` (resolución directa mediante tabla hash)
  - **Dict:** `0.00000018 s` (resolución directa mediante tabla hash)

---

## Preguntas de la plantilla

### 1. ¿Por qué List crece aproximadamente de forma lineal?
Porque la búsqueda en una lista tradicional se realiza de manera secuencial (elemento por elemento). Al colocar el elemento objetivo al final de la muestra, el algoritmo se ve obligado a realizar $n$ comparaciones. En nuestras mediciones reales se observa claramente: al pasar de $n = 1,000$ (`0.00003870 s`) a $n = 10,000$ (`0.00044595 s`), el tamaño se multiplicó por 10 y el tiempo también aumentó aproximadamente 11 veces, cumpliendo el modelo matemático $O(n)$.

### 2. ¿Por qué Set y Dict se comportan de forma distinta?
Tanto Set como Dict están fundamentados internamente en Tablas Hash. En lugar de iterar secuencialmente, aplican una función matemática sobre la clave (el carnet) que calcula de forma inmediata la dirección exacta en memoria. En nuestras pruebas empíricas, tanto con 100 registros como con 100,000 registros, el tiempo se mantuvo invariablemente en torno a `0.00000016 s`, demostrando que no dependen del volumen de datos ($O(1)$ en promedio).

### 3. ¿Medir tiempo es lo mismo que demostrar Big O? Explique.
No. Medir tiempo con `time.perf_counter()` obtiene valores físicos en segundos, los cuales dependen directamente del hardware, el sistema operativo, la carga del procesador y las optimizaciones del intérprete de Python. Big O, en cambio, es una abstracción matemática que clasifica la tasa de crecimiento del trabajo computacional en el límite asintótico ($n \to \infty$), independientemente de la máquina en que se ejecute.

### 4. ¿Qué estructura elegiría para búsquedas por carnet y por qué?
Elegiría un **Diccionario (Dict)**. Dado que el caso de estudio requiere no solo verificar si el estudiante existe sino también "recuperar todos sus datos", el diccionario permite indexar el carnet como clave única y asociar el registro completo como valor. Esto garantiza recuperar la información completa en tiempo constante $O(1)$ sin importar si la universidad tiene 1,000 o 5,000,000 de alumnos.

### 5. ¿Qué cambia cuando el carnet buscado no existe?
En **List** y **Lista Enlazada**, una búsqueda fallida representa forzosamente el peor escenario posible ($O(n)$), ya que el algoritmo tiene que recorrer y comparar absolutamente todos los elementos (`0.00548227 s` en nuestra prueba) antes de concluir que no está. Por el contrario, en **Set** y **Dict**, la búsqueda fallida sigue tomando tiempo constante $O(1)$ (`0.00000015 s`), ya que la función hash consulta directamente la casilla correspondiente y confirma de inmediato que la clave no existe.

---

## 10 Preguntas Obligatorias de Análisis (Guía de Laboratorio)

1. **¿Por qué una búsqueda secuencial sobre List se clasifica como O(n)?**  
   Básicamente porque, en el peor de los casos, a Python le toca revisar uno por uno todos los elementos hasta llegar al final. Si la lista crece, el tiempo de búsqueda va a crecer exactamente en esa misma proporción (es decir, escala 1:1 con el tamaño de los datos).

2. **¿Por qué Set y Dictionary tienen búsqueda O(1) en promedio?**  
   Porque por debajo hacen "trampa" usando Tablas Hash. En lugar de ir buscando registro por registro, toman la llave (en nuestro caso, el carnet), le aplican una fórmula matemática y saltan directamente a la posición exacta en memoria. Todo en un solo movimiento.

3. **¿Por qué O(1) no significa "cero tiempo" ni "exactamente el mismo tiempo siempre"?**  
   Porque O(1) significa que el esfuerzo se mantiene "constante", pero hacer las cosas igual toma tiempo físico. La computadora siempre gasta sus microsegundos en hacer el cálculo de la llave o manejar procesos de fondo; por eso en nuestras pruebas veíamos pequeñas fluctuaciones (variaba entre 0.00000015 s y 0.00000018 s), pero la gran diferencia es que el tiempo nunca se disparaba.

4. **¿Cuál es la diferencia entre medir segundos y analizar Big O?**  
   Medir en segundos es súper relativo; depende de qué tan buena sea nuestra computadora, el sistema operativo o qué más estemos corriendo en ese momento. En cambio, analizar el Big O es usar matemáticas puras para saber cómo se va a comportar y escalar nuestro algoritmo si de repente le metemos millones de datos, sin importar la máquina.

5. **¿Por qué una lista enlazada puede insertar al inicio en O(1) pero buscar en O(n)?**  
   Meter un dato al inicio es O(1) porque es un movimiento súper directo: solo creamos el nuevo eslabón, lo enganchamos a la cabeza de la lista y actualizamos el puntero (no movemos nada más). Para buscar es otra historia, no tenemos índices, así que nos toca ir saltando de nodo en nodo hasta el final, lo que se vuelve un recorrido O(n). En nuestra prueba eso nos tomó `0.00081263 s`.

6. **¿Qué condición permite que un árbol de búsqueda se acerque a O(log n)?**  
   Que el árbol esté bien balanceado. Si las ramas están parejitas, cada vez que bajamos a la izquierda o a la derecha estamos descartando automáticamente la mitad de todos los datos que quedaban, haciendo que la búsqueda sea rapidísima.

7. **¿Qué ocurre con el BST si se inserta información ya ordenada?**  
   Es el peor escenario. Si metemos los datos ya ordenados, el árbol crece solamente hacia un lado y se termina convirtiendo prácticamente en una lista enlazada normal, arruinando la búsqueda y volviéndola O(n). Por eso en nuestro código usamos random.shuffle() para desordenar todo primero, así garantizamos que quedara balanceado y logramos un tiempo de `0.00000261 s`.

8. **¿Qué estructura elegiría para recuperar un estudiante completo por carnet? Justifique.**  
   UDe lejos elegiríamos un Diccionario. Como nos piden recuperar todos los datos del estudiante, el diccionario nos permite usar el carnet como "llave" y guardar todo el objeto como "valor". Nos devuelve el registro completo al instante en $O(1)$.

9. **¿Qué estructura elegiría si solamente necesita saber si un carnet existe? Justifique.**  
   Para este caso nos iríamos con un Set (Conjunto). Si solo queremos un "sí o no" (saber si existe), el Set nos da la misma velocidad instantánea $O(1)$ que el diccionario, pero ahorrándonos muchísima memoria RAM, porque no guarda los datos completos del estudiante, solo las claves.

10. **Si el sistema realiza 70% búsquedas, 20% inserciones y 10% reportes, ¿qué decisión de diseño tomaría y por qué?**  
    Nos quedaríamos con un Diccionario como estructura base. Si el 90% del trabajo crítico del día a día son búsquedas e inserciones, el diccionario nos garantiza que todo eso fluirá rapidísimo en O(1). Para el 10% de los reportes (que seguro requieren ordenar la info de alguna manera), simplemente generaríamos vistas o listas temporales a partir de ese diccionario solo en el momento que se necesiten.

---

## Conclusión

El experimento demostró empíricamente la superioridad de las estructuras basadas en tablas hash frente al recorrido lineal cuando se trabaja a gran escala. Mientras que la búsqueda en List aumentó drásticamente de 0.00000413 s a 0.00609619 s al alcanzar los 100,000 registros, Set y Dict conservaron una latencia fija de 0.00000016 s, confirmando la validez del modelo O(1). Por su parte, la lista enlazada confirmó su naturaleza O(n) al requerir 0.00081263 s en el peor caso, y el árbol BST balanceado demostró su eficiencia O(log n) registrando apenas 0.00000261 s. En conclusión, para el sistema universitario planteado, la implementación con Diccionario resulta la solución óptima, garantizando un rendimiento constante que no colapsará ante el crecimiento futuro de la población estudiantil.
