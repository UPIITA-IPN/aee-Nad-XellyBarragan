import sys

def calcular_inverso(a, m):
    """
    Calcula el inverso multiplicativo de 'a' módulo 'm'
    usando el Algoritmo Extendido de Euclides.
    """
    m0 = m
    y = 0
    x = 1

    if m == 1:
        return 0

    while a > 1:
        # Si m es 0 y a > 1, no hay mcd = 1
        if m == 0:
            return None
            
        q = a // m
        t = m

        # Algoritmo de Euclides estándar
        m = a % m
        a = t
        t = y

        # Actualizamos x e y
        y = x - q * y
        x = t

    # Si el resultado es negativo, lo convertimos a positivo
    if x < 0:
        x = x + m0

    # Verificación final: el MCD debe ser 1
    return x

if __name__ == "__main__":
    # Validamos que existan los dos argumentos
    if len(sys.argv) != 3:
        print("Uso: python AEE.py <a> <m>")
        sys.exit(1)

    try:
        num = int(sys.argv[1])
        mod = int(sys.argv[2])
        
        resultado = calcular_inverso(num, mod)
        
        if resultado is not None:
            print(resultado)
        else:
            print("No existe (MCD != 1)")
            
    except ValueError:
        print("Error: Ingresa solo números enteros.")
