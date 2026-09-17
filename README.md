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
   Porque en el peor caso se debe iterar sobre cada uno de los $n$ elementos. El número de operaciones escala en proporción 1:1 con respecto al tamaño de la entrada.

2. **¿Por qué Set y Dictionary tienen búsqueda O(1) en promedio?**  
   Porque utilizan direccionamiento hash, donde la clave determina directamente la posición del registro en memoria en una sola operación sin requerir barridos lineales.

3. **¿Por qué O(1) no significa "cero tiempo" ni "exactamente el mismo tiempo siempre"?**  
   $O(1)$ significa orden constante, no ausencia de tiempo. Ejecutar las instrucciones de la CPU, calcular el hash y atender interrupciones del procesador siempre consume microsegundos, los cuales pueden fluctuar ligeramente (ej. entre `0.00000015 s` y `0.00000018 s`).

4. **¿Cuál es la diferencia entre medir segundos y analizar Big O?**  
   Medir segundos evalúa el rendimiento práctico de una ejecución en una computadora particular. Big O modela formalmente cómo escala la complejidad algorítmica al crecer $n$.

5. **¿Por qué una lista enlazada puede insertar al inicio en O(1) pero buscar en O(n)?**  
   Insertar al inicio solo requiere enlazar el nuevo nodo a la cabeza actual y actualizar el puntero (operación atómica e invariable). Buscar requiere saltar de nodo en nodo mediante punteros hasta el final ($O(n)$), lo cual en nuestra prueba tomó `0.00081263 s`.

6. **¿Qué condición permite que un árbol de búsqueda se acerque a O(log n)?**  
   Que el árbol se mantenga balanceado en sus dos ramas. De esta forma, cada comparación izquierda/derecha descarta la mitad de los elementos restantes.

7. **¿Qué ocurre con el BST si se inserta información ya ordenada?**  
   Se degenera en una estructura equivalente a una lista enlazada unilineal, aumentando la altura a $n$ y degradando la búsqueda a $O(n)$. Por ello en nuestra prueba se aplicó `random.shuffle()` para preservarlo balanceado (`0.00000261 s`).

8. **¿Qué estructura elegiría para recuperar un estudiante completo por carnet? Justifique.**  
   Un **Diccionario**, ya que maneja la relación clave-valor requerida para devolver el objeto del estudiante en $O(1)$.

9. **¿Qué estructura elegiría si solamente necesita saber si un carnet existe? Justifique.**  
   Un **Set**, ya que solo almacena las claves optimizando el uso de memoria RAM y comprobando existencia en $O(1)$.

10. **Si el sistema realiza 70% búsquedas, 20% inserciones y 10% reportes, ¿qué decisión de diseño tomaría y por qué?**  
    Utilizaría un **Diccionario** como almacenamiento principal para garantizar que el 90% de las operaciones críticas (búsquedas e inserciones) se ejecuten en $O(1)$. Para el 10% restante de reportes, generaría vistas o listas ordenadas bajo demanda.

---

## Conclusión

El experimento demostró empíricamente la superioridad de las estructuras basadas en tablas hash frente al recorrido lineal cuando se trabaja a gran escala. Mientras que la búsqueda en List aumentó drásticamente de 0.00000413 s a 0.00609619 s al alcanzar los 100,000 registros, Set y Dict conservaron una latencia fija de 0.00000016 s, confirmando la validez del modelo O(1). Por su parte, la lista enlazada confirmó su naturaleza O(n) al requerir 0.00081263 s en el peor caso, y el árbol BST balanceado demostró su eficiencia O(log n) registrando apenas 0.00000261 s. En conclusión, para el sistema universitario planteado, la implementación con Diccionario resulta la solución óptima, garantizando un rendimiento constante que no colapsará ante el crecimiento futuro de la población estudiantil.
