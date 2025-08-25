import numpy as np
import matplotlib.pyplot as plt

# Define n range
n = np.arange(-3, 5)  # from n = -3 to 4

# Define x(n) according to given data
# Values: [2, 2, 2, 0 (at n=0), 1, 2, 3, 4]
x = np.array([2, 2, 2, 0, 1, 2, 3, 4])

# Function to reverse/shift signals
def reverse(signal, n):
    # reverse: x(-n)
    return signal[::-1], -n[::-1]

def shift(signal, n, k):
    # shift: x(n-k) means replace n with n-k
    return signal, n + k

# (a) x(n)
xn = x
nn = n

# (b) x(-n)
x_rev, n_rev = reverse(x, n)

# (c) x(-n+2)  => shift x(-n) by +2 in n-axis
x_rev_shift, n_rev_shift = shift(x_rev, n_rev, 2)

# Plotting
fig, axs = plt.subplots(3, 1, figsize=(8, 8), sharex=True)

# x(n)
axs[0].stem(nn, xn, basefmt=" ")
axs[0].set_title("(a) x(n)")
axs[0].grid(True)

# x(-n)
axs[1].stem(n_rev, x_rev, basefmt=" ")
axs[1].set_title("(b) x(-n)")
axs[1].grid(True)

# x(-n+2)
axs[2].stem(n_rev_shift, x_rev_shift, basefmt=" ")
axs[2].set_title("(c) x(-n+2)")
axs[2].grid(True)

axs[-1].set_xlabel("n")
plt.tight_layout()
plt.show()

'''
consider the signal x(n)=[2,2,2,0(n=0),1,2,3,4].signal is from n=-3 to 4. graphically represent x(n),x(-n),x(-n+2)
'''