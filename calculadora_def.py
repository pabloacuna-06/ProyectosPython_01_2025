import time

def sumar(num1,num2):
    resultado_suma = num1 + num2
    return (resultado_suma)

def restar(num1,num2):
    resultado_resta = num1 - num2
    return (resultado_resta)

def division(num1,num2):
    try:
        resultado_division = num1 / num2
        return(resultado_division)
    except ZeroDivisionError:
        print("Error, no se puede dividir por 0.\n")
        time.sleep(3)

def multiplicacion(num1,num2):
    resultado_multiplicacion = num1 * num2
    return(resultado_multiplicacion)

def mostrar_menu():
    print("================================")
    print("Menu calculadora en python.")
    print("================================")
    print("1.sumar.")
    print("2.restar.")
    print("3.division.")
    print("4.multiplicacion.")
    print("5.salir.")

def obtener_numeros():
    while True:
        try:
            num1 = int(input("Ingresa un primer numero: "))
            num2 = int(input("Ingresa un segundo numero: "))
            return(num1,num2)
        except ValueError:
            print("Error,se ha ingresado un numero no valido.")
            time.sleep(3)

def main():
    while True:
        mostrar_menu()
    
        try:
            op = int(input("Ingrese una opcion de 1 -5: "))
        except ValueError:
            print("Error, Ingrese un numero valido.")
            time.sleep(3)
        if op < 1 or op > 5:
            print("Error,ha ingresado una opcion no valida")
            time.sleep(3)
        if op in [1,2,3,4]:
            num1,num2 = obtener_numeros()

            if op == 1:
                resultado = sumar(num1,num2)
                print(f"El resultado de la suma es: {resultado}\n")
                time.sleep(2)
            if op == 2:
                resultado = restar(num1,num2)
                print(f"El resultado de las resta es: {resultado}\n ")
                time.sleep(2)
            if op == 3:
                resultado = division(num1,num2)
                print(f"El resultado de la divison es: {resultado}\n")
                time.sleep(2)
            if op == 4:
                resultado = multiplicacion(num1,num2)
                print(f"El resultado de la multiplicacion es: {resultado}\n")
                time.sleep(2)
        if op == 5:
            print("Saliendo......")
            exit()

main()

























