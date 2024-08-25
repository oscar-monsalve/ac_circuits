import sys
import cmath
import numpy as np

sys.path.insert(1, "/home/om/personal/coding/ac_circuits")
import helpers  # nopep8


# Exercise 3
R1 = 60  # ohms
R2 = 60  # ohms
C = 12.5 * 10**-6  # F
L = 20 * 10**-3  # H
omega = 200  # rad/s

xc = helpers.reactance_capacitor(C, omega)
xl = helpers.reactance_inductor(L, omega)
zeq_rec = R1 + helpers.parallel_of_two(xl, xc + R2)
zeq_pol = cmath.polar(zeq_rec)

print("Exercise 3:")
print(f"    Xc: {xc} Ω")
print(f"    Xl: {xl} Ω")
print(f"    Zeq: {zeq_rec:.4f} Ω = {zeq_pol[0]:.4f} Ω ∠{np.rad2deg(zeq_pol[1]):.2f}°. ANSWER")
