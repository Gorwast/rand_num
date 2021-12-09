import csv
from csv import Error
from datetime import datetime


def multiplyLenNormalize(seed):
    """Funcion que regresa un numero flotante que nos permite normalizar los numeros ingresados al poder multiplicarlo despues por el mismo

    Args:
        seed (int): Numero que deseamos saber su numero "normalizador"

    Returns:
        [float]: numero flotante que se puede multiplicar despues por seed para "normalizarlo"
    """
    # Determinamos la longitud de la semilla introducida por el usuario
    tam1 = len(str(seed))
    s = "0."
    for x in range(tam1 - 1):  # Creamos una cadena con 0's dependiendo de la longitud de la semilla
        s = s + "0"
    s = s + "1"
    f = float(s)#Convertimos la cadena a valor flotante
    return f

def getSeed():
    """Metodo que genera una semilla para los metodos siguientes, utiliza la hora del usuario

    Returns:
        [int]: Numero basado en el tiempo establecido en el reloj del usuario actual
    """
    d = datetime.utcnow()
    seed = (d.year + d.month + d.day + d.hour +
            d.minute + d.second + d.microsecond)
    return seed ** 2
    

def LCG(seed, n, a=1664525, c=1013904223, m=2**32):
    """METODO DEPRECADO
    Nota: este metodo al final no funciono como se esperaba, solo se deja con fines educativos

    Funcion implementa un Generador lineal congruencial (LCG) para la generacion de numeros aleatorios
    cuya estructura basica seria de la siguiente forma:

    def lcg(modulus: int, a: int, c: int, seed: int) -> Generator[int, None, None]:
    while True:
            seed = (a * seed + c) %% modulus
            yield seed

    Args:
            seed (int): Semilla con la que trabaja el metodo para generar n numeros pseudoaleatorios
            n (int): Cantidad de numeros a generar
            a (int, optional): Numero con el cual se multiplica la semilla en cada iteracion para crear un numero nuevo. Por defecto este es 1664525.
            c (int, optional): Constante la cual se suma a la semilla en cada iteracion para crear un numero nuevo. Por defecto este es 1013904223.
            m ([int], optional): modulo que se aplica a la operacion de crear un numero nuevo. la operación módulo obtiene el resto de la división de un número entre otro (a veces llamado residuo). Por defecto este es 2**32, en algunos casos se puede cambiar por 2**64.

    Returns:
            [type]: [description]

    Yields:
            [type]: [description]
    """
    numbers = []
    min_num = 100000000
    max_num = 0
    for i in range(n):
        seed = (a * seed + c) % m

        if (seed < min_num):
            min_num = seed

        if (seed > max_num):
            max_num = seed

        numbers.append(seed)
    print(min_num)
    print(max_num)
    return numbers


def randNumCuadradosMedios(seed, n, start=0, end=1, write_file=False, *args):
    """METODO DEPRECADO
    Nota: este metodo al final no funciono como se esperaba, solo se deja con fines educativos

    Funcion que toma una semilla para generar un grupo pseudoaleatorio de numeros, esta funcion utiliza el 
    Algoritmo de cuadrados medios pero se cambio por el metodo de Generador lineal congruencial porque esta funcion
    se cicla al generar mas de 10,000 numeros aprox.

    Args:
        seed (int): Semilla con la que trabaja el metodo para generar n numeros pseudoaleatorios
        n (int): Cantidad de numeros a generar
        start (int, optional): Inicio del rango en el cual se desea que se encuentren los numeros, si no se indica ninguno, este inicia en 0.
        end (int, optional): Inicio del rango en el cual se desea que se encuentren los numeros, si no se indica ninguno, este inicia en 1 .
    """
    f = multiplyLenNormalize(seed)

    print("Cantidad de dígitos: ", tam1)
    numero1 = int(seed)

    if write_file:
        with open('numeros_aleatorios.csv', 'w', newline='') as csvfile, open("demofile2.txt", "w") as txtf:
            spamwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='\"', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(("id", "numero_normal", "numero_en_rango"))
            for i in range(n):
                numero2 = numero1**2
                snumero2 = str(numero2)
                tam2 = len(snumero2)
                primerc = int((tam2 - tam1) / 2)

                snumero3 = snumero2[primerc:primerc+tam1]
                snumero3 = float(snumero3)

                OldRange = 1
                NewRange = (end - start)
                NewValue = (((snumero3*f) * NewRange) / OldRange) + start
                if write_file:
                    try:
                        spamwriter.writerow((i, snumero3 * f, NewValue))
                    except Error as e:
                        print("Error creando el archivo", e)
                print("{}.  {}   {}".format(i, snumero3 * f, NewValue))
                txtf.write(str(NewValue)+"\n")
                numero1 = int(snumero3)
    else:
        for i in range(n):
            numero2 = numero1**2
            snumero2 = str(numero2)
            tam2 = len(snumero2)
            primerc = int((tam2 - tam1) / 2)

            snumero3 = snumero2[primerc:primerc+tam1]
            snumero3 = float(snumero3)

            OldRange = 1
            NewRange = (end - start)
            NewValue = (((snumero3*f) * NewRange) / OldRange) + start
            print("{}.  {}   {}".format(i, snumero3 * f, NewValue))

            numero1 = int(snumero3)


