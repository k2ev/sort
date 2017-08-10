from utils import my_length
from insertion import insertion_sort


# wrapper
def merge_sort(my_list, left=0, right=None, switch_threshold=0):
    # my_merge_sort_r(my_list, left, right, switch_threshold)
    my_merge_sort_nr(my_list, left, right, switch_threshold)


# merge sort another style
def my_merge_sort_r(my_list, left=0, right=None, switch_threshold=0):
    left, right, length = my_length(my_list, left, right)

    if length < switch_threshold:
        insertion_sort(my_list, left, right)

    if length > 1:
        mid = left + (right - left) // 2
        my_merge_sort_r(my_list, left, mid)
        my_merge_sort_r(my_list, mid + 1, right)
        my_merge(my_list, left, mid, right)

    return


def my_merge(my_list, left, mid, right):
    length = right - left + 1
    temp = [0] * length
    i, j, k = left, mid + 1, 0

    while i <= mid and j <= right:
        if my_list[i] <= my_list[j]:
            temp[k] = my_list[i]
            i += 1
        else:
            temp[k] = my_list[j]
            j += 1
        k += 1

    while i <= mid:
        temp[k] = my_list[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = my_list[j]
        j += 1
        k += 1

    for idx in range(length):
        my_list[left + idx] = temp[idx]

    return


# merge sort non recursive
def my_merge_sort_nr(my_list, left=0, right=None, switch_threshold=0):
    left, right, length = my_length(my_list, left, right)
    if length > 1:
        if switch_threshold > 0:
            width = switch_threshold
            left_p = left
            # at the bottom most level, use insert-sort
            while left_p < right:
                right_p = min(left_p+width-1, right)
                insertion_sort(my_list,left_p,right_p)
                left_p += width
        else:
            width = 1

        while width < length:
            left_p = left
            while left_p <= right:
                mid_p = min(left_p + width - 1, right)
                right_p = min(left_p + 2*width - 1, right)
                my_merge(my_list, left_p, mid_p, right_p)
                left_p += 2*width
            width *= 2

    return

