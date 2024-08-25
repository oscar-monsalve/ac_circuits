import helpers
import cmath
import numpy as np


def main() -> None:
    # sinusoid 1
    amp1 = 15
    phase_angle1 = 120
    is_sine1 = False

    # sinusoid 2
    amp2 = 52.84
    phase_angle2 = -28.44
    is_sine2 = False

    phasor1_rec = helpers.sinusoid2cos(amp1, phase_angle1, is_sine1)
    phasor1_pol = cmath.polar(phasor1_rec)

    phasor2_rec = helpers.sinusoid2cos(amp2, phase_angle2, is_sine2)
    phasor2_pol = cmath.polar(phasor2_rec)

    sinusoids_phase_angle = helpers.sinusoids_phase_angle(phasor1_rec, phasor2_rec)

    sum = helpers.sum_cosine_sinusoids(phasor1_rec, phasor2_rec)

    helpers.format_pol(phasor1_pol, "voltage")
    helpers.format_pol(phasor2_pol, "impedance")
    print(f"The angle between v1 and v2 is: {sinusoids_phase_angle}°")
    helpers.lags_or_leads(phasor1_rec, phasor2_rec)
    helpers.format_pol(sum, "voltage")


if __name__ == "__main__":
    main()
