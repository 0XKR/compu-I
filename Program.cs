int cont_p3 = 0;
decimal acum = 0;
int cont = 0;




Console.WriteLine("Ingrese numero de dias: ");
int q = Convert.ToInt32(Console.ReadLine());

for (int i = 0; i < q; i++)
{
   
    decimal bolivar_ant = 0; 
    Console.WriteLine("Fecha: ");
    string fecha = Console.ReadLine();
    Console.WriteLine("Precio en bolivares: ");
    decimal bolivares = Convert.ToDecimal(Console.ReadLine());
    Console.WriteLine("Dolares: ");
    decimal dolares = Convert.ToDecimal(Console.ReadLine());
    cont++;
    decimal paralelo = bolivares / dolares;

    Console.WriteLine("El precio del paralelo es: {0}",paralelo);

    if (cont == 1)
    {
        Console.WriteLine("Es el primer registro");
    }
    else
    {
        decimal variacion = bolivar_ant - bolivares;
        if (variacion != 0)
        {
            Console.WriteLine("hubo variacion");
        }
        else
        {
            Console.WriteLine("No hubo Variacion");
        }
    }
    bolivar_ant = bolivares;

    if (paralelo > (decimal)(150 * 4.3/ 100))
    {
        cont_p3++;
    }
    if (cont == q | cont == q - 1)
    {
        acum += paralelo;
    }
}
float porc = cont_p3 * 100 / cont;
Console.WriteLine("El porcentaje es: {0}", porc);
decimal prom = acum / 2;
Console.WriteLine("El promedio es: {0}", prom);
