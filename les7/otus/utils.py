pi = 3.1415


# @my_decorator
def calc_circle(circle):
    return pi * circle['r'] ** 2


def circle_box_area(box):
    return box['w'] * box['h']


def circle_triangle_area(i):
    pass


def circle_poly_area(box):
    pass

# print(calc_circle(100))
if __name__ == '__main__':
    print(calc_circle(({'r': 1})))
    print(calc_circle(({'r': 1})))

print(__name__)
