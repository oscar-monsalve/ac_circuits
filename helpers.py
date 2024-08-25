
def parallel_of_two(z1: complex, z2: complex) -> complex:
    """
    Returns the equivalent impedance of two parallel-connected impedances.
    """

    return (z1 * z2) / (z1 + z2)


def current_divider(z1: complex, z2: complex, i_total: complex) -> complex:
    """
    Returns the complex current flowing through the impedances z1 and z2.
    """
    i_z1 = (z2 / (z1 + z2)) * i_total
    i_z2 = (z1 / (z1 + z2)) * i_total

    return i_z1, i_z2


def voltage_divider(z1: complex, z2: complex, vs: complex) -> complex:
    """
    Returns the voltage phasor drop at the impedances z1 and z2.
    """
    v_z1 = (z1 / (z1 + z2)) * vs
    v_z2 = (z2 / (z1 + z2)) * vs

    return v_z1, v_z2


def star_to_delta(z1: complex, z2: complex, z3: complex) -> complex:
    """
    converts from a star to a delta connection.

    Returns the impedances za, zb, zc to form a delta connection.
    """
    za = (z1*z2 + z2*z3 + z3*z1) / z3
    zb = (z1*z2 + z2*z3 + z3*z1) / z2
    zc = (z1*z2 + z2*z3 + z3*z1) / z1

    return za, zb, zc


def delta_to_star(za: complex, zb: complex, zc: complex) -> complex:
    """
    converts from a delta to a star connection.

    Returns the impedances z1, z2, z3 to form a star connection.
    """
    z1 = (za * zb) / (za + zb + zc)
    z2 = (za * zc) / (za + zb + zc)
    z3 = (zb * zc) / (za + zb + zc)

    return z1, z2, z3


def reactance_capacitor(C: float, omega: float) -> complex:
    """
    Return the capacitive reactance with a known capacitance C and the rotational frequency Ω.
    """
    return 1 / (omega * C * complex(0, 1))


def reactance_inductor(L: float, omega: float) -> complex:
    """
    Return the inductive reactance with a known inductance L and the rotational frequency ω.
    """
    return omega * L * complex(0, 1)
