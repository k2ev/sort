import random
from time import time
from bubble import *
from insertion import *
from merge import *
from quick import *
import copy

def main():
    #a = [9,1,5,9,2,5]
    a = random.choices(range(0,100000000), k=10000000)
    a1 = copy.copy(a)
    print("original array")
    # print(a)
    t1 = time()
    quick_sort(a, switch_threshold=8)
    t2 = time()
    print("sorted array time", t2-t1)
    # print(a)
    print("original array")
    # print(a1)
    t3 = time()
    merge_sort(a1, switch_threshold=8)
    t4 = time()
    print("sorted array time", t4 - t3)
    # print(a1)

if __name__ == "__main__":
    main()