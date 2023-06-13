from interpreter import draw
from chessPictures import *

squareNeg = square.negative()
ImagenNueva = squareNeg.join(square)

ImagenNueva = ImagenNueva.horizontalRepeat(3)

draw(ImagenNueva)