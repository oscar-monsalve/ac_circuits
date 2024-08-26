import helpers
import cmath
import numpy as np


def main() -> None:
    z1 = 10-16j
    z2 = 10
    z3 = 10-16j

    za, zb, zc = helpers.star_to_delta(z1, z2, z3)

    x = helpers.parallel_of_two(20, za)
    y = helpers.parallel_of_two(15j, zc)

    zeq = 8 - 12j + helpers.parallel_of_two(x + y, zb)

    print(f"zeq: {zeq}")


if __name__ == "__main__":
    main()
