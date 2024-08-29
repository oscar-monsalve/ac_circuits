import helpers
import cmath
import numpy as np


def main() -> None:
    z1 = complex(2)
    z2 = complex(3)
    z3 = complex(4)

    zeq_par = helpers.parallel_of(z1, z2, z3)
    zeq_ser = helpers.series_of(z1, z2, z3)

    print(zeq_par)
    print(zeq_ser)


if __name__ == "__main__":
    main()
