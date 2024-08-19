import helpers
# import cmath


def main() -> None:
    v = complex(10)

    z1 = complex(100)
    z2 = complex(0, 50)

    v_z1 = helpers.voltage_divider(z1, z2, v)
    v_z22= helpers.voltage_divider(z1, z2, v)

    print(v_z1)
    print(v_z2)


if __name__ == "__main__":
    main()
