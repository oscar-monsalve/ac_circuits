import helpers
import numpy as np
import cmath


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

# Exercise 3
R1 = 60  # ohms
R2 = 60  # ohms
C = 12.5 * 10**-6  # F
L = 20 * 10**-3  # H
omega = 200  # rad/s

xc = helpers.reactance_capacitor(C, omega)
xl = helpers.reactance_inductor(L, omega)
zeq = R1 + helpers.parallel_of_two(xl, xc + R2)

print("Exercise 3:")
print(f"    Xc: {xc} Ω")
print(f"    Xl: {xl} Ω")
print(f"    Zeq: {zeq} Ω")
print(f"    I: {i_pol[0]:.5f} A ∠{np.rad2deg(i_pol[1]):.2f}°. ANSWER")
