'''
Ejercicio propuesto 19
──────────────────────
Dolar Oficial Vs. Dolar Paralelo
'''

#Inicializacion
cont_p3 = 0
Acum_p4 = 0
cont = 0

q = int(input('Ingrese la cantidad de dias: ')) 

for i in range(q):

    #Entrada
    fecha = input('Ingrese fecha [DD/MM/AAAA]: ')
    precio_bolivares = float(input('Ingrese precio en BS: '))
    precio_dolares = float(input('Ingrese precio en $: ' ))

    cont += 1 #contador de dias transcurridos

    paralelo_dolar = precio_bolivares / precio_dolares

    #pregunta 1

    print(f'El precio del dolar paralelo es: {paralelo_dolar}')

    #pregunta 2

    if cont == 1: #cuando sea el primer dia el contador valdrá 1
        print('Este es el primer registro!') 

    else:
        variacion = precio_bolivares_ant - precio_bolivares #calcular variacion a partir del segundo dia

        if variacion != 0:
            print('Hubo variación')
        
        else:
            print('No hubo variación')

    precio_bolivares_ant = precio_bolivares

    #preguunta 3

    if paralelo_dolar > 150 * 4.3 / 100: #si el dolar paralelo supera en mas de un 50% al oficial contadorP3 suma 1
        cont_p3 +=1

    #Pregunta 4

    if cont == q or cont == q-1:
        Acum_p4 += paralelo_dolar

#pregunta 3
porcentaje = cont_p3 * 100 / cont

#pregunta 4
promedio = Acum_p4 / 2

#salida pregunta 3 y 4
print('El porcentaje de la pregunta 3 es : ',porcentaje)
print('El promedio de la pregunta 4 es :',promedio)
