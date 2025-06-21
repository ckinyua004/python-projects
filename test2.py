import matplotlib.pyplot as plt
import numpy as np

# Constants
g = 9.81  # Gravity (m/s^2)
v0 = 20   # Initial speed (m/s)
theta = 45 * np.pi / 180  # Angle in radians

# Time array
t = np.linspace(0, 2 * v0 * np.sin(theta) / g, num=100)

# Equations of motion
x = v0 * np.cos(theta) * t
y = v0 * np.sin(theta) * t - 0.5 * g * t**2

# Plot
plt.plot(x, y)
plt.title("Projectile Motion")
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.grid()
plt.show()
