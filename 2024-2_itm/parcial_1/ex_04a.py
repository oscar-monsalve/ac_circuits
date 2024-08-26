import sys
import cmath
import numpy as np

sys.path.insert(1, "/home/om/personal/coding/ac_circuits")
import helpers  # nopep8


def main() -> None:
    # Exercise 4
    vs = cmath.rect(20, np.deg2rad(10))
    z1 = 2
    z2 = 4
    z3 = complex(0, -6)
    z4 = 3
    z5 = complex(0, 4)

    zeq_rec = z1 + helpers.parallel_of_two(z2 + z3, z4 + z5)
    zeq_pol = cmath.polar(zeq_rec)

    i_rec = vs / zeq_rec
    i_pol = cmath.polar(i_rec)

    print("Solution exercise 4a:")
    print(f"Zeq: {zeq_rec}")
    helpers.format_pol(zeq_pol, "impedance", "Zeq")
    helpers.format_pol(i_pol, "current", "I")


if __name__ == "__main__":
    main()
