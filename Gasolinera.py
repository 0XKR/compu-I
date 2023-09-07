'''
Estación de servicio Internacional
'''
resp = 's'
cont_p3 = 0
cont_p4 = 0
cont_combustible_en_exceso = 0
cont_vehiculos_totales = 0
cant_anterior = 0
lect_anterior = 1000000000


while resp == 's':
    
    #Entrada
    nombre = input('nombre: ')
    hora_llegada = float(input('Hora de llegada [HH,MM]: '))
    hora_despacho = float(input('Hora de despacho [HH,MM]: '))
    tipo_vehiculo = int(input('Tipo de vehiculo [1, 2 ó 3]: '))
    lect_inicial = float(input('Lectura inicial del tanque:'))
    cant_comprada = float(input('Cantidad de gasolina comprada(litros): '))

    #Pregunta 1
    monto = cant_comprada / 2
    print(f'El monto en dolares fue de ${monto}')

    total_litros = lect_inicial + cant_comprada

    if tipo_vehiculo == 1:

        litros_faltan = 35 - lect_inicial
        if total_litros > 35:
            exceso = total_litros - 35
            print(f'se excedio por {exceso} litros')

            cont_combustible_en_exceso += 1 # <---- anexo de la pregunta 5 (va a contar las veces que se excedio)
        
    elif tipo_vehiculo == 2:

        litros_faltan = 56 - lect_inicial
        if total_litros > 56:
            exceso = total_litros - 56
            print(f'se excedio por {exceso} litros')

            cont_combustible_en_exceso += 1 # <---- anexo de la pregunta 5

    else:

        litros_faltan = 120 - lect_inicial
        if total_litros > 120:
            exceso = total_litros - 120
            print(f'se excedio por {exceso} litros')

            cont_combustible_en_exceso += 1 # <---- anexo de la pregunta 5

    #Pregunta 2
    tiempo = hora_despacho - hora_llegada
    print(f'El tiempo transcurrido fue [{tiempo}]')

    #Pregunta 3 (proceso)
    if tipo_vehiculo != 2 and hora_llegada >= 18:
        cont_p3 += 1

    cont_vehiculos_totales += 1
    
    #Pregunta 4 (proceso)
    if cant_comprada >= cant_anterior and lect_inicial <= lect_anterior:
        
        ultimo_nombre = nombre
        ultimo_tipo_vehiculo = tipo_vehiculo
        cant_anterior = cant_comprada
        lect_anterior = lect_inicial

        if cant_comprada == cant_anterior and lect_inicial == lect_anterior:
            
            ultimo_nombre = nombre
            cont_p4 += 1

        else:
            
            ultimo_nombre = nombre
            ultimo_tipo_vehiculo = tipo_vehiculo
            cont_p4 = 0


    resp = input('desea agregar otro vehiculo? [s ó n]: ')
    #fin del ciclo


#pregunta 5 (proceso)
porc_exceso = cont_combustible_en_exceso * 100 / cont_vehiculos_totales

#Imprimir pregunta 3
print(f'hubo {cont_p3} vehiculos diferentes al sedan que no pudieron ser atendidos por llegar tarde')

#Imprimir Pregunta 4

print(f'El nombre del ultimo cliente que surtio la mayor cantidad de combustible y con menor lectura inicial fue: {ultimo_nombre}, su vehiculo es de tipo {ultimo_tipo_vehiculo} ')
if cont_p4 > 0:
    print(f'Hubo {cont_p4} clientes con la misma condicion')

#Imprimir Pregunta 5
print(f'hubo un {porc_exceso}% de clientes que compraron gasolina en exceso')
