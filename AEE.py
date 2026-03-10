def gcd(a, b):
    # Guardamos originales
    a_orig, b_orig = a, b
    
    # Ajuste de valores iniciales para que x corresponda a 'a' y 'y' a 'b'
    # En la identidad ax + by = gcd
    x0, x1 = 1, 0  # Coeficientes para 'a'
    y0, y1 = 0, 1  # Coeficientes para 'b'
    
    print(f"\n---Algoritmo Extendido para gCD({a}, {b}) ---")
    
    while b != 0:
        q = a // b
        r = a % b
        
        print(f"División: {a:4} = {q:2} * {b:3} + {r:3}")
        
        # Actualizamos a y b
        a, b = b, r
        
        # Actualizamos coeficientes x e y
        # Nueva x = x_anterior - q * x_actual
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1

    # Al terminar el bucle, los coeficientes correctos quedaron en x0 y y0
    return a, x0, y0

if __name__ == "__main__":
    val_a = 3
    val_b = 26
    
    mcd, x, y = gcd(val_a, val_b)
    
    print("-" * 50)
    print(f"RESULTADO FINALE:")
    print(f"Máximo Común Divisor (gcd): {gcd}")  
    print(f"Coeficiente x (para {val_a}): {x}")
    print(f"Coeficiente y (para {val_b}): {y}")
    print("-" * 50)
    
    
    # Esta vez la verificación DEBE dar el MCD (2)
    verificacion = (val_a * x) + (val_b * y)
    print(f"Verificación: {val_a}({x}) + {val_b}({y}) = {verificacion}")