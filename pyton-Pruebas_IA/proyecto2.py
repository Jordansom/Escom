import cv2
import os
import numpy as np
import joblib
import pandas as pd
from skimage.measure import regionprops
from sklearn.model_selection import cross_val_predict, train_test_split, cross_val_score, StratifiedKFold, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import VotingClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score, roc_auc_score, confusion_matrix

# Cambiar al directorio que contiene las subcarpetas de cada clase
dataset_path='C:\\Users\\jorda\\Documents\\pyton\\kaggle\\shapes'
os.chdir(dataset_path)

# Lista de carpetas de las imagenes
classes = ["circle", "square", "star", "triangle"]

# Número de imágenes por clase en la muestra de cada carpeta
sample_size_per_class = 250

# Listas para almacenar los momentos invariantes y las etiquetas de clase
hu_moments_list = []
labels_list = []

# Crear una muestra equilibrada
for class_index, class_name in enumerate(classes):
    class_path = os.path.join(dataset_path, class_name)
    images = os.listdir(class_path)
    
    for image_name in images[:sample_size_per_class]:
        image_path = os.path.join(class_path, image_name)

        # Leer la imagen y convertirla a escala de grises
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        # Normalizar la imagen y binarizarla
        _, binary_image = cv2.threshold(cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX), 128, 255, cv2.THRESH_BINARY)

        # Calcular los momentos invariantes de Hu
        hu_moments = cv2.HuMoments(cv2.moments(binary_image)).flatten()

        # Almacenar los momentos invariantes y la etiqueta de clase
        hu_moments_list.append(hu_moments)
        labels_list.append(class_index)

# Guardar los momentos invariantes y las etiquetas en un archivo
#joblib.dump((hu_moments_list, labels_list), "momentos_invariantes.pkl")

# Convertir la lista en un array de numpy
X = np.array(hu_moments_list)
y= np.array(labels_list)
# Normalizar los datos
scaler = StandardScaler()
X_normalized = scaler.fit_transform(X.reshape(-1, 1))
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

modelo = [LogisticRegression(),SVC(),RandomForestClassifier(n_estimators=100, random_state=42),KNeighborsClassifier()]
nombre_modelos = ['Logistic Regression', 'SVC', 'Random Forest', 'K-Neighbors']

for i, modelo_i in enumerate(modelo):
    Cros_result = cross_val_predict(modelo[i], X, y, cv=10)
    #Asegurar que Cros_result sea una matriz bidimensional
    Cros_result = Cros_result.reshape(-1, 1)
    # Crear y entrenar el clasificador 70-30
    clf = modelo[i]
    clf.fit(X_train, y_train)
    # Predecir las clases de los patrones de prueba
    result7030 = clf.predict(X_test)
    # Asegurar que result7030 sea una matriz bidimensional
    result7030 = result7030.reshape(-1, 1)

    print('\nModelo:',nombre_modelos[i])
    # Calcular y mostrar las métricas de desempeño
    print("\nAccuracy 70-30:", accuracy_score(y_test, result7030))
    #print("AUC:", roc_auc_score(y_test, result7030, multi_class='ovr'))
    print("\nConfusion Matrix 70-30:\n", confusion_matrix(y_test, result7030))
    # Calcular y mostrar las métricas de desempeño
    print("\nAccuracy k=10:", accuracy_score(y, Cros_result))
    # Calcular AUC por clase utilizando OneVsRestClassifier
    print("\nConfusion Matrix k=10:\n", confusion_matrix(y, Cros_result))


    



