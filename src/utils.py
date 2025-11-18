import cv2
import os

def load_image(path):
    """Carga una imagen con manejo básico de errores."""
    img = cv2.imread(path)
    if img is None:
        raise ValueError(f"No se pudo leer la imagen: {path}")
    return img