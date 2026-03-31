# ---- Funciones provistas (NO modificar) ----

def count_vowels(text):
    """Dado un texto, retorna la cantidad de vocales (a, e, i, o, u) que contiene."""
    count = 0
    for char in text.lower():
        if char in "aeiou":
            count += 1
    return count

def count_consonants(text):
    """Dado un texto, retorna la cantidad de consonantes que contiene."""
    count = 0
    for char in text.lower():
        if char.isalpha() and char not in "aeiou":
            count += 1
    return count

# ---- Funciones a implementar ----

def total_letters(text):
    
    total = count_vowels(text) + count_consonants(text)
    return total 

def vowel_percentage(text):
    total= total_letters(text)
    if total==0:
        return 0.0
    
    total1= (count_vowels(text)*100)/(count_vowels(text)+count_consonants(text))
   
    return total1  

def analyze_text(text):
    vocales = count_vowels(text)
    consonantes = count_consonants(text)
    total= count_vowels(text)+ count_consonants(text)
    porciento= str(round(vowel_percentage(text),1))
    
    return f"V:{vocales} C:{consonantes} T:{total} P:{porciento}%"
    """
    Retorna un string con el análisis completo del texto usando el siguiente formato:
    "V:{vowels} C:{consonants} T:{total} P:{percentage}%"

    Debe USAR las funciones count_vowels, count_consonants, total_letters y vowel_percentage.

    Ejemplo: analyze_text("hola") → "V:2 C:2 T:4 P:50.0%"
    """
    
