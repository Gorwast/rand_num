import random_numbers as ran

option = 0
start = 0
end = 1
write_file = False
roundOutput = False

while True:
    try:
        print("")
        print("Que desea Hacer?")
        print("1. Generar Numeros.")
        print("2. Opciones.")
        print("3. Salir. ")
        print("")
        option = input("# ")
        
        if option == "1":
            numeros = input("¿Cuantos Numeros quiere generar?: ")
            ran.randNumWithLCG(int(numeros), start, end, write_file, roundOutput)
            continue
        elif option == "2":
            while True:
                try:
                    print("")
                    print("Opciones")
                    print("1. Inicio de rango de numeros: " + str(start))
                    print("2. Final de rango de numeros: " + str(end))
                    if write_file:
                        print("3.Escribir archivo: Si")
                    else:
                        print("3.Escribir archivo: No")
                    if roundOutput:
                        print("4.Redondear resultado: Si")
                    else:
                        print("4.Redondear resultado: No")
                    print("5. salir")
                    print("")
                    option = input("# ")
                    if option == "1":
                        start = input(
                            "Indique el inicio de rango de numeros (entero):")
                        start = int(start)
                        continue
                    elif option == "2":
                        end = input("Indique el final de rango de numeros (entero):")
                        end = int(end)
                        continue
                    elif option == "3":
                        write_file = not write_file
                        continue
                    elif option == "4":
                        roundOutput = not roundOutput
                        continue
                    elif option == "5":
                        break
                    else:
                        print("Intenta de nuevo")
                except ValueError as e:
                    print(e)
                    continue
                break
            else:
                print("Intenta de nuevo")
            continue
        elif option == "3":
            break
        else:
            print("Valor no deseado, intenta de nuevo")
            continue
        print("")

    except ValueError as e:
        print(e)
        continue
    break
