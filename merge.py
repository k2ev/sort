import heapq

from insertion import insertion_sort
from utils import my_length


# wrapper
def merge_sort(my_list, left=0, right=None, num_part=2, switch_threshold=0, n_ways=False):
    my_merge_sort_r(my_list, left, right, num_part, switch_threshold, n_ways)
    # my_merge_sort_nr(my_list, left, right, switch_threshold)


# merge sort another style
def my_merge_sort_r(my_list, left=0, right=None, num_part=2, switch_threshold=0, n_ways=False):
    left, right, length = my_length(my_list, left, right)

    if length < switch_threshold or num_part < 2:
        insertion_sort(my_list, left, right)
        return

    if length > 1:
        if num_part == 2 and n_ways is False:
            mid = left + (right - left) // 2
            # print("split call: ", left, mid)
            my_merge_sort_r(my_list, left, mid, num_part, switch_threshold, n_ways)
            #print("split call: ", mid + 1, right)
            my_merge_sort_r(my_list, mid + 1, right, num_part, switch_threshold, n_ways)
            #print("merge call: ", left, right, mid)
            my_merge(my_list, left, right, mid)
        else:
            part_size = max(length // num_part, 1)  # min part_size permitted is 1
            lo = left
            mids = []
            while lo <= right:
                mid = min(lo - 1 + part_size, right)
                if mid > right - part_size:
                    mid = right  # dont append to mids as this is last one
                else:
                    mids.append(mid)
                # print("split call: ", lo, mid)
                my_merge_sort_r(my_list, lo, mid, num_part // 2, switch_threshold, n_ways)
                lo = mid + 1
            #print("merge call: ", left, right, mids)
            my_merge_n_ways(my_list, left, right, mids)

    return


# two ways merge - this is somewhat suboptimal as there is a lot of copying happening here
def my_merge(my_list, left, right, mid):
    length = right - left + 1
    temp = [0] * length
    i, j, pos = left, mid + 1, 0

    while pos < length:
        if i <= mid and j <= right:
            if my_list[i] <= my_list[j]:
                temp[pos] = my_list[i]
                i += 1
            else:
                temp[pos] = my_list[j]
                j += 1
        elif i <= mid:
            temp[pos] = my_list[i]
            i += 1
        elif j <= right:
            temp[pos] = my_list[j]
            j += 1

        pos += 1

    for idx in range(length):
        my_list[left + idx] = temp[idx]

    return


# n ways merge - this is somewhat suboptimal as there is a lot of copying happening here
def my_merge_n_ways(my_list, left, right, partitions):
    length = right - left + 1
    length_partitions = len(partitions)

    if length > 1 and length_partitions > 0:

        partitions_start = list(map(lambda x: x + 1, partitions))
        partitions_start.insert(0, left)
        partitions_end = partitions
        partitions_end.append(right)

        pos = 0
        temp = [0] * length
        pheap = []
        for i, x in enumerate(partitions_start):
            heapq.heappush(pheap, (my_list[x], i))

        while pos < length:
            temp[pos], p_i = heapq.heappop(pheap)
            partitions_start[p_i] += 1
            if partitions_start[p_i] <= partitions_end[p_i]:
                heapq.heappush(pheap, (my_list[partitions_start[p_i]], p_i))
            pos += 1
              
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
                right_p = min(left_p + 2 * width - 1, right)
                my_merge(my_list, left_p, right_p, mid_p)
                left_p += 2*width
            width *= 2

    return

