import numpy as np

def least_squares_parabola(x, y):
    A = np.vstack([np.square(x), x, np.ones(len(x))]).T  # Matrix for quadratic terms
    coeffs = np.linalg.lstsq(A, y, rcond=None)[0]  # Solve for a, b, c
    return coeffs  # Returns [a, b, c]

# User Input
n = int(input("Enter number of data points: "))
x = np.array([float(input(f"Enter x[{i}]: ")) for i in range(n)])
y = np.array([float(input(f"Enter y[{i}]: ")) for i in range(n)])

# Compute coefficients
a, b, c = least_squares_parabola(x, y)

# Output
print(f"Best-fitting parabola: y = {a:.4f}x^2 + {b:.4f}x + {c:.4f}")
