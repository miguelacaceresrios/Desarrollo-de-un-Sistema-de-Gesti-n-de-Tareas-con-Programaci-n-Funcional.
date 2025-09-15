
# 📝 Sistema de Gestión de Tareas (Programación Funcional)

Este proyecto implementa un sistema de gestión de tareas utilizando **programación funcional** en Python.  
Se busca demostrar el uso de **funciones puras, recursión, inmutabilidad y orden superior**, conceptos clave en este paradigma.

---

## 🚀 Características principales
- ✅ **Funciones puras**: cada operación retorna una nueva lista sin modificar la original.
- 🔁 **Recursión** en lugar de bucles iterativos.
- 🔎 **Filtros personalizados** según prioridad o estado de la tarea.
- 📊 **Ordenación funcional** de tareas mediante *merge sort*.
- 🛡️ **Inmutabilidad** garantizando que la lista original no cambia.
- 🧩 Código modular y extensible para nuevos criterios de filtrado u ordenación.

---

## 📂 Estructura del proyecto
proyecto_funcional/
│── tareas_funcionales.py # Código fuente principal
│── README.md # Documentación del proyecto

💻 Ejemplo de uso
Salida esperada al ejecutar el programa:

bash
Copiar código
=== SISTEMA DE GESTIÓN DE TAREAS (Programación Funcional) ===

Lista inicial de tareas:
ID: 1, Descripción: Estudiar para el examen, Prioridad: alta, Completada: False
ID: 2, Descripción: Hacer compras, Prioridad: media, Completada: False
ID: 3, Descripción: Llamar al médico, Prioridad: alta, Completada: True

Después de marcar tarea 2 como completada:
ID: 1, Descripción: Estudiar para el examen, Prioridad: alta, Completada: False
ID: 2, Descripción: Hacer compras, Prioridad: media, Completada: True
ID: 3, Descripción: Llamar al médico, Prioridad: alta, Completada: True

Tareas de alta prioridad:
ID: 1, Descripción: Estudiar para el examen, Prioridad: alta, Completada: False
ID: 3, Descripción: Llamar al médico, Prioridad: alta, Completada: True

🛠️ Funciones implementadas
Gestión de tareas
añadir_tarea(lista, tarea) → agrega una nueva tarea.

eliminar_tarea(lista, id) → elimina una tarea por su ID usando recursión.

actualizar_tarea(lista, id, nuevos_datos) → actualiza una tarea de forma inmutable.

mostrar_tareas(lista) → imprime todas las tareas de forma recursiva.

Filtrado y ordenación
filtrar_tareas(lista, criterio) → función de orden superior para filtrar.

Criterios incluidos:

es_alta_prioridad(tarea)

es_media_prioridad(tarea)

es_baja_prioridad(tarea)

esta_completada(tarea)

no_esta_completada(tarea)

ordenar_tareas(lista, clave) → ordena las tareas mediante merge sort.

📚 Fundamentos teóricos
Este proyecto se inspira en el paradigma de la programación funcional, cuyos principios son:

Funciones puras → no producen efectos secundarios.

Inmutabilidad → los datos no cambian, se generan nuevas estructuras.

Funciones de orden superior → reciben o devuelven funciones.

Recursión → reemplaza bucles tradicionales en el procesamiento de listas.

🤝 Contribución
Las contribuciones son bienvenidas.
Si deseas colaborar:

Haz un fork del repositorio.

Crea una rama nueva con tu mejora (git checkout -b mejora-nueva).

Haz commit de tus cambios (git commit -m "Agrego nuevo filtro").

Haz push a tu rama (git push origin mejora-nueva).

Abre un Pull Request 🚀.

