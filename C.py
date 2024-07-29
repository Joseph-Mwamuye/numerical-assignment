import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


x_points = [2.00, 4.25, 5.25, 7.81, 9.20, 10.60]
y_points = [7.2, 7.1, 6.0, 5.0, 3.5, 5.0]


linear_spline = interp1d(x_points, y_points)


x_new = 4.0
y_new = linear_spline(x_new)

print(f"The interpolated value at x = {x_new} is y = {y_new}")


x_range = np.linspace(min(x_points), max(x_points), 500)
y_range = linear_spline(x_range)

plt.plot(x_points, y_points, 'o', label='Data points')
plt.plot(x_range, y_range, '-', label='Linear spline interpolation')
plt.plot(x_new, y_new, 'ro', label=f'Interpolated point (4.0, {y_new:.2f})')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Spline Interpolation')
plt.show()
