import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)  # Example function

def trapezoidal_rule(a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    integral = (h / 2) * (y[0] + 2 * np.sum(y[1:n]) + y[n])
    return integral

# Parameters
a = 0  # Start of the interval
b = np.pi  # End of the interval
n = 10  # Number of trapezoids

# Calculate the integral
integral = trapezoidal_rule(a, b, n)

# Print the result
print(f"Approximate integral of sin(x) from {a} to {b} using {n} trapezoids is {integral}")

# Plotting
x = np.linspace(a, b, 1000)
y = f(x)

plt.plot(x, y, 'b', label='sin(x)')
plt.fill_between(x, 0, y, color='skyblue', alpha=0.4)

# Plot trapezoids
x_trap = np.linspace(a, b, n+1)
y_trap = f(x_trap)

for i in range(n):
    plt.plot([x_trap[i], x_trap[i], x_trap[i+1], x_trap[i+1]], [0, y_trap[i], y_trap[i+1], 0], 'r')

plt.title('Trapezoidal Rule Approximation')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()