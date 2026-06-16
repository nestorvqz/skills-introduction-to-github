# Programa simple en Python: determinar si un número es par o impar

def es_par(num):
    # Retorna True si el número es par
    return num % 2 == 0

def main():
    try:
        valor = input("Ingresa un número: ").strip()

        # Validación: verificar que sea un número entero
        numero = int(valor)

        if es_par(numero):
            print(f"El número {numero} es PAR.")
        else:
            print(f"El número {numero} es IMPAR.")

    except ValueError:
        # Manejo de error si el usuario no ingresa un entero válido
        print("Error: debes ingresar un número entero válido.")

if __name__ == "__main__":
    main()

