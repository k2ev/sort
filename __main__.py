import copy
from time import time

from input import gen_input
from merge import merge_sort


def main():
    num = 1000000
    my_a = gen_input(num)
    t1 = time()
    merge_sort(my_a, switch_threshold=8)
    t2 = time()
    print("sorted array time", t2-t1)
    a = copy.copy(my_a)
    # print(a)
    # print("original array")
    # print(a1)
    my_a = gen_input(num)
    t3 = time()
    merge_sort(my_a, num_part=100, switch_threshold=8, n_ways=True)
    t4 = time()
    print("sorted array time", t4 - t3)
    # print(a1)
    print(a == my_a)

if __name__ == "__main__":
    main()