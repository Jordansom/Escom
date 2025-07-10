import cv2
import os
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score
from sklearn.model_selection import train_test_split, cross_val_predict, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

# Cambiar al directorio que contiene las subcarpetas de cada clase
dataset_path = 'C:\\Users\\jorda\\Documents\\pyton\\kaggle\\shapes'
os.chdir(dataset_path)

# Lista de carpetas de las imágenes
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
        _, binary_image = cv2.threshold(cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX), 128, 255,
                                        cv2.THRESH_BINARY)

        # Calcular los momentos invariantes de Hu
        hu_moments = cv2.HuMoments(cv2.moments(binary_image)).flatten()

        # Almacenar los momentos invariantes y la etiqueta de clase
        hu_moments_list.append(hu_moments)
        labels_list.append(class_index)

# Convertir la lista en un array de numpy
X = np.array(hu_moments_list)
y = np.array(labels_list)
# Normalizar los datos
scaler = StandardScaler()
X_normalized = scaler.fit_transform(X)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_normalized, y, test_size=0.3, random_state=42)

# Definir los modelos adicionales
classifiers = [
    LogisticRegression(max_iter=1000),
    SVC(kernel='linear',probability=True),
    SVC(kernel='rbf',probability=True),
    RandomForestClassifier(),
    KNeighborsClassifier(),
    DecisionTreeClassifier(),
    GaussianNB(),
    GradientBoostingClassifier(),
    AdaBoostClassifier(),
    QuadraticDiscriminantAnalysis()
]

# Definir los parámetros a probar para cada clasificador (ajustar según sea necesario)
param_grids = [
    {'C': [0.001, 0.01, 0.1, 1, 10, 100], 'penalty': ['l2']},
    {'C': [0.001, 0.01, 0.1, 1, 10, 100]},
    {'C': [0.001, 0.01, 0.1, 1, 10, 100], 'gamma': [0.001, 0.01, 0.1, 1, 10, 100]},
    {'n_estimators': [50, 100, 200]},
    {'n_neighbors': [3, 5, 7], 'weights': ['uniform', 'distance']},
    {'max_depth': [None, 5, 10, 20], 'min_samples_split': [2, 5, 10]},
    {},  # No hay parámetros específicos para GaussianNB
    {'n_estimators': [50, 100, 200], 'learning_rate': [0.01, 0.1, 1]},
    {'n_estimators': [50, 100, 200], 'learning_rate': [0.01, 0.1, 1]},
    {} 
]

nombre_modelos = [
    'Logistic Regression', 'SVC (linear)', 'SVC (rbf)', 'Random Forest', 'K-Neighbors',
    'Decision Tree', 'GaussianNB', 'Gradient Boosting', 'AdaBoost', 'QDA'
]  # ,'MLP',

# Realizar GridSearchCV para ajuste de hiperparámetros
for clf, param_grid, nombre_modelo in zip(classifiers, param_grids, nombre_modelos):
    grid_search = GridSearchCV(clf, param_grid, cv=5, scoring='accuracy')
    grid_search.fit(X_train, y_train)

    print(f'\nMejores parámetros para {nombre_modelo}:')
    print(grid_search.best_params_)

    # Predecir las clases de los patrones de prueba
    result7030 = grid_search.predict(X_test)
    
    # Modificar para manejar la métrica AUC en un problema multiclase
    result7030_proba = grid_search.predict_proba(X_test)
    auc_7030 = roc_auc_score(y_test, result7030_proba, multi_class='ovr')

    print('\nModelo:', nombre_modelo)
    # Calcular y mostrar las métricas de desempeño
    print("Accuracy 70-30:", accuracy_score(y_test, result7030))
    print("AUC 70-30:", auc_7030)
    print("Confusion Matrix 70-30:\n", confusion_matrix(y_test, result7030))

    # Cross-validation con el mejor modelo
    Cros_result = cross_val_predict(grid_search.best_estimator_, X_normalized, y, cv=10)
    
    # Modificar para manejar la métrica AUC en un problema multiclase
    Cros_result_proba = cross_val_predict(grid_search.best_estimator_, X_normalized, y, cv=10, method='predict_proba')
    auc_cv = roc_auc_score(y, Cros_result_proba, multi_class='ovr')

    print("\nAccuracy k=10:", accuracy_score(y, Cros_result))
    print("AUC k=10:", auc_cv)
    print("Confusion Matrix k=10:\n", confusion_matrix(y, Cros_result))

# Crear el directorio para las imágenes de momentos invariantes
output_images_dir = 'moment_invariant_images'
os.makedirs(output_images_dir, exist_ok=True)

# Guardar momentos invariantes en formato CSV
df = pd.DataFrame(X_normalized, columns=[f'Hu_{i}' for i in range(X_normalized.shape[1])])
df['label'] = y
df.to_csv('hu_moments_dataset.csv', index=False)

# Guardar imágenes en un directorio
output_images_dir = 'moment_invariant_images'
os.makedirs(output_images_dir, exist_ok=True)

for i, (hu_moments, label) in enumerate(zip(X_normalized, y)):
    image = np.zeros((100, 100, 3), dtype=np.uint8)  # Create a blank image
    image_path = os.path.join(output_images_dir, f'image_{i}_class_{label}.png')

    # Save the image with the corresponding label in the filename
    cv2.imwrite(image_path, image)

print("Dataset and images saved successfully.")