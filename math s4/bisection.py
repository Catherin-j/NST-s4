import sympy as sp
def f(x, expr):
    return expr.subs('x', x).evalf()

def bisection_method(expr, a, b, tol=0.001):
    if f(a, expr) * f(b, expr) >= 0:
        print("Invalid interval. The function values at the endpoints must have opposite signs.")
        return None
    
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if f(c, expr) == 0:
            return round(c, 3)
        elif f(a, expr) * f(c, expr) < 0:
            b = c
        else:
            a = c
    return round((a + b) / 2, 3)

# User Input
expr_str = input("Enter the function in terms of x (e.g., x**3 - x - 2): ")
expr = sp.sympify(expr_str)
a = float(input("Enter the lower bound of the interval: "))
b = float(input("Enter the upper bound of the interval: "))

tol = 0.001  # 3 decimal places
root = bisection_method(expr, a, b, tol)
if root is not None:
    print(f"The root of the equation is approximately: {root}")
