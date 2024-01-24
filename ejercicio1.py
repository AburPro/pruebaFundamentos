v1=float(input('ingrese voltaje 1: '))
v2=float(input('ingrese voltaje 2: '))
v3=float(input('ingrese voltaje 3: '))
v4=float(input('ingrese voltaje 4: '))
v5=float(input('ingrese voltaje 5: '))
promedio=(v1+v2+v3+v4+v5)/5
if promedio > 220:
    print(f'{promedio} <- ALTO VOLTAJE')
else:
    print(f'{promedio} <- VOLTAJE CORRECTO')