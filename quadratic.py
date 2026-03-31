# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    discriminante= b*b-(4*a*c)
    if discriminante <0:
        return "( )"
    elif discriminante > 0:
        r1= (-b + ((b*b-(4*a*c))**0.5))/2*a
        r2= (-b - ((b*b-(4*a*c))**0.5))/2*a
        return f"({r1}, {r2})"
    else:
        r12= (-b/2*a)
        return f"({r12})"
        

def value_y(a, b, c, x):
    y= a*(x*x) + b*x + c
    return y 
    
 


def to_string(a, b, c):
    if a==0 and b==0:
        y = c
        return f"f(x) = {y}"
    elif a==0:
        return f"f(x) = {b} * X + {c}"
    elif b==0:
        return f"f(x) = {a} * X^2 + {c}"
    elif c==0:
        return f"f(x) = {a} * X^2+ {b} * X"
    else: 
        return f"f(x) = {a} * X^2 + {b} * X + {c}"
    


def derivation(a, b, c):
    if a==0 and b==0:
        return f"f'(x) = 0"
    elif a==0:
        return f"f'(x) = {b}"
    elif b==0:
        a= 2*a
        return f"f'(x) = {a} * X"
    elif c==0:
        a=2*a
        return f"f'(x) = {a} * X + {b}"
    else:
        a=2*a
        return f"f'(x) = {a} * X + {b}"
        


