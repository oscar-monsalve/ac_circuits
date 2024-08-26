import cmath
import sys

sys.path.insert(1, "/home/om/personal/coding/ac_circuits")
import helpers  # nopep8


def main() -> None:
    # Exercise 1

    # sinusoid 1
    # left hand term
    amp1_1 = 12
    phase_angle1_1 = -10
    is_sine1_1 = True

    # right hand term
    amp1_2 = -1
    phase_angle1_2 = 45
    is_sine1_2 = False

    # sinusoid 2
    amp2 = -10
    phase_angle2 = 50
    is_sine2 = False

    # Solution
    phasor1_1_rec = helpers.sinusoid2cos(amp1_1, phase_angle1_1, is_sine1_1)
    phasor1_2_rec = helpers.sinusoid2cos(amp1_2, phase_angle1_2, is_sine1_2)
    phasor1_sum_rec = helpers.sum_cosine_sinusoids(phasor1_1_rec, phasor1_2_rec)
    phasor1_sum_pol = cmath.polar(phasor1_sum_rec)

    phasor2_rec = helpers.sinusoid2cos(amp2, phase_angle2, is_sine2)
    phasor2_pol = cmath.polar(phasor2_rec)

    # Phase angle
    sinusoids_phase_angle = helpers.sinusoids_phase_angle(phasor1_sum_rec, phasor2_rec)

    # Sum v1 and v2
    sum_rec = helpers.sum_cosine_sinusoids(phasor1_sum_rec, phasor2_rec)
    sum_pol = cmath.polar(sum_rec)

    print("Solution exercise 1b:")
    helpers.format_pol(phasor1_sum_pol, "voltage", "V1")
    helpers.format_pol(phasor2_pol, "voltage", "V2")
    print(f"The angle between v1 and v2 is: {sinusoids_phase_angle}°")
    helpers.lags_or_leads(phasor1_sum_rec, phasor2_rec)
    helpers.format_pol(sum_pol, "voltage", "V1+V2")


if __name__ == "__main__":
    main()
