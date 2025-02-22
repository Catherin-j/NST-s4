import numpy as np

def f(x, y):
    """Define the differential equation dy/dx = f(x, y)."""
    return eval(func)  # Evaluates user input function

def runge_kutta_4th(x0, y0, x_target, h):
    """Applies the 4th-order Runge-Kutta method."""
    x, y = x0, y0
    
    while x < x_target:
        if x + h > x_target:  # Adjust step if exceeding target
            h = x_target - x
        
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)
        
        y += (k1 + 2*k2 + 2*k3 + k4) / 6
        x += h
    
    return y

# User Input
func = input("Enter dy/dx as a function of x and y (e.g., x + y): ")
x0 = float(input("Enter initial x (x0): "))
y0 = float(input("Enter initial y (y0): "))
x_target = float(input("Enter x at which y is required: "))
h = float(input("Enter step size (h): "))

# Compute approximation
y_final = runge_kutta_4th(x0, y0, x_target, h)
print(f"The approximate value of y at x = {x_target} is: {y_final:.4f}")
