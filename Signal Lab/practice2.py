import numpy as np
import matplotlib.pyplot as plt
n = np.arange(-10, 11)
x = np.array([abs(i) if -3 <= i <= 3 else 0 for i in n])
def shift(x, n, shift_amount):
    return np.array([x[n.tolist().index(k - shift_amount)] if (k - shift_amount) in n else 0 for k in n])


ya = x
yb = shift(x, n, 1)
yc = shift(x, n, -1)
print(ya)
print(yb)
print(yc)