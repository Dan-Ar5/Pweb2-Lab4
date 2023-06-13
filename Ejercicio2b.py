from interpreter import draw
from chessPictures import *

Caballo1 = knight
blacKnight1 = knight.negative()

Caballo2 = knight
Caballo2 = Caballo2.verticalMirror()

blacKnight2 = knight.negative()
blacKnight2 = blacKnight2.verticalMirror()

Imagen = (blacKnight2.join(Caballo2)).up(Caballo1.join(blacKnight1))
draw(Imagen)