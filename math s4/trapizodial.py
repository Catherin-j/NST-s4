import numpy as np
import sympy as sp

def f(x, expr):
    return expr.subs('x', x).evalf()

def trapezoidal_rule(expr, a, b, n):
    h = (b - a) / n  # Step size
    x_values = np.linspace(a, b, n+1)
    y_values = [f(x, expr) for x in x_values]
    
    integral = (h / 2) * (y_values[0] + 2 * sum(y_values[1:-1]) + y_values[-1])
    return integral

# User Input
expr_str = input("Enter the function in terms of x (e.g., x**3 - 4*x - 9): ")
expr = sp.sympify(expr_str)
a = float(input("Enter the lower limit of integration: "))
b = float(input("Enter the upper limit of integration: "))
n = int(input("Enter the number of subintervals: "))

# Compute integral
result = trapezoidal_rule(expr, a, b, n)
print(f"The approximate integral using the Trapezoidal Rule is: {result:.4f}")
