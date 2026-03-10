import sys

def get_inverse(a, n):
    # Algoritmo Extendido de Euclides simplificado
    a_orig, n_orig = a, n
    x0, x1 = 1, 0
    
    while n != 0:
        q = a // n
        a, n = n, a % n
        x0, x1 = x1, x0 - q * x1
    
    # Si el MCD no es 1, no hay inverso multiplicativo
    if a != 1:
        return None
    
    # El inverso es x0, ajustado al módulo n_orig
    return x0 % n_orig

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)

    try:
        val_a = int(sys.argv[1])
        val_n = int(sys.argv[2])
        
        inverso = get_inverse(val_a, val_n)
        
        if inverso is not None:
            print(inverso)
        else:
            print(f"No existe inverso para {val_a} mod {val_n}")
            
    except ValueError:
        sys.exit(1)