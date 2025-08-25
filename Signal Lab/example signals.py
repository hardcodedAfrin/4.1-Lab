import numpy as np
import matplotlib.pyplot as plt
n = np.arange(-10, 11)
x = np.array([abs(i) if -3 <= i <= 3 else 0 for i in n])
def shift(x, n, shift_amount):
    return np.array([x[n.tolist().index(k - shift_amount)] 
                     if (k - shift_amount) in n else 0 for k in n])
ya = x
yb = shift(x, n, 1)
yc = shift(x, n, -1)
yd = (shift(x, n, -1) + x + shift(x, n, 1))/3
ye = np.maximum.reduce([shift(x, n, -1), x, shift(x, n, 1)])
yf = np.cumsum(x)
fig, axs = plt.subplots(6, 1, figsize = (10, 15), sharex =  True)
titles = ['(a) y(n) = x(n)',
          '(b) y(n) = x(n - 1)',
          '(c) y(n) = x(n + 1)',
          '(d) y(n) = (1/3)[x(n+1) + x(n) + x(n - 1)]',
          '(e) y(n) = max(x(n+1), x(n), x(n - 1))',
          '(f) y(n) = cumulative sum of x(k)'
          ]

results = [ya, yb, yc, yd, ye, yf]
for i in range(6):
    axs[i].stem(n, results[i], basefmt=" ")
    axs[i].set_ylabel("y(n)")
    axs[i].set_title(titles[i])
    axs[i].grid(True)
axs[-1].set_xlabel("n")
plt.tight_layout()
plt.show()