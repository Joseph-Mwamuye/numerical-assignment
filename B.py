import numpy as np
import scipy.integrate as integrate
import scipy.interpolate as interpolate
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats

# 1. Differentiation
def differentiate(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

# Example function
def f(x):
    return x**2 - x - 2

x = 2
print(f"Derivative of f(x) at x = {x}: {differentiate(f, x)}")

# 2. Numerical Integration
def integrand(x):
    return np.sin(x)

result, error = integrate.quad(integrand, 0, np.pi)
print(f"Integral of sin(x) from 0 to π: {result}")

# 3. Curve Fitting
def model(x, a, b):
    return a * np.exp(b * x)

x_data = np.linspace(0, 4, 50)
y_data = model(x_data, 2.5, 1.3) + np.random.normal(size=len(x_data))

params, covariance = curve_fit(model, x_data, y_data)
print(f"Fitted parameters: a = {params[0]}, b = {params[1]}")

# 4. Linear Regression
slope, intercept, r_value, p_value, std_err = stats.linregress(x_data, y_data)
print(f"Linear regression: slope = {slope}, intercept = {intercept}")

# 5. Spline Interpolation
x_points = [2.00, 4.25, 5.25, 7.81, 9.20, 10.60]
y_points = [7.2, 7.1, 6.0, 5.0, 3.5, 5.0]
spline = interpolate.CubicSpline(x_points, y_points)

x_new = np.linspace(2, 10.6, 100)
y_new = spline(x_new)

plt.plot(x_points, y_points, 'o', label='data points')
plt.plot(x_new, y_new, '-', label='spline interpolation')
plt.legend()
plt.show()
