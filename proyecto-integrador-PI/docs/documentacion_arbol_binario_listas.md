# Documentación: Árbol Binario con Listas

## Introducción

Este archivo implementa un Árbol Binario utilizando listas en Python. Permite realizar operaciones como inserción, eliminación, búsqueda y recorridos (inorden, preorden y postorden). Además, incluye una función para visualizar el árbol rotado 90°.

## Paso a Paso del Código

### 1. Crear un Árbol

La función `crear_arbol(valor)` crea un árbol binario con un valor inicial. El árbol se representa como una lista con tres elementos:

- El valor de la raíz.
- La sublista izquierda (subárbol izquierdo).
- La sublista derecha (subárbol derecho).

```python
arbol = crear_arbol("Lucía")
```

### 2. Insertar Valores

La función `insertar(arbol, valor)` inserta un valor en el árbol binario siguiendo el orden alfabético. Si el valor es menor que la raíz, se inserta en el subárbol izquierdo; si es mayor, en el subárbol derecho.

```python
insertar(arbol, "Carlos")
insertar(arbol, "Ana")
```

### 3. Recorridos

El código incluye tres tipos de recorridos:

- **Inorden**: izquierda - raíz - derecha.
- **Preorden**: raíz - izquierda - derecha.
- **Postorden**: izquierda - derecha - raíz.

Ejemplo:

```python
inorden(arbol)
preorden(arbol)
postorden(arbol)
```

### 4. Visualización del Árbol

La función `imprimir_arbol(arbol, nivel=0)` muestra el árbol rotado 90°, con la raíz en la parte izquierda y los niveles del árbol representados por la indentación.

```python
imprimir_arbol(arbol)
```

### 5. Buscar un Valor

La función `buscar(arbol, valor)` verifica si un valor está presente en el árbol.

```python
existe = buscar(arbol, "Carlos")
print(existe)  # True o False
```

### 6. Eliminar un Valor

La función `eliminar(arbol, valor)` elimina un valor del árbol. Si el nodo tiene hijos, se reemplaza por el valor mínimo del subárbol derecho.

```python
eliminar(arbol, "Lucía")
```

## Cómo Probar el Código

### 1. Ejecutar el Archivo

Ejecuta el archivo `arbol_binario_listas.py` en Python para ver los resultados de las operaciones implementadas.

```bash
python src/arbol_binario_listas.py
```

### 2. Salida Esperada

El código incluye ejemplos de uso con una lista de nombres. Al ejecutarlo, deberías ver:

- El árbol rotado 90°.
- Los recorridos inorden, preorden y postorden.
- Resultados de búsqueda.
- El árbol antes y después de eliminar un valor.

### 3. Modificar los Datos

Puedes modificar la lista `nombres` para probar con otros valores:

```python
nombres = ["Juan", "María", "Luis", "Elena"]
```

### 4. Agregar Pruebas

Para pruebas más detalladas, utiliza el archivo `tests/test_arbol.py` en la carpeta `tests/`.

```bash
pytest tests/test_arbol.py
```



Funciones principales
crear_arbol(valor)
Crea un árbol binario con un valor inicial. El árbol se representa como una lista con tres elementos:

El valor de la raíz.
El subárbol izquierdo (otra lista).
El subárbol derecho (otra lista).
insertar(arbol, valor)
Inserta un valor en el árbol binario siguiendo el orden alfabético:

Si el valor es menor que la raíz, se inserta en el subárbol izquierdo.
Si es mayor, se inserta en el subárbol derecho.
Recorridos del árbol
Permiten visitar los nodos en diferentes órdenes:

inorden(arbol): izquierda → raíz → derecha.
preorden(arbol): raíz → izquierda → derecha.
postorden(arbol): izquierda → derecha → raíz.
imprimir_arbol(arbol, nivel=0)
Muestra el árbol rotado 90°, con la raíz en la parte izquierda y los niveles representados por la indentación.

buscar(arbol, valor)
Busca un valor en el árbol. Devuelve True si el valor está presente, False en caso contrario.

encontrar_minimo(arbol)
Encuentra el valor mínimo en un subárbol. Esto es útil para la eliminación de nodos.

eliminar(arbol, valor)
Elimina un valor del árbol. Si el nodo tiene hijos, se reemplaza por el valor mínimo del subárbol derecho.

Ejemplo de uso
El código incluye un ejemplo práctico:

Se crea un árbol vacío.
Se insertan nombres como "Lucía", "Carlos", "Ana", etc.
Se imprimen los recorridos del árbol (inorden, preorden, postorden).
Se busca si ciertos nombres están en el árbol.
Se elimina el nodo "Lucía" y se muestra el árbol antes y después de la eliminación.
Salida esperada
Al ejecutar el código, se muestra:

El árbol rotado 90°.
Los recorridos del árbol.
Resultados de búsqueda (True o False).
El estado del árbol antes y después de eliminar un nodo.