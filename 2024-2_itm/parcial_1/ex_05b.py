import numpy as np
import cmath
import sys

sys.path.insert(1, "/home/om/personal/coding/ac_circuits")
import helpers  # nopep8


def main() -> None:
    # Exercise 5b
    # Delta impedances
    za = 4j
    zb = -3j
    zc = 8+5j

    # Calculate the wye impedances
    z1, z2, z3 = helpers.delta_to_star(za, zb, zc)

    # Remaining impedances
    R1 = 5
    R2 = 10
    xc = -2j

    zeq_rec = z1 + helpers.parallel_of_two(z2 + R1 + xc, z3 + R2)
    zeq_pol = cmath.polar(zeq_rec)

    # Bonus
    # Voltage source definition
    amp = 120
    phase = 0
    is_sine = True

    vs = helpers.sinusoid2cos(amp, phase, is_sine)

    i_rec = vs / zeq_rec
    i_pol = cmath.polar(i_rec)

    print("Solution exercise 5b:")
    print(f"Zeq_rec: {zeq_rec} Ω. ANSWER")
    helpers.format_pol(zeq_pol, "impedance", "Zeq_pol")
    print("Bonus:")
    helpers.format_pol(i_pol, "current", "I")


if __name__ == "__main__":
    main()
