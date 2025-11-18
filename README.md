## Descripción

Este proyecto busca explorar técnicas de visión por computadora y aprendizaje automático para el reconocimiento de especies de plantas a partir de imágenes de hojas. Se plantea como un ensayo práctico y piloto, sencillo pero funcional, orientado a incursionar en herramientas de procesamiento y análisis de imágenes.

Se desarrolló en dos fases:

**Primera Fase**: 
Visión clásica (OpenCV): extracción de características manuales como área, perímetro, color promedio.

Machine Learning: entrenamiento de un modelo de clasificación (Random Forest, SVM, KNN) utilizando esas características.

El dataset utilizado fue el Swedish Leaf Dataset, con 15 especies de plantas (balanceado).

**Segunda Fase**:
Uso de modelos preentrenados para la identificación de plantas como Resnet.

## Referencias

Swedish Leaf Dataset: [Kaggle](https://www.kaggle.com/datasets/majorproject24/swedish-leaf-dataset?resource=download-directory)
OpenCV documentation: https://docs.opencv.org/
Scikit-learn: https://scikit-learn.org/stable/

# Uso del Dataset
Este proyecto usa el dataset Swedish Leaf.
Descárgalo desde Kaggle
Luego descomprímelo en tu ordenador y actualiza la variable `DATASET_PATH` en el código (con la ruta acorde a tu archivo)

