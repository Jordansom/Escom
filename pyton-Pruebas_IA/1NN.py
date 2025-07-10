import numpy as np
from sklearn.datasets import load_iris, load_wine
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier

# Función para cargar y preprocesar el conjunto de datos
def cargar_datos(dataset_loader):
    datos = dataset_loader()
    X = datos.data
    y = datos.target
    return X, y

indice = 0

# Uso de arreglos para la indicación del cargado de datos como su nombres para la muestra
datasets = [load_iris, load_wine]
banco = ["Iris Dataset", "Wine Dataset"]

for load_dataset in datasets:
    # Cargar el conjunto de datos
    X, y = cargar_datos(load_dataset)

    # Imprime las características del Banco de datos Iris
    print("\nEl banco de datos:", banco[indice], "\n")
    print("Conjunto de características (X):")
    print(X[:10])
    print("Etiquetas de clases (y):")
    print(y[:10])

    # Configuración del clasificador k-NN
    knn = KNeighborsClassifier()

    # Realiza la validación cruzada de 10-fold
    scores = cross_val_score(knn, X, y, cv=10)

    # Imprime la precisión para cada fold
    print("\nPrecisión para cada fold:", scores)

    # Calcula y muestra la precisión promedio
    exactitud_promedio = np.mean(scores)
    print("\nExactitud promedio:", exactitud_promedio)

    indice += 1



