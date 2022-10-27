import numpy as np

x = np.array([2, 1, 3])

x = np.append(x, 4)
x = np.delete(x, 0)
x = np.sort(x)

print(x)