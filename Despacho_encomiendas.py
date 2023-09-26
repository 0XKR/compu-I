
from datetime import date, timedelta



def leer(lista_contenido,linea):
    lst_linea = lista_contenido[linea].split(',')
    cedula = lst_linea[0]
    nombre = lst_linea[1]
    ciudad = lst_linea[2]
    peso = float(lst_linea[3])
    largo = float(lst_linea[4])
    ancho = float(lst_linea[5])
    alto = float(lst_linea[6])
    cent = float(lst_linea[7])
    
    return (
        cedula, nombre, 
        ciudad, peso, largo, 
        ancho, alto, cent
        )

def generar_arch1(arch,cedula,nombre,ciudad,peso,largo,ancho,alto,fecha_envio,fecha_llegada):
    arch.write(f'{cedula},{nombre},{ciudad},{peso},{largo},{ancho},{alto},{fecha_envio},{fecha_llegada}')
    
def generar_arch2(arch,cedula,nombre,ciudad,perimetro,costo):
    arch.write(f'{cedula},{nombre},{ciudad},{perimetro},{costo}')

def convertir_fecha(fecha):
    lst_fecha = fecha.split('/')
    dia = int(lst_fecha[0])
    mes = int(lst_fecha[1])
    año = int(lst_fecha[2])

    fecha_date = date(año,mes,dia)
    return fecha_date

def sumar_fecha(fecha,cant_dias):
    
    fecha_date = convertir_fecha(date)
    return fecha_date + timedelta(cant_dias)

def la_mayor(l,an,al):
    mayor = l
    if l < an:
        mayor = an 
    elif an < al:
        mayor = al
    return mayor

def perimetro(l,an,al,mayor):
    return 2 * (l + an + al - mayor)

def tarifa(peso):
    if peso < 3.5:
        tarifa = 400  

    if peso <= 8:
        tarifa = 650  

    if peso > 8: 
        tarifa = 1000

    return tarifa

def tipo(l,an,al,per):
    tipo_env = 'extraordinario'
    if l <= 1 and an <=1 and al <=1 and per <= 2:
        tipo_env = 'normal'
    return tipo_env


    
 
def main():
    
    arch1 = open('recepcion.txt','r')
    arch2 = open('normal.txt','w')
    arch3 = open('extraordinario.txt','w')
    arch4 = open('costos_envio.txt','w')

    contenido = arch1.readlines()
    linea = 0
    
    
    while linea < len(contenido):
        cent = 0
        fecha_envio = contenido[linea]
        
        linea += 1

        while cent == 0:
            
            cedula, nombre, ciudad, peso, largo, ancho, alto, cent = leer(contenido,linea)
            
            
            
            linea += 1


    


if __name__ == '__main__':
    main()

