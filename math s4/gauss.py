import numpy as np

def gauss_seidel(A, b, x0, tol=1e-3, max_iterations=100):
    n = len(A)
    x = np.array(x0, dtype=float)
    for _ in range(max_iterations):
        x_new = np.copy(x)
        for i in range(n):
            sum1 = sum(A[i][j] * x_new[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum1) / A[i][i]
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new.round(3)
        x = x_new
    return x.round(3)

# Taking user input
n = int(input("Enter the number of equations: "))
A = []
b = []
print("Enter the coefficients matrix:")
for _ in range(n):
    A.append(list(map(float, input().split())))
print("Enter the constants vector:")
b = list(map(float, input().split()))
print("Enter initial guesses:")
x0 = list(map(float, input().split()))

# Solve using Gauss-Seidel method
solution = gauss_seidel(A, b, x0)
print("Solution:", solution)