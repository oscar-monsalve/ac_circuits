import cmath
import numpy as np
import sys

sys.path.insert(1, "/home/om/personal/coding/ac_circuits")  # linux
sys.path.insert(1, "D:/OneDrive - Instituto Tecnológico Metropolitano/coding/ac_circuits")  # windows
import helpers  # nopep8


def main() -> None:
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

    print("Solution exercise 2a:")
    print(f"Xc: {xc} Ω")
    print(f"Xl: {xl} Ω")
    print(f"Zeq: {zeq} Ω")
    helpers.format_pol(i_pol, "current", "I")


if __name__ == "__main__":
    main()
