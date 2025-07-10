from sklearn.datasets import load_iris

# Cargar el conjunto de datos Iris
wine  = load_iris()

# Para ver los datos en forma de arreglo NumPy, puedes usar
X = wine.data
y = wine.target

# Imprimir las primeras 5 filas del conjunto de características (X)
print("Conjunto de características (X):")
print(X[:20])

# Imprimir las primeras 5 etiquetas de clases (y)
print("Etiquetas de clases (y):")
print(y[:5])