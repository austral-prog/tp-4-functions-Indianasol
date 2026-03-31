# ---- Funciones provistas (NO modificar) ----

def is_even(n):
    """Dado un número entero n, retorna True si es par, False si es impar."""
    return n % 2 == 0

def is_positive(n):
    """Dado un número entero n, retorna True si es mayor a 0, False en caso contrario."""
    return n > 0

# ---- Función a implementar ----

def classify_number(n):
    if n == 0:
        return "zero"
    elif is_positive(n) and is_even(n):
        return f"positive even"
    elif not is_positive(n) and is_even(n):
        return f"negative even"
    elif is_positive(n) and not is_even(n):
        return f"positive odd"
    else:
        return f"negative odd"
    
