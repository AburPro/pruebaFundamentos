import math
l=float(input('Para un triangulo equilatero\nIngrese la longitud del lado: '))
area=(math.sqrt(3)/4)*math.pow(l,2)
if area <1000:
    print(area)
else:
    print('DATOS NO VALIDOS')