from PIL import Image
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

# Warnings
import warnings;
warnings.simplefilter('ignore')

# Path
ROOT_PATH = os.path.abspath(os.path.join('../'+os.path.dirname('__file__')))

# Lista para almacenar las matrices de las imágenes
matrices = []
persona = []
images = []
import cv2
tamaño = (255, 255)
# Iterar sobre los archivos en el directorio
for archivo in os.listdir(ROOT_PATH +"/data/images/input/raw/"):
    # Comprobar si el archivo es una imagen
    if archivo.endswith(".jpg") or archivo.endswith(".png"):
        # Cargar la imagen
        imagen = Image.open(os.path.join(ROOT_PATH +"/data/images/input/raw/", archivo))
        img = cv2.imread(os.path.join(ROOT_PATH +"/data/images/input/raw/", archivo), 0)
        
        # Escala de grises
        imagen = imagen.convert('L')
        # Redimensionar la imagen
        imagen = imagen.resize(tamaño)
        # Guardar la imagen redimensionada
        imagen.save(ROOT_PATH +"/data/images/input/gold/" + archivo)
        # Convertir la imagen en una matriz NumPy y agregarla a la lista
        matriz = np.asarray(imagen).reshape((-1,))
        matrices.append(matriz)
        persona.append(archivo.split(".")[0])
        
# Convertir la matriz en un dataframe de pandas
# df_imagenes = pd.DataFrame(matrices)
df_imagenes = matrices

cv2.imshow('charlotte', matrices[1])
cv2.waitKey(0)