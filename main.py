import helpers
import cmath
import numpy as np


def main() -> None:
    it = cmath.rect(2, np.deg2rad(-20))

    z1 = complex(2, 6)
    z2 = complex(0, 5)

    zeq = helpers.parallel_of_two(z1, z2)

    i1, i2 = helpers.current_divider(z1, z2, it)
    i1_pol = cmath.polar(i1)
    i2_pol = cmath.polar(i2)

    print(f"Zeq: {zeq:.2f} Ω.")
    print(f"I1 -> {i1_pol[0]:.2f} A ∠{np.rad2deg(i1_pol[1]):.2f}°")
    print(f"I2 -> {i2_pol[0]:.2f} A ∠{np.rad2deg(i2_pol[1]):.2f}°")


if __name__ == "__main__":
    main()
