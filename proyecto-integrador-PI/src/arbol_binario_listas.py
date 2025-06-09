# arbol_binario_listas.py
# Proyecto Integrador - Programación I


# -----------------------------
# Árbol Binario con Listas
# -----------------------------

# Crear un árbol con un valor inicial
def crear_arbol(valor):
    return [valor, [], []]

# Insertar un valor en el árbol binario (orden alfabético)
def insertar(arbol, valor):
    if arbol == []:
        arbol += crear_arbol(valor)
    elif valor < arbol[0]:
        insertar(arbol[1], valor)
    else:
        insertar(arbol[2], valor)

# Recorrido inorden (izquierda - raíz - derecha)
def inorden(arbol):
    if arbol != []:
        inorden(arbol[1])
        print(arbol[0])
        inorden(arbol[2])

# Recorrido preorden (raíz - izquierda - derecha)
def preorden(arbol):
    if arbol != []:
        print(arbol[0])
        preorden(arbol[1])
        preorden(arbol[2])

# Recorrido postorden (izquierda - derecha - raíz)
def postorden(arbol):
    if arbol != []:
        postorden(arbol[1])
        postorden(arbol[2])
        print(arbol[0])

# Visualización del árbol rotado 90°
def imprimir_arbol(arbol, nivel=0):
    if arbol != []:
        imprimir_arbol(arbol[2], nivel + 1)
        print('   ' * nivel + str(arbol[0]))
        imprimir_arbol(arbol[1], nivel + 1)

# Buscar un valor en el árbol
def buscar(arbol, valor):
    if arbol == []:
        return False
    if arbol[0] == valor:
        return True
    elif valor < arbol[0]:
        return buscar(arbol[1], valor)
    else:
        return buscar(arbol[2], valor)

# Encontrar el valor mínimo en un subárbol (usado en eliminación)
def encontrar_minimo(arbol):
    actual = arbol
    while actual[1] != []:
        actual = actual[1]
    return actual[0]

# Eliminar un valor del árbol
def eliminar(arbol, valor):
    if arbol == []:
        return []

    if valor < arbol[0]:
        arbol[1] = eliminar(arbol[1], valor)
    elif valor > arbol[0]:
        arbol[2] = eliminar(arbol[2], valor)
    else:
        if arbol[1] == []:
            return arbol[2]
        elif arbol[2] == []:
            return arbol[1]
        minimo = encontrar_minimo(arbol[2])
        arbol[0] = minimo
        arbol[2] = eliminar(arbol[2], minimo)
    return arbol

# -----------------------------
# Ejemplo de uso del árbol
# -----------------------------

nombres = ["Lucía", "Carlos", "Ana", "Martín", "Sofía", "Zoe", "Pedro"]

arbol_nombres = []

for nombre in nombres:
    insertar(arbol_nombres, nombre)

print("Árbol rotado 90°:")
imprimir_arbol(arbol_nombres)

print("\nRecorrido inorden:")
inorden(arbol_nombres)

print("\n¿Está 'Pedro'? ", buscar(arbol_nombres, "Pedro"))
print("¿Está 'Laura'? ", buscar(arbol_nombres, "Laura"))

print("\nÁrbol antes de eliminar 'Lucía':")
imprimir_arbol(arbol_nombres)

eliminar(arbol_nombres, "Lucía")

print("\nÁrbol después de eliminar 'Lucía':")
imprimir_arbol(arbol_nombres)

print("\nRecorrido preorden:")
preorden(arbol_nombres)

print("\nRecorrido postorden:")
postorden(arbol_nombres)
