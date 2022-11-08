# from utils import *
# import utils
# from utils_v2 import *
# import utils_v2
# from utils_v2 import calc_circle
# from utils_v2 import calc_circle as calc_circle_v2
# import utils as ut
from utils import (
    calc_circle,
    circle_box_area,
    circle_triangle_area,
    circle_poly_area
)


def main():
    circle_1 = {
        'r': 5,
    }

    # circle_1['area'] = pi * circle_1['r'] ** 2
    # print(circle_1['area'])
    # print(circle_1)

    circle_2 = {
        'r': 15,
    }
    circle_1['area'] = calc_circle(circle_1)
    print(circle_1['area'])
    print(circle_1)

    circle_2['area'] = calc_circle(circle_2)
    print(circle_2['area'])
    print(circle_2)

    print(max(circle_1['area'], circle_2['area']))  # замена масимум и минимум

    box_1 = {
        'w': 10,
        'h': 15,
    }

    box_1['area'] = circle_box_area(box_1)
    print(box_1['area'])
    print(box_1)
    print(max(circle_1['area'], circle_2['area'], box_1['area']))


if __name__ == '__main__':
    main()