def randNumWithLCG(n, start=0, end=1, write_file=False, roundOutput=False, a=15074714826142052245,c=1442695040888963407,m=2**64, *args):
    """Funcion que genera un grupo pseudoaleatorio de numeros usando la tecnica de Generador lineal congruencial (LCG)

    Args:
        n (int): Cantidad de numeros a generar
        start (int, optional): Inicio del rango en el cual se desea que se encuentren los numeros, si no se indica ninguno, este inicia en 0.
        end (int, optional): Inicio del rango en el cual se desea que se encuentren los numeros, si no se indica ninguno, este inicia en 1 .
        write_file (bool, optional): Opcion para crear un archivo de texto con los numeros generados. Por defecto este es False.
        roundOutput (bool, optional): Opcion para redondear los resultados de los numeros generados. Por defecto este es False.
        a (int, optional): Numero con el cual se multiplica la semilla en cada iteracion para crear un numero nuevo. Por defecto este es 1664525.
        c (int, optional): Constante la cual se suma a la semilla en cada iteracion para crear un numero nuevo. Por defecto este es 1013904223.
        m ([int], optional): modulo que se aplica a la operacion de crear un numero nuevo. la operación módulo obtiene el resto de la división de 
        un número entre otro (a veces llamado residuo). Por defecto este es 2**32, en algunos casos se puede cambiar por 2**64.
    """

    # Aqui creamos la semilla que vamos a utlizar, en nuestro caso usaremos la fecha del computador del usuario para crear la semilla
    seed = getSeed()
    print("Semilla: " + str(seed))
    numbers = []
    min_num = 1000000000000000000000000
    max_num = 0
    # Si write_file es verdadero, se creará un archivo con los numeros a generar
    if write_file:
        #abrimos el archivo de texto a continuacion
        with open('numeros_aleatorios.csv', 'w', newline='') as csvfile, open("numeros_aleatorios.txt", "w") as txtf:
            spamwriter = csv.writer(csvfile, delimiter=',',quotechar='\"', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(("id", "numero_normal", "numero_en_rango"))
            
            #Ciclo para calcular los valores y operaciones
            for i in range(n):
                #Calculamos el valor aleatorio con la siguiente formula
                seed = (a * seed + c) % m
                # Las siguientes lineas son para crear un factor por el cual se va a normalizar la semilla dada (seed * f)
                # Ej. pasar de 2158318253 a 0.2158318253
                f = multiplyLenNormalize(seed)

                # Aqui pasamos de tener una escala de 0.1 a 1, a tener una escala entre el valor de end y start
                OldRange = (18446677011695788001 - 16360254923613)
                NewRange = (end - start)
                NewValue = ((((seed)-16360254923613) * NewRange) /OldRange) + start

                # Si queremos el valor redondeado se cambia
                # Ej. 136.3128367152 pasa a 136
                if roundOutput:
                    NewValue = round(NewValue)

                try:
                    spamwriter.writerow((i, seed * f, NewValue))
                except Error as e:
                    print("Error agregando la fila al archivo", e)
                
                # Se imprime en consola el resultado
                print("{}. {}  {}".format(i, seed * f, NewValue))

                #Escribimos el valor en el archivo de texto
                txtf.write(str(NewValue)+"\n")
                numbers.append(NewValue)
    else:
        for i in range(n):
            #Calculamos el valor aleatorio con la siguiente formula
            seed = (a * seed + c) % m

            # Las siguientes lineas son para crear un factor por el cual se va a normalizar la semilla dada (seed * f)
            # Ej. pasar de 2158318253 a 0.2158318253
            f = multiplyLenNormalize(seed)

            # Aqui pasamos de tener una escala de 0.1 a 1, a tener una escala entre el valor de end y start
            OldRange = (18446677011695788001 - 16360254923613)
            NewRange = (end - start)
            NewValue = ((((seed*f)-16360254923613) * NewRange) / OldRange) + start

            # Si queremos el valor redondeado se cambia
            # Ej. 136.3128367152 pasa a 136
            if roundOutput:
                NewValue = round(NewValue)

            # Se imprime en consola el resultado
            print("{}.  {}".format(i, NewValue))
            numbers.append(NewValue)

    return numbers
