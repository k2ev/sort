import copy
import random
from time import time

from merge import *


def main():
    # a = [27, 24, 23, 26, 24]
    a = random.choices(range(0, 10000000), k=1000000)
    a1 = copy.copy(a)
    print("original array")
    # print(a)
    t1 = time()
    merge_sort(a, switch_threshold=8)
    t2 = time()
    print("sorted array time", t2-t1)
    print(a)
    print("original array")
    # print(a1)
    t3 = time()
    merge_sort(a1, num_part=3, switch_threshold=8)
    t4 = time()
    print("sorted array time", t4 - t3)
    print(a1)
    print(a == a1)

if __name__ == "__main__":
    main()