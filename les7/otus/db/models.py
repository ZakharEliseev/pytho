import sys
from pathlib import Path
from utils import circle_box_area
# from ..utils_v2 import calc_circle


# sys.path.append('/home/ezv/otus1/les7/otus')
sys.path.append(Path(__file__).resolve().parent.parent)


print(__file__)
print(Path(__file__).resolve().parent.parent)
print(circle_box_area({'w': 15, 'h': 10}))
# print(calc_circle({'w': 15, 'h': 10}))
# print(sys.path)