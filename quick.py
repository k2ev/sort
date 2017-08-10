from utils import my_length
from insertion import insertion_sort


#wrapper
def quick_sort(my_list, left=0, right=None, switch_threshold=0):
    my_quick_sort_opt_non(my_list, left, right, switch_threshold)


# quick sort
def my_quick_sort_opt_non(my_list, left=0, right=None, switch_threshold=0):
    # initialize length and right index
    left, right, length = my_length(my_list, left, right)

    if length < switch_threshold:
        insertion_sort(my_list, left, right)

    if length > 1:
        left_p, right_p = my_partition(my_list, left, right)
        my_quick_sort_opt_non(my_list, left, left_p - 1)
        my_quick_sort_opt_non(my_list, right_p + 1, right)
    return


# partition for quick sort
def my_partition(my_list, left, right):
    pivot_idx = left + (right - left) // 2  # equivalent of (left+right) // 2 but works better for large numbers
    pivot = my_list[pivot_idx]
    current = left
    # following a dutch parititioning algorithm here.
    # another easier implementation to define left_array and append smaller values to it
    # while append large values to right array. Then stitch and return. However, uses a lot of memory space
    while current <= right:
        if my_list[current] < pivot:
            my_list[current], my_list[left] = my_list[left], my_list[current]
            left, current = left + 1, current + 1
        elif my_list[current] > pivot:
            my_list[current], my_list[right] = my_list[right], my_list[current]
            right -= 1  # dont move pos
        else:
            current += 1

    return left, right