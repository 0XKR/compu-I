'''
Contraste de imagen en escala de grises 
_______________________________________

coeficiente de intensidad mayor de las 
zonas a escalas de grises y luego a cada 
pixel en escala de grises se le calcula el 
coeficiente de intensidad de contraste como
la diferencia entre el valor maximo de 
intensidad calculad y el el coefiente de 
intensidad que registra el pixel

Desarrolle programa que lea archivo "" que contiene:
coord en x, coord en y coeficiente de intensidad 
'''


arch1 = open('imagen.txt','r')
arch2 = open('contraste.txt','w')

contenido = arch1.readlines()

for linea in contenido:
    lst_linea = linea.split(',')
    x = int(lst_linea[0]) #coord en x
    y = int(lst_linea[1]) #coord en y
    r = int(lst_linea[2]) #intensida led rojo
    g = int(lst_linea[3]) #intensida led verde 
    b = int(lst_linea[4]) #intensida led azul

    mayor_i = r
    if b > r and b > g:
        b = mayor_i
        print('El mayor coeficiente de intesidad en la imagen es el azul')
    elif g > b and g > r:
        g = mayor_i
        print('El mayor coeficiente de intesidad en la imagen es el verde ')
    else: 
        print('El mayor coeficiente de intesidad en la imagen es el rojo')

    contraste_r = mayor_i - r
    contraste_b = mayor_i - b 
    contraste_g = mayor_i - g

    arch2.write(f'{x},{y},{contraste_r},{contraste_g},{contraste_b}')

arch1.close()
arch2.close()











