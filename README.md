*This project has been created as part of the 42 curriculum by hassamoh, lpoyanco.*

# A-Maze-ing

## Descripción

**A-Maze-ing** es un proyecto de generación de laberintos desarrollado como parte del currículo de 42.

El objetivo principal del proyecto es diseñar e implementar un generador de laberintos configurable capaz de crear laberintos válidos mediante algoritmos de generación y resolverlos automáticamente.

El programa genera laberintos en base a parámetros definidos en un archivo de configuración, permite visualizarlos y exportarlos a un archivo de salida.

Objetivos principales:

* Generar laberintos válidos de forma algorítmica
* Permitir configurar dimensiones y colores
* Mantener una arquitectura modular y reutilizable
* Implementar generación, resolución y exportación del laberinto

---

## Estructura del Proyecto

```bash
.
├── a_maze_ing.py
├── animation.py
├── config.py
├── config.txt
├── Makefile
├── mazegen
│   ├── constants.py
│   ├── __init__.py
│   ├── maze_generator.py
│   ├── patterns_42.py
│   ├── print_maze.py
│   └── style.py
├── maze.txt
└── pyproject.toml
```

---

## Features

* Generación de laberintos usando DFS con backtracking iterativo
* Resolución automática usando BFS
* Generación de laberintos perfectos (camino único)
* Generación de laberintos imperfectos (con loops)
* Configuración mediante archivo externo
* Personalización de colores
* Exportación del laberinto a archivo de texto
* Uso de semillas (`seed`) para resultados reproducibles
* Visualización y animación del proceso

---

## Instrucciones

### Requisitos

* Python 3.x
* Poetry
* pip

---

### Compilar

```bash
make build
```

Compila el proyecto usando Poetry.

---

### Instalar

```bash
make install
```

Instala:

* El paquete generado
* flake8
* mypy

---

### Ejecutar

```bash
make run
```

Equivalente a:

```bash
python3 a_maze_ing.py config.txt
```

---

### Debug

```bash
make debug
```

Ejecuta el proyecto usando el debugger de Python.

---

### Linting

```bash
make lint
```

Ejecuta:

* flake8
* mypy

Con comprobaciones estrictas de calidad y tipado.

---

### Clean

```bash
make clean
```

Elimina:

* `__pycache__`
* `.mypy_cache`
* directorios de build
* archivos `.pyc`

---

## Estructura del Archivo de Configuración

El proyecto utiliza un archivo de configuración llamado `config.txt`.

Ejemplo:

```txt
WIDTH=20
HEIGHT=15
ENTRY=0,0
EXIT=19,14
OUTPUT_FILE=maze.txt
PERFECT=True
SEED=42
BACKGROUND=BLACK
WALL=WHITE
PATH=GREEN
START=YELLOW
FINAL=RED
ICON=GREY
```

### Parámetros de Configuración

* **WIDTH** → Anchura del laberinto
* **HEIGHT** → Altura del laberinto
* **ENTRY** → Coordenadas de entrada `(x,y)`
* **EXIT** → Coordenadas de salida `(x,y)`
* **OUTPUT_FILE** → Archivo de salida
* **PERFECT** → Define si el laberinto será perfecto o imperfecto
* **SEED** → Semilla aleatoria para generación reproducible
* **BACKGROUND** → Color de fondo
* **WALL** → Color de paredes
* **PATH** → Color del camino solución
* **START** → Color de la entrada
* **FINAL** → Color de la salida
* **ICON** → Color del numero de 42

Este sistema permite modificar completamente el comportamiento del programa sin tocar el código fuente.

---

## Algoritmo de Generación del Laberinto

Este proyecto utiliza **Depth-First Search (DFS) con backtracking iterativo** para generar el laberinto.

### Funcionamiento

1. Se comienza en la celda inicial
2. Se marca como visitada
3. Se obtienen los vecinos no visitados
4. Se selecciona uno aleatoriamente
5. Se elimina la pared entre ambas celdas
6. Se avanza a la nueva celda
7. Si no hay vecinos disponibles, se hace backtracking usando un stack

El algoritmo termina cuando todas las celdas válidas han sido visitadas.

Este método garantiza que el laberinto sea completamente navegable.

---

## Algoritmo de Resolución del Laberinto

La resolución del laberinto se realiza usando **Breadth-First Search (BFS)**.

