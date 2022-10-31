def demo_map():
    list_of_powers = list(
        map(
            lambda x: x ** 2,
            [1, 2, 3, 4, 5]
        )
    )
    print(list_of_powers)


def main():
    # print('Hello World!')
    demo_map()


if __name__ == '__main__':
    main()
