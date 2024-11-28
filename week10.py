import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

plt.style.use('whitegrid')

plt.plot(x, y1, label='Sine', color='red', linestyle='-', linewidth=2)
plt.plot(x, y2, label='Cosine', color='blue', linestyle='--', linewidth=2)
plt.plot(x, y3, label='Tangent', color='green', linestyle='-.', linewidth=2)

plt.show()