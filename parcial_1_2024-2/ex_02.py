import numpy as np
import cmath
import sys

sys.path.insert(1, "/home/om/personal/coding/ac_circuits")
import helpers  # nopep8


# Exercise 2
R = 10  # ohm
C = 5 * 10**-3  # F
L = 20 * 10**-3  # H
omega = 2  # rad/s

xc = helpers.reactance_capacitor(C, omega)
xl = helpers.reactance_inductor(L, omega)

vs = cmath.rect(10, np.deg2rad(-105))

zeq = R + xc + xl
i_rec = vs / zeq
i_pol = cmath.polar(i_rec)

print("Exercise 2:")
print(f"    Xc: {xc} Ω")
print(f"    Xl: {xl} Ω")
print(f"    Zeq: {zeq} Ω")
print(f"    I: {i_pol[0]:.5f} A ∠{np.rad2deg(i_pol[1]):.2f}°. ANSWER")
