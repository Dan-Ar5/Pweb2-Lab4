from interpreter import draw
from chessPictures import *

squareBl = square.negative()
ImagenNueva = square.join(squareBl)

ImagenNueva = ImagenNueva.horizontalRepeat(3)

draw(ImagenNueva)