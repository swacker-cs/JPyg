from pathlib import Path
from PIL import Image
import os

def readDir(selectedDir):
    dir = Path(selectedDir)
    img_extensions = { ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"}
    images = [
        path for path in dir.iterdir()
        if path.is_file() and path.suffix.lower() in img_extensions
    ]
    print(images)
    return images

def processImages(images, OutDir, size):
    counter = 0
    for img in images:
        fileName = img.stem + "_converted.jpg"
        savePath = Path(OutDir) / fileName
        image = Image.open(img)
        dimension = (size, size)
        print(image.mode)
        if image.mode != "RGB":
            image = image.convert("RGB")
        image.thumbnail(dimension, Image.LANCZOS)
        image.save(savePath, quality=95, subsampling=0)