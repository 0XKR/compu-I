'''
Programa para calcular IMC
'''

M = int(input('Ingrese numero de personas: '))
suma_imc_obeso = 0
hombres_obesos = 0

primera_mujer_obesa = ''
contador_mujer_obesa = 0
contador_mujeres_mismo_tipo = 0
tipo_obesidad = ''

NDLPDBP = '' #NDLPDBP = nombre de la persona de bajo peso
SDLPDBP = '' #SDLPDBP = sexo de la persona de bajo peso
menor_talla = 100000000000000 #la idea es que al inicio sea un numero muy grande para cuando se evalue es sea el mayor y la condicion sea verdadera

for i in range(M):
 
    
    peso = float(input('Ingrese su peso: '))
    talla = float(input('Ingrese su talla: '))
    sexo =  str.upper(input('Ingrese su sexo (M ó F): '))
    nombre = input('Ingrese su nombre: ')

    IMC = peso/talla**2


    if IMC < 20 and talla < menor_talla:
        menor_talla = talla
        NDLPDBP = nombre
        SDLPDBP = sexo 



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

    if IMC >= 25 and sexo == 'F' and contador_mujer_obesa == 0:
        primera_mujer_obesa = nombre
        contador_mujer_obesa = contador_mujer_obesa + 1
        tipo_obesidad = a

    if a == tipo_obesidad:
        contador_mujeres_mismo_tipo = contador_mujeres_mismo_tipo + 1        

    else:
        print('el sexo debe ser M ó F!!')
    
    print(f'hola {nombre}, su tipo de peso es {a}, y su IMC es {IMC} ')

if hombres_obesos > 0:
    prom_obeso = suma_imc_obeso/hombres_obesos
    print(f'el promedio del IMC de hombres con peso mayor al normal es: {prom_obeso} ')
else: 
    print('no hay hombres con sobrepeso!')


if contador_mujer_obesa == 0:
    print('no hubo mujeres con obesidad prosesadas')
else:
    print('la primera mujer con obesidad fue: ',primera_mujer_obesa)
    
    if contador_mujeres_mismo_tipo - 1 > 1:
        print(f'hay {contador_mujeres_mismo_tipo - 1} mujeres con el mismo tipo de obesidad de {primera_mujer_obesa}')

    else:
        print(f'hay una sola mujer con el mismo tipo de obesidad de {primera_mujer_obesa}')


print(f'el nombre de la persona de menor talla es {NDLPDBP}, sexo: {SDLPDBP}, talla: {menor_talla}')







