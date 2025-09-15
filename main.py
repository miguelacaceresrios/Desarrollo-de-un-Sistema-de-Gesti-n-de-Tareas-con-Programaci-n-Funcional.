"""
Actividad de Programación Funcional
Integrantes del grupo:
1. [Nombre del integrante 1]
2. [Nombre del integrante 2]
3. [Nombre del integrante 3]

Referencias bibliográficas:
- Cousineau, G., & Mauny, M. (1998). The functional approach to programming. Cambridge University Press.
- Haskell.org. (2023). Learn Haskell. https://www.haskell.org/
- Python Software Foundation. (2023). Functional Programming HOWTO. https://docs.python.org/3/howto/functional.html
"""

# =============================================
# TAREA 1: IMPLEMENTAR UNA LISTA DE TAREAS
# =============================================

def crear_lista_tareas():
    """Crea una nueva lista vacía de tareas."""
    return []

def añadir_tarea(lista_tareas, tarea):
    """
    Función pura para añadir una tarea a la lista.
    
    Args:
        lista_tareas (list): Lista actual de tareas
        tarea (dict): Tarea a añadir con estructura {'id', 'descripcion', 'prioridad', 'fecha_creacion', 'completada'}
    
    Returns:
        list: Nueva lista con la tarea añadida
    """
    return lista_tareas + [tarea]

def eliminar_tarea(lista_tareas, id_tarea):
    """
    Función pura para eliminar una tarea por ID usando recursión.
    
    Args:
        lista_tareas (list): Lista actual de tareas
        id_tarea (int): ID de la tarea a eliminar
    
    Returns:
        list: Nueva lista sin la tarea especificada
    """
    def _eliminar_recursivo(tareas_restantes, tareas_acumuladas):
        if not tareas_restantes:
            return tareas_acumuladas
        elif tareas_restantes[0]['id'] == id_tarea:
            return _eliminar_recursivo(tareas_restantes[1:], tareas_acumuladas)
        else:
            return _eliminar_recursivo(tareas_restantes[1:], tareas_acumuladas + [tareas_restantes[0]])
    
    return _eliminar_recursivo(lista_tareas, [])

def actualizar_tarea(lista_tareas, id_tarea, nuevos_datos):
    """
    Función pura para actualizar una tarea usando recursión.
    
    Args:
        lista_tareas (list): Lista actual de tareas
        id_tarea (int): ID de la tarea a actualizar
        nuevos_datos (dict): Datos a actualizar
    
    Returns:
        list: Nueva lista con la tarea actualizada
    """
    def _actualizar_recursivo(tareas_restantes, tareas_acumuladas):
        if not tareas_restantes:
            return tareas_acumuladas
        elif tareas_restantes[0]['id'] == id_tarea:
            tarea_actualizada = {**tareas_restantes[0], **nuevos_datos}
            return _actualizar_recursivo(tareas_restantes[1:], tareas_acumuladas + [tarea_actualizada])
        else:
            return _actualizar_recursivo(tareas_restantes[1:], tareas_acumuladas + [tareas_restantes[0]])
    
    return _actualizar_recursivo(lista_tareas, [])

def mostrar_tareas(lista_tareas, indice=0):
    """
    Función recursiva para mostrar todas las tareas.
    
    Args:
        lista_tareas (list): Lista de tareas a mostrar
        indice (int): Índice actual para la recursión
    """
    if indice < len(lista_tareas):
        tarea = lista_tareas[indice]
        print(f"ID: {tarea['id']}, Descripción: {tarea['descripcion']}, "
              f"Prioridad: {tarea['prioridad']}, Completada: {tarea['completada']}")
        mostrar_tareas(lista_tareas, indice + 1)

# =============================================
# TAREA 2: FILTRADO Y ORDENACIÓN DE TAREAS
# =============================================

def filtrar_tareas(lista_tareas, criterio):
    """
    Función de orden superior para filtrar tareas según un criterio.
    
    Args:
        lista_tareas (list): Lista de tareas a filtrar
        criterio (function): Función que retorna True/False para cada tarea
    
    Returns:
        list: Lista filtrada de tareas
    """
    def _filtrar_recursivo(tareas_restantes, tareas_filtradas):
        if not tareas_restantes:
            return tareas_filtradas
        elif criterio(tareas_restantes[0]):
            return _filtrar_recursivo(tareas_restantes[1:], tareas_filtradas + [tareas_restantes[0]])
        else:
            return _filtrar_recursivo(tareas_restantes[1:], tareas_filtradas)
    
    return _filtrar_recursivo(lista_tareas, [])

# Funciones de criterio para filtrar
def es_alta_prioridad(tarea):
    return tarea['prioridad'] == 'alta'

def es_media_prioridad(tarea):
    return tarea['prioridad'] == 'media'

def es_baja_prioridad(tarea):
    return tarea['prioridad'] == 'baja'

