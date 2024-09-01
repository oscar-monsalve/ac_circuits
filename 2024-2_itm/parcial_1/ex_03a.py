import sys
import cmath

sys.path.insert(1, "/home/om/personal/coding/ac_circuits")  # linux
sys.path.insert(1, "D:/OneDrive - Instituto Tecnológico Metropolitano/coding/ac_circuits")  # windows
import helpers  # nopep8


def main() -> None:
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

    print("Solution exercise 3a:")
    print(f"Xc: {xc} Ω")
    print(f"Xl: {xl} Ω")
    print(f"Zeq_rec: {zeq_rec} Ω. ANSWER")
    helpers.format_pol(zeq_pol, "impedance", "Zeq_pol")


if __name__ == "__main__":
    main()
