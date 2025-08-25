import numpy as np

x = np.array([1, 2, 3])
h = np.array([0, 0.5, 1])

N = len(x)
M = len(h)
L = N + M - 1


conv = np.zeros(L)
for n in range(L):
    for k in range(N):
        if 0 <= n - k < M:
            conv[n] += x[k] * h[n - k]


corr = np.zeros(L)
x_padded = np.pad(x, (M - 1, M - 1), mode='constant')
for n in range(L):
    for k in range(M):
        corr[n] += x_padded[n + k] * h[k]

print("Convolution: ", conv)
print("Correlation: ", corr)
'''Convolution: Needs only enough zeros at the ends to handle output length. The loop’s if condition stops invalid indexing.

Correlation: To avoid index errors when sliding h over x, we explicitly pad both sides of x with 𝑀-1 zeros so every shift has a full M-length window.
Convolution:  [0.  0.5 2.  3.5 3. ]
Correlation:  [1.  2.5 4.  1.5 0. ]
'''