v1=float(input('ingrese voltaje 1: '))
v2=float(input('ingrese voltaje 2: '))
v3=float(input('ingrese voltaje 3: '))
if v1!=v2!=v3:
    voltaje=(v1+v2+v3)/3
    if voltaje<115:
        print(f'{voltaje} VOLTAJE CORRECTO')
    elif voltaje>115 and voltaje<220:
        print(f'{voltaje} ALTO VOLTAJE')
    else:
        print('PELIGRO')
else:
    print('DATOS NO VALIDOS')