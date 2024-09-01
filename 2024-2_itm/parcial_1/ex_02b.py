import numpy as np
import cmath
import sys

sys.path.insert(1, "/home/om/personal/coding/ac_circuits")  # linux
sys.path.insert(1, "D:/OneDrive - Instituto Tecnológico Metropolitano/coding/ac_circuits")  # windows
import helpers  # nopep8


def main() -> None:
    # Exercise 2b
    R = 60  # ohm
    C = 10 * 10**-3  # F
    L = 5  # H
    omega = 4  # rad/s

    xc = helpers.reactance_capacitor(C, omega)
    xl = helpers.reactance_inductor(L, omega)

    vs = cmath.rect(20, np.deg2rad(-15))

    zeq = R + helpers.parallel_of_two(xc, xl)
    i_rec = vs / zeq
    i_pol = cmath.polar(i_rec)

    i1_rec, i2_rec = helpers.current_divider(xc, xl, i_rec)
    i2_pol = cmath.polar(i2_rec)

    v0_rec = helpers.voltage_inductor(i2_rec, xl)
    v0_pol = cmath.polar(v0_rec)

    print("Solution exercise 2b:")
    print(f"Xc: {xc} Ω")
    print(f"Xl: {xl} Ω")
    print(f"Zeq: {zeq} Ω")
    helpers.format_pol(i_pol, "current", "I")
    helpers.format_pol(i2_pol, "current", "I2")
    helpers.format_pol(v0_pol, "voltage", "V0")


if __name__ == "__main__":
    main()
