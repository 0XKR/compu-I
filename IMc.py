'''
Programa para calcular IMC
'''
M = int(input('Ingrese numero de personas: '))
suma_imc_obeso = 0
hombres_obesos = 0

for i in range(M):
 
    
    peso = float(input('Ingrese su peso: '))
    talla = float(input('Ingrese su talla: '))
    sexo =  str.upper(input('Ingrese su sexo (M ó F): '))
    nombre = input('Ingrese su nombre: ')

    IMC = peso/talla**2

    if IMC >= 24 and sexo == 'M':

        hombres_obesos = hombres_obesos+1
        suma_imc_obeso = suma_imc_obeso+IMC
        

    if sexo == 'M':
        if IMC < 20:
            a = 'bajo peso'
        elif IMC < 24:
            a = 'peso normal'
        elif IMC < 29:
            a = 'Obesidad tipo 1'
        elif IMC < 37:
            a = 'Obesidad tipo 2'
        else:
            a = 'Obesidad tipo 3'

    elif sexo == 'F':
        if IMC < 20:
            a = 'bajo peso'
        elif IMC < 25:
            a = 'peso normal'
        elif IMC < 30:
            a = 'Obesidad tipo 1'
        elif IMC < 40:
            a = 'Obesidad tipo 2'
        else:
            a = 'Obesidad tipo 3'

    else:
        print('el sexo debe ser M ó F!!')
    
    print(f'hola {nombre}, su tipo de peso es {a}, y su IMC es {IMC} ')

if hombres_obesos > 0:
    prom_obeso = suma_imc_obeso/hombres_obesos
    print(f'el promedio del IMC de hombres con peso mayor al normal es: {prom_obeso} ')
else: 
    print('no hay hombres con sobrepeso!')






