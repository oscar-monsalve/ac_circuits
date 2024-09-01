import cmath
import sys

sys.path.insert(1, "/home/om/personal/coding/ac_circuits")  # linux
sys.path.insert(1, "D:/OneDrive - Instituto Tecnológico Metropolitano/coding/ac_circuits")  # windows
import helpers  # nopep8


def main() -> None:
    # Exercise 3b
    R1 = 30  # ohms
    R2 = 50  # ohms
    C = 50 * 10**-6  # F
    L = 0.1  # H
    omega = 200  # rad/s

    xc = helpers.reactance_capacitor(C, omega)
    xl = helpers.reactance_inductor(L, omega)
    zeq_rec = R1 + helpers.parallel_of_two(R2, xc) + xl
    zeq_pol = cmath.polar(zeq_rec)

    print("Solution exercise 3b:")
    print(f"Xc: {xc} Ω")
    print(f"Xl: {xl} Ω")
    print(f"Zeq_rec: {zeq_rec} Ω. ANSWER")
    helpers.format_pol(zeq_pol, "impedance", "Zeq_pol")


if __name__ == "__main__":
    main()
