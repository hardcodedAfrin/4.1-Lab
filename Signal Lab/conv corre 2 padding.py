import numpy as np

x = np.array([1, 2, 3])
h = np.array([0, 0.5, 1])

N = len(x)
M = len(h)

# Use 2-padding (two zeros on both sides) for x
pad = 2
x_padded = np.pad(x, (pad, pad), mode='constant')

# Output length grows by 2*pad compared to the standard N+M-1
L = len(x_padded) + M - 1   # == (N + 2*pad) + M - 1

# --- Convolution (with 2-padding on x) ---
conv = np.zeros(L)
for n in range(L):
    for k in range(len(x_padded)):
        if 0 <= n - k < M:
            conv[n] += x_padded[k] * h[n - k]

# --- Correlation (with 2-padding on x) ---
corr = np.zeros(L)
for n in range(L):
    for k in range(M):
        idx = n + k
        if 0 <= idx < len(x_padded):   # guard for edges since we only padded by 2
            corr[n] += x_padded[idx] * h[k]

print("Convolution (2-padding): ", conv)
print("Correlation (2-padding): ", corr)
