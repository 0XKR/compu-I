'''problema abstracto'''

cont,cont_p3,acum_p3,cont_p5 = 0
resp = 'si'
while resp == 'si' and cont < 100:
    nombre = input('nombre: ')
    v1 = float(input('valor 1: '))
    v2 = float(input('valor 2: '))
    tipo = input('tipo:[m,k,r]')

    cont += 1

    if tipo == 'k':
        p = v2 + (1+v2) / (v1+2)
    else:
        p = (1+v2) / v1 + v2

    if tipo == 'm':
        d = v2**(1/3)
    else:
        d = v2 / (v1+1)
    
    print(f'{p:.2f},{d:.2f}')

    if cont == 1:
        print('este es el primer resgistro')
        primer_p = p
    else: 
        if v2 > v2_ant:
            print('v2 aumento')
        else:
            print('v2 NO aumento')

        ultimo_p = p
    
    if v2 > 0:
        cont_p3 += 1
        acum_p3 += v2

    if abs(v1 - 100) <= 100 :
        menor_nombre = nombre
        menor = abs(v1 - 100)

        if abs(v1 - 100) == menor:
            cont_p5 += 1
            ultimo_v1 = v1
        else:
            cont_p5 = 1

    v2_ant = v2

    resp = input('Otro registro?[s/n]\n')

porc_p3 = cont_p3 * 100 / cont
prom_p4 = (ultimo_p + primer_p) / 2

print('el porcentaje de la pregunta 3 fue: ',porc_p3)
print('el promedio de la pregunta 4 fue: ',prom_p4)

print('el nomre leido del valor 1 mas cercano a 100 fue: ',menor_nombre)

if cont_p5 > 1:
    print(f'hubo {cont_p5} valores con el mismo acercamiento, el ultimo fue {ultimo_v1}')
    
    










