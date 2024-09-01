import cmath
import sys

sys.path.insert(1, "/home/om/personal/coding/ac_circuits")  # linux
sys.path.insert(1, "D:/OneDrive - Instituto Tecnológico Metropolitano/coding/ac_circuits")  # windows

import helpers  # nopep8


def main() -> None:
    # Exercise 1

    # sinusoid 1
    amp1 = -15
    phase_angle1 = 30
    is_sine1 = True

    # sinusoid 2
    # left hand term
    amp2_1 = 60
    phase_angle2_1 = -15
    is_sine2_1 = False

    # right hand term
    amp2_2 = 15
    phase_angle2_2 = -50
    is_sine2_2 = True

    # Solution
    phasor1_rec = helpers.sinusoid2cos(amp1, phase_angle1, is_sine1)
    phasor1_pol = cmath.polar(phasor1_rec)

    phasor2_1_rec = helpers.sinusoid2cos(amp2_1, phase_angle2_1, is_sine2_1)
    phasor2_2_rec = helpers.sinusoid2cos(amp2_2, phase_angle2_2, is_sine2_2)

    phasor2_rec = helpers.sum_cosine_sinusoids(phasor2_1_rec, phasor2_2_rec)
    phasor2_pol = cmath.polar(phasor2_rec)

    # Phase angle
    sinusoids_phase_angle = helpers.sinusoids_phase_angle(phasor1_rec, phasor2_rec)

    # Sum v1 and v2
    sum_rec = helpers.sum_cosine_sinusoids(phasor1_rec, phasor2_rec)
    sum_pol = cmath.polar(sum_rec)

    print("Solution exercise 1a:")
    helpers.format_pol(phasor1_pol, "voltage", "V1")
    helpers.format_pol(phasor2_pol, "voltage", "V2")
    print(f"The angle between v1 and v2 is: {sinusoids_phase_angle}°")
    helpers.lags_or_leads(phasor1_rec, phasor2_rec)
    helpers.format_pol(sum_pol, "voltage", "V1+V2")


if __name__ == "__main__":
    main()
