import numpy as np

x = np.array([1, 2, 3])
h = np.array([0, 0.5, 1])

# -------------------------
# Manual Convolution
# -------------------------
# h কে উল্টে নিতে হবে
h_flipped = h[::-1]

# full mode length = len(x) + len(h) - 1
n = len(x) + len(h) - 1
conv_result = np.zeros(n)

for i in range(n):
    total = 0
    for j in range(len(x)):
        k = i - j
        if 0 <= k < len(h_flipped):
            total += x[j] * h_flipped[k]
    conv_result[i] = total

# -------------------------
# Manual Correlation
# -------------------------
# correlation এ h উল্টানো হয় না
corr_result = np.zeros(n)

for i in range(n):
    total = 0
    for j in range(len(x)):
        k = i - j
        if 0 <= k < len(h):
            total += x[j] * h[k]
    corr_result[i] = total

# -------------------------
# Output
# -------------------------
print("Manual Convolution:", conv_result)
print("Manual Correlation:", corr_result)