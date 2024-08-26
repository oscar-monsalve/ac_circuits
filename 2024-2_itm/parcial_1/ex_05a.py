import sys
import cmath

sys.path.insert(1, "/home/om/personal/coding/ac_circuits")
import helpers  # nopep8


def main() -> None:
    # Exercise 5 (See page 805-solution-book for an alternative solution)
    z1 = 10-16j
    z2 = 10
    z3 = 10-16j

    za, zb, zc = helpers.star_to_delta(z1, z2, z3)

    x = helpers.parallel_of_two(20, za)
    y = helpers.parallel_of_two(15j, zc)

    zeq = 8 - 12j + helpers.parallel_of_two(x + y, zb)
    print("Solution exercise 5a:")
    print(f"zeq: {zeq} Ω. ANSWER")

    # Bonus
    # voltage source
    amp = 120
    phase_angle = 0
    is_sine = True
    vs_rec = helpers.sinusoid2cos(amp, phase_angle, is_sine)
    vs_pol = cmath.polar(vs_rec)
    helpers.format_pol(vs_pol, "voltage", "Vs")

    i_rec = vs_rec / zeq
    i_pol = cmath.polar(i_rec)
    print("Bonus answer:")
    helpers.format_pol(i_pol, "current", "I")


if __name__ == "__main__":
    main()
