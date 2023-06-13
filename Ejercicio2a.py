from interpreter import draw
from chessPictures import *

Caballo1 = knight
blacKnight1 = knight.negative()
Caballo2 = knight
blacKnight2 = knight.negative()

Imagen = (blacKnight2.join(Caballo2)).up(Caballo1.join(blacKnight1))
draw(Imagen)
