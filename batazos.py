'''batazos'''

from math import sin as sen, cos, tan as tg, pi

arch1 = open('estadio.txt','r')
arch2 = open('homerun.txt','w')
arch3 = open('otros','w')

cont_total = 0
cont_jonron = 0
cont_dentro = 0
cont_out = 0
mayor_xmax = 0


cent: int
contenido = arch1.readlines()
linea = 0

while linea < len(contenido):
    lst_ext = contenido[linea].split(',')
    largo_campo = lst_ext[0]
    altura_muro = lst_ext[1]
    linea += 1
    while cent == 0:
        lst_int = contenido[linea].split(',')
        nombre = lst_int[0]
        altura = float(lst_int[1])
        velocidad = float(lst_int[2])
        angulo = float(lst_int[3]) #grados
        angulo_rad = angulo * pi / 180 
        
        xmax = velocidad ** 2 * sen(2 * angulo_rad) / 9.81
        Y = altura + largo_campo * tg(angulo_rad) - 9.81 * (largo_campo) ** 2 / (2 * (velocidad) ** 2 * (cos(angulo_rad)) ** 2)
        if xmax > largo_campo and altura_muro < altura:
            cont_jonron += 1
            arch2.write(f'{nombre}\n') 

        # jonron mas largo
            if xmax > mayor_xmax:
                mayor_xmax = xmax
                mayor_nombre = nombre
                mayor_velocidad = velocidad
                mayor_angulo = angulo
        if xmax <= 36.88:
            cont_dentro += 1
            arch3.write(f'{nombre}\n')   

        elif (xmax > 36.88 and xmax < largo_campo) or (xmax > largo_campo and altura <= altura_muro):
            cont_out += 1
            arch3.write(f'{nombre}\n')

        cont_total += 1


if cont_total != 0:
    porc_jonrom = cont_jonron * 100 / cont_total
    porc_dentro = cont_dentro * 100 / cont_total 
    porc_out = cont_out * 100 / cont_total

    print(f'el porcentaje de jonrones fue: {porc_jonrom:.2f}%') 
    print(f'el porcentaje de dentro del cuadro fue: {porc_dentro:.2f}%')
    print(f'el porcentaje de outfielders fue: {porc_out:.2f}%')

print(f'el jonron mas largo lo hizo: {mayor_nombre}, velocidad: {mayor_velocidad}, angulo: {mayor_angulo}')

arch1.close()
arch2.close()    
arch3.close()        