### Funcionamiento

1. Se empieza desde la entrada
2. Se exploran las celdas accesibles por niveles
3. Se almacena el nodo padre de cada celda visitada
4. Se detiene al encontrar la salida
5. Se reconstruye el camino desde la salida hasta la entrada

BFS garantiza encontrar el camino más corto en un laberinto no ponderado.

---

## ¿Por qué elegimos estos algoritmos?

### DFS para generación

Elegimos DFS porque:

* Es sencillo de implementar
* Tiene buen rendimiento
* Genera laberintos visualmente interesantes
* Funciona muy bien con animaciones

### BFS para resolución

Elegimos BFS porque:

* Garantiza el camino más corto
* Es fiable y fácil de depurar
* Facilita la reconstrucción de la solución

La combinación de ambos algoritmos nos permitió obtener un sistema eficiente, claro y fácil de mantener.

---

## Código Reutilizable

Varias partes del proyecto fueron diseñadas para ser reutilizables.

### `mazegen/maze_generator.py`

Contiene la lógica principal de:

* Generación
* Resolución
* Exportación

Puede reutilizarse para:

* Distintos tamaños de laberinto
* Nuevos algoritmos
* Futuras implementaciones de solvers

---

### `config.py`

Gestiona el parsing del archivo de configuración.

Puede reutilizarse en otros proyectos que necesiten configuración basada en archivos `.txt`.

---

### `animation.py`

Contiene lógica de animación reutilizable para:

* Visualización de procesos
* Renderizado paso a paso

---

### `mazegen/print_maze.py`

Encargado de la representación visual del laberinto.

Puede adaptarse fácilmente a otros formatos de salida.

---

## Gestión del Equipo y del Proyecto

### Miembros y Roles

#### hassamoh

* Lógica principal del generador
* Implementación de algoritmos
* Optimización y testing

#### lpoyanco

* Sistema de configuración
* Visualización y animación
* Debugging y testing

Ambos miembros colaboraron en:

* Arquitectura del proyecto
* Diseño de decisiones técnicas
* Documentación

---

## Planificación

### Planificación Inicial

El plan inicial fue:

1. Diseñar la arquitectura
2. Elegir algoritmos
3. Implementar generación
4. Añadir configuración
5. Añadir visualización
6. Testing y documentación

---

### Evolución Durante el Proyecto

Durante el desarrollo, la planificación cambió.

Principales cambios:

* El debugging llevó más tiempo del esperado
* La visualización fue más compleja de implementar
* La configuración necesitó más validaciones

Nos adaptamos:

* Repartiendo tareas claramente
* Revisando el progreso con frecuencia
* Refactorizando módulos cuando fue necesario

---

## Qué Funcionó Bien

* Buena distribución del trabajo
* Arquitectura modular clara
* Algoritmos eficientes
* Buen proceso de debugging

---

## Qué Podría Mejorarse

* Mejor estimación inicial de tiempos
* Más testing de integración desde el principio
* Documentación más temprana durante desarrollo

---

## Herramientas Utilizadas

Herramientas de desarrollo:

* Python
* Poetry
* Makefile
* flake8
* mypy
* Git / GitHub

Herramientas de gestión:

* Comunicación en equipo
* Reuniones de planificación

---

## Recursos

Referencias principales:

* Documentación oficial de Python
* Documentación de DFS y BFS
* Artículos sobre maze generation
* Subject oficial de 42

Recursos útiles:

* https://docs.python.org/3/
* https://en.wikipedia.org/wiki/Maze_generation_algorithm
* https://realpython.com/

---

## Uso de IA

Herramientas de IA fueron utilizadas como apoyo durante el desarrollo.

La IA se utilizó para:

* Ayuda en documentación
* Mejora de estructura del README
* Sugerencias de refactorización
* Asistencia en debugging
* Mejora de legibilidad del código

La IA no fue utilizada para generar completamente la lógica ni la arquitectura del proyecto.

Las decisiones finales de diseño e implementación fueron tomadas y validadas por el equipo.

---

## Futuras Mejoras

Posibles extensiones futuras:

* Soporte para múltiples algoritmos de generación
* Implementación de nuevos solvers
* Interfaz gráfica
* Más estilos de visualización
* Exportación a más formatos
* Modificar el Numero
