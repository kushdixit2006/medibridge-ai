import easyocr
import cv2
import numpy as np
from PIL import Image
reader=easyocr.Reader(['en'])
def extract_text_from_image(image_path):
    results=reader.readtext(image_path,detail=0)
    return " ".join(results)
