import cmath
import numpy as np


def parallel_of_two(z1: complex, z2: complex) -> complex:
    """
    Returns the equivalent impedance of two parallel-connected impedances.
    """

    return (z1 * z2) / (z1 + z2)


def current_divider(z1: complex, z2: complex, i_total: complex) -> tuple[complex, complex]:
    """
    Returns a tuple (complex, complex) of the currents flowing through the impedances z1 and z2.
    """
    i_z1 = (z2 / (z1 + z2)) * i_total
    i_z2 = (z1 / (z1 + z2)) * i_total

    return i_z1, i_z2


def voltage_divider(z1: complex, z2: complex, vs: complex) -> tuple[complex, complex]:
    """
    Returns a tuple (complex, comple) of the voltages at the impedances z1 and z2.
    """
    v_z1 = (z1 / (z1 + z2)) * vs
    v_z2 = (z2 / (z1 + z2)) * vs

    return v_z1, v_z2


def star_to_delta(z1: complex, z2: complex, z3: complex) -> tuple[complex, complex, complex]:
    """
    converts from a star to a delta connection.

    Returns the impedances za, zb, zc to form a delta connection.
    """
    za = (z1*z2 + z2*z3 + z3*z1) / z3
    zb = (z1*z2 + z2*z3 + z3*z1) / z2
    zc = (z1*z2 + z2*z3 + z3*z1) / z1

    return za, zb, zc


def delta_to_star(za: complex, zb: complex, zc: complex) -> tuple[complex, complex, complex]:
    """
    converts from a delta to a star connection.

    Returns a tuple of three impedances z1, z2, z3 to form a star connection.
    """
    z1 = (za * zb) / (za + zb + zc)
    z2 = (za * zc) / (za + zb + zc)
    z3 = (zb * zc) / (za + zb + zc)

    return z1, z2, z3


def reactance_capacitor(C: float, omega: float) -> complex:
    """
    Returns the capacitive reactance with a known capacitance C and the rotational frequency Ω.
    """
    return 1 / (omega * C * complex(0, 1))


def reactance_inductor(L: float, omega: float) -> complex:
    """
    Returns the inductive reactance with a known inductance L and the rotational frequency ω.
    """
    return omega * L * complex(0, 1)


def voltage_inductor(i: complex, xl: complex) -> complex:
    """
    Returns the voltage at the inductor.

    Args:
    i: the complex-rectangular current flowing through the inductor.
    xl: the complex-rectangular inductive reactance.
    """
    return i * xl


def voltage_capacitor(i: complex, xc: complex) -> complex:
    """
    Returns the voltage at the capacitor.

    Args:
    i: the complex-rectangular current flowing through the capacitor.
    xc: the complex-rectangular capacitive reactance.
    """
    return i * xc


def format_pol(pol: tuple[float, float], phasor_type: str, name: str) -> None:
    """
    Returns the formatted version a polar number as: "module ∠ angle".

    Args:
    pol: a tuple (module, angle), angle in radians.
    phasor_type: either of the following strings: "impedance", "voltage", or "current".
    name: variable name, e.g., "V1".
    """
    if phasor_type == "impedance":
        return print(f"{name}: {pol[0]} Ω ∠ {np.rad2deg(pol[1])}°")
    if phasor_type == "voltage":
        return print(f"{name}: {pol[0]} V ∠ {np.rad2deg(pol[1])}°")
    if phasor_type == "current":
        return print(f"{name}: {pol[0]} A ∠ {np.rad2deg(pol[1])}°")


def sinusoid2cos(amplitude: float, phase_angle: float, is_sine: bool) -> complex:
    """
    Returns a rectangular complex number equivalent to a cosine form from a sinusoid signal.

    Args:
    amplitude: the sinusoid's amplitud, negative or positive.
    phase angle: the sinusoid's phase angle in degrees.
    is_sine: If True, converts sine to cosine. If False, converts cosine to cosine if the amplitude < 0, or returns the same input if amplitud > 0.
    """
    phase_angle_rad = np.deg2rad(phase_angle)

    if is_sine is True:
        if amplitude < 0:
            phase_angle_rad += (np.pi / 2)
            return cmath.rect(amplitude * -1, phase_angle_rad)
        if amplitude > 0:
            phase_angle_rad -= (np.pi / 2)
            return cmath.rect(amplitude, phase_angle_rad)
    if is_sine is False:
        if amplitude < 0:
            phase_angle_rad -= (np.pi)
            return cmath.rect(amplitude * -1, phase_angle_rad)
        if amplitude > 0:
            return cmath.rect(amplitude, phase_angle_rad)


def sinusoids_phase_angle(s1: complex, s2: complex) -> float:
    """
    Returns the angle in degrees between two complex numbers equivalent to two cosine sinusoids.

    Args:
    s1, s2: rectangular complex numbers equivalent to cosine sinusoids.
    """
    s1_pol = cmath.polar(s1)
    s2_pol = cmath.polar(s2)

    if s1_pol[1] > s2_pol[1]:
        return np.rad2deg(s1_pol[1] - s2_pol[1])
    if s2_pol[1] > s1_pol[1]:
        return np.rad2deg(s2_pol[1] - s1_pol[1])


def lags_or_leads(s1: complex, s2: complex) -> None:
    """
    Determines which complex numbers s1 and s2, equivalent to two cosine sinusoids, lags or leads.

    Args:
    s1, s2: complex numbers in rectangular form.
    """
    s1_pol = cmath.polar(s1)
    s2_pol = cmath.polar(s2)

    if s1_pol[1] > s2_pol[1]:
        phase_angle = np.rad2deg(s1_pol[1] - s2_pol[1])
        return print(f"Sinusoid 1 leads sinusoid 2 in {phase_angle:.2f}°")
    if s2_pol[1] > s1_pol[1]:
        phase_angle = np.rad2deg(s2_pol[1] - s1_pol[1])
        return print(f"Sinusoid 2 leads sinusoid 1 in {phase_angle:.2f}°")


def sum_cosine_sinusoids(s1: complex, s2: complex) -> complex:
    """
    Returns the sum of two complex numbers, equivalent to two cosine sinusoids, in rectangular form.

    Args:
    s1, s2: complex numbers in rectangular form.
    """
    return s1 + s2
