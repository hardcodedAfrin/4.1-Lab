import numpy as np

# Original signals
x = np.array([1, 2, 3])
h = np.array([0, 0.5, 1])

# ---------- Convolution with 1-padding ----------
x_conv = np.pad(x, (1, 1), mode='constant')  # 1 zero left, 1 zero right
h_conv = np.pad(h, (1, 1), mode='constant')

N_conv = len(x_conv)
M_conv = len(h_conv)
L_conv = N_conv + M_conv - 1

conv = np.zeros(L_conv)
for n in range(L_conv):
    for k in range(N_conv):
        if 0 <= n - k < M_conv:
            conv[n] += x_conv[k] * h_conv[n - k]

# ---------- Correlation with 1-padding ----------
M = len(h)  # original h length
extra_pad = (M - 1) + 1  # M-1 for correlation + 1 extra for 1-padding
x_corr_padded = np.pad(x, (extra_pad, extra_pad), mode='constant')

N_corr = len(x_corr_padded)
L_corr = N_corr - M + 1

corr = np.zeros(L_corr)
for n in range(L_corr):
    for k in range(M):
        corr[n] += x_corr_padded[n + k] * h[k]  # h not flipped for correlation

print("Convolution (1-padding):", conv)
print("Correlation (1-padding):", corr)

'''For “1-padding”:

Add 1 extra zero at the start and 1 extra zero at the end of x and/or h.

This increases the output length and lets you see the effect of additional zeros at the edges.

Correlation length:

Minimum zeros required = M-1 on both sides of x.

1-padding: add 1 more zero on both sides → total M-1+1 zeros.'''