def demo_map():
    list_of_powers = list(
        map(
            lambda x: x ** 2,
            [1, 2, 3, 4, 5]
        )
    )
    print(list_of_powers)


def demo_zip():
    values1 = list(range(2, 10))
    values2 = list(range(10, 29, 3))
    print(values1)
    print(values2)

    for v1, v2 in zip (values1, values2):
        print(f'{v1=}, {v2=}, sum = ', v1+v2)


def main():
    demo_zip()
    demo_map()

if __name__ == '__main__':
    main()