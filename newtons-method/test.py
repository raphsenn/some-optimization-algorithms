import numpy as np
import matplotlib.pyplot as plt

# Zielfunktion
def f(x, y):
    return x + y

# Gleichheitsbeschränkung
def c(x, y):
    return 2 - x**2 - y**2

# Gitter für x und y erstellen
x = np.linspace(-3, 3, 400)
y = np.linspace(-3, 3, 400)
X, Y = np.meshgrid(x, y)

# Zielfunktion und Gleichheitsbeschränkung auswerten
Z_f = f(X, Y)
Z_c = c(X, Y)

# Plot der Zielfunktion
plt.contour(X, Y, Z_f, levels=20, cmap='viridis', label='Zielfunktion')

# Plot der Gleichheitsbeschränkung
plt.contour(X, Y, Z_c, levels=[0], colors='red', label='Gleichheitsbeschränkung')

# Plot-Einstellungen
plt.xlabel('x')
plt.ylabel('y')
plt.title('Optimierungsproblem mit Gleichheitsbeschränkung')
plt.legend()
plt.grid(True)
plt.show()
