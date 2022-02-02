import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1000, 50)
print(np.shape(x))

y = np.random.rand(len(x)) * 100

plt.figure(1)
plt.plot(x, y)

plt.show()