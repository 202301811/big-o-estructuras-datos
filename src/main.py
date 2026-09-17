import csv
import io
import random
import time
import urllib.request
from statistics import mean

from arbol_bst import ArbolBST
from lista_enlazada import ListaEnlazada

# === 1. TU URL RAW ===
URL = "https://raw.githubusercontent.com/202301811/big-o-estructuras-datos/main/data/estudiantes.csv"
REPETICIONES = 50


def descargar_datos(url):
    print("-> Descargando CSV desde GitHub RAW...")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as respuesta:
        contenido = respuesta.read().decode("utf-8")
    return list(csv.DictReader(io.StringIO(contenido)))


def buscar_lista(estudiantes, carnet):
    for estudiante in estudiantes:
        if estudiante["carnet"] == carnet:
            return estudiante
    return None


def medir(funcion, repeticiones=REPETICIONES):
    muestras = []
    for _ in range(repeticiones):
        inicio = time.perf_counter()
        funcion()
        muestras.append(time.perf_counter() - inicio)
    return mean(muestras)


def main():
    estudiantes = descargar_datos(URL)
    print(f"OK: {len(estudiantes):,} registros recibidos exitosamente.\n")


    print("=" * 65)
    print(f"{'n':>8} | {'List O(n) (s)':>16} | {'Set O(1) (s)':>16} | {'Dict O(1) (s)':>16}")
    print("-" * 65)

    tamanos = [100, 1_000, 10_000, 50_000, 100_000]
    
    for n in tamanos:
        muestra = estudiantes[:n]
        carnets_set = {e["carnet"] for e in muestra}
        dict_estudiantes = {e["carnet"]: e for e in muestra}
        
        # Peor caso: buscar el último elemento
        carnet_objetivo = muestra[-1]["carnet"]

        t_list = medir(lambda: buscar_lista(muestra, carnet_objetivo))
        t_set = medir(lambda: carnet_objetivo in carnets_set)
        t_dict = medir(lambda: dict_estudiantes.get(carnet_objetivo))

        print(f"{n:>8,d} | {t_list:>16.8f} | {t_set:>16.8f} | {t_dict:>16.8f}")

    print("=" * 65)


    print("\n--- PRUEBA LISTA ENLAZADA (n = 10,000) ---")
    lista_enlazada = ListaEnlazada()
    muestra_10k = estudiantes[:10_000]
    
    # Inserción al inicio O(1)
    for est in muestra_10k:
        lista_enlazada.insertar_inicio(est)

    # Búsqueda O(n): buscar el primero insertado (ahora está al final)
    carnet_buscar_le = muestra_10k[0]["carnet"]
    t_lista_enl = medir(lambda: lista_enlazada.buscar(carnet_buscar_le), repeticiones=20)
    print(f"Tiempo de búsqueda en Lista Enlazada (peor caso): {t_lista_enl:.8f} s -> O(n)")


    print("\n--- PRUEBA ÁRBOL BINARIO DE BÚSQUEDA (n = 5,000) ---")
    muestra_bst = estudiantes[:5_000].copy()
    random.shuffle(muestra_bst)  # Para evitar degradación a lista
    
    arbol = ArbolBST()
    for est in muestra_bst:
        arbol.insertar(est)

    carnet_buscar_bst = muestra_bst[-1]["carnet"]
    t_bst = medir(lambda: arbol.buscar(carnet_buscar_bst), repeticiones=50)
    print(f"Tiempo de búsqueda en BST (balanceado por shuffle): {t_bst:.8f} s -> O(log n)")

    print("\n--- RETO: BÚSQUEDA DE CARNET INEXISTENTE ('EST999999') ---")
    carnet_fantasma = "EST999999"
    muestra_completa = estudiantes
    set_completo = {e["carnet"] for e in muestra_completa}
    dict_completo = {e["carnet"]: e for e in muestra_completa}

    t_list_fallida = medir(lambda: buscar_lista(muestra_completa, carnet_fantasma), repeticiones=10)
    t_set_fallida = medir(lambda: carnet_fantasma in set_completo)
    t_dict_fallida = medir(lambda: dict_completo.get(carnet_fantasma))

    print(f"List (recorre todo n) : {t_list_fallida:.8f} s")
    print(f"Set  (función hash)   : {t_set_fallida:.8f} s")
    print(f"Dict (función hash)   : {t_dict_fallida:.8f} s")


if __name__ == "__main__":
    main()