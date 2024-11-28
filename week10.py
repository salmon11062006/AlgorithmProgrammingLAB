import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

size = int(input("Enter the size of the array: "))

graph_type = input("Enter the type of graph (plot, scatter, bar): ").strip().lower()

x = np.arange(1, size + 1)

y = x ** 2

if graph_type == 'plot':
    plt.plot(x, y)
elif graph_type == 'scatter':
    plt.scatter(x, y)
elif graph_type == 'bar':
    plt.bar(x, y)
else:
    print("Invalid graph type. Please enter 'plot', 'scatter', or 'bar'.")

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Assignment Week 10')
plt.show()