def esta_completada(tarea):
    return tarea['completada']

def no_esta_completada(tarea):
    return not tarea['completada']

def ordenar_tareas(lista_tareas, clave):
    """
    Función para ordenar tareas usando recursión (implementación de merge sort).
    
    Args:
        lista_tareas (list): Lista de tareas a ordenar
        clave (str): Clave por la cual ordenar ('prioridad', 'fecha_creacion', etc.)
    
    Returns:
        list: Lista ordenada de tareas
    """
    if len(lista_tareas) <= 1:
        return lista_tareas
    
    # Dividir la lista en dos mitades
    medio = len(lista_tareas) // 2
    izquierda = ordenar_tareas(lista_tareas[:medio], clave)
    derecha = ordenar_tareas(lista_tareas[medio:], clave)
    
    # Combinar las mitades ordenadas
    return _combinar_ordenadas(izquierda, derecha, clave)

def _combinar_ordenadas(izquierda, derecha, clave):
    """Función auxiliar para combinar listas ordenadas."""
    if not izquierda:
        return derecha
    if not derecha:
        return izquierda
    
    # Definir orden de prioridades
    orden_prioridades = {'alta': 0, 'media': 1, 'baja': 2}
    
    if clave == 'prioridad':
        if orden_prioridades[izquierda[0][clave]] <= orden_prioridades[derecha[0][clave]]:
            return [izquierda[0]] + _combinar_ordenadas(izquierda[1:], derecha, clave)
        else:
            return [derecha[0]] + _combinar_ordenadas(izquierda, derecha[1:], clave)
    else:
        if izquierda[0][clave] <= derecha[0][clave]:
            return [izquierda[0]] + _combinar_ordenadas(izquierda[1:], derecha, clave)
        else:
            return [derecha[0]] + _combinar_ordenadas(izquierda, derecha[1:], clave)

# =============================================
# EJEMPLO DE USO Y PRUEBAS
# =============================================

if __name__ == "__main__":
    print("=== SISTEMA DE GESTIÓN DE TAREAS (Programación Funcional) ===\n")
    
    # Crear lista inicial de tareas
    tareas = crear_lista_tareas()
    
    # Añadir algunas tareas de ejemplo
    tarea1 = {
        'id': 1,
        'descripcion': 'Estudiar para el examen',
        'prioridad': 'alta',
        'fecha_creacion': '2023-10-01',
        'completada': False
    }
    
    tarea2 = {
        'id': 2,
        'descripcion': 'Hacer compras',
        'prioridad': 'media',
        'fecha_creacion': '2023-10-02',
        'completada': False
    }
    
    tarea3 = {
        'id': 3,
        'descripcion': 'Llamar al médico',
        'prioridad': 'alta',
        'fecha_creacion': '2023-10-01',
        'completada': True
    }
    
    # Añadir tareas usando funciones puras
    tareas = añadir_tarea(tareas, tarea1)
    tareas = añadir_tarea(tareas, tarea2)
    tareas = añadir_tarea(tareas, tarea3)
    
    print("Lista inicial de tareas:")
    mostrar_tareas(tareas)
    print()
    
    # Actualizar una tarea
    tareas = actualizar_tarea(tareas, 2, {'completada': True})
    print("Después de marcar tarea 2 como completada:")
    mostrar_tareas(tareas)
    print()
    
    # Filtrar tareas por prioridad alta
    tareas_altas = filtrar_tareas(tareas, es_alta_prioridad)
    print("Tareas de alta prioridad:")
    mostrar_tareas(tareas_altas)
    print()
    
    # Filtrar tareas no completadas
    tareas_pendientes = filtrar_tareas(tareas, no_esta_completada)
    print("Tareas pendientes:")
    mostrar_tareas(tareas_pendientes)
    print()
    
    # Ordenar tareas por prioridad
    tareas_ordenadas = ordenar_tareas(tareas, 'prioridad')
    print("Tareas ordenadas por prioridad:")
    mostrar_tareas(tareas_ordenadas)
    print()
    
    # Eliminar una tarea
    tareas = eliminar_tarea(tareas, 1)
    print("Después de eliminar la tarea 1:")
    mostrar_tareas(tareas)
    print()
    
    # Demostrar inmutabilidad: la lista original no se modifica
    print("Demostración de inmutabilidad:")
    lista_original = [tarea1, tarea2, tarea3]
    lista_modificada = añadir_tarea(lista_original, {
        'id': 4,
        'descripcion': 'Nueva tarea',
        'prioridad': 'baja',
        'fecha_creacion': '2023-10-03',
        'completada': False
    })
    
    print(f"Lista original tiene {len(lista_original)} elementos")
    print(f"Lista modificada tiene {len(lista_modificada)} elementos")
    print("La lista original permanece intacta (inmutabilidad)")



# programar en python en una clase de programacion funcional cuando queria tocar haskell 🥀
