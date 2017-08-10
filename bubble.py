from utils import my_length


# wrapper
def bubble_sort(my_list, left=0, right=None):
    my_bubble_opt_2(my_list, left, right)


# bubble sort basic with n2 comparisons
def my_bubble_opt_n(my_list, left=0, right=None):
    left, right, length = my_length(my_list, left, right)

    if length > 0:
        # outer loop runs n number of times
        for i in range(left, right+1):
            # inner loop does pairwise swapping - sinking largest to bottom
            for j in range(left, right):
                if my_list[j] > my_list[j+1]:
                    my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return


# optimized version of my_bubble
def my_bubble_opt_1(my_list, left=0, right=None):
    left, right, length = my_length(my_list, left, right)
    if length > 0:
        for i in range(left, right+1):
                # run inner loop few times as we know bottom i-left are already largest
                for j in range(left, right - (i-left)):
                    if my_list[j] > my_list[j+1]:
                        my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return


# optimized version my_bubble. Similar to my_bubble_opt_1 and outer loop stops if elements already sorted
def my_bubble_opt_2(my_list, left=0, right=None):
    left, right, length = my_length(my_list, left, right)

    if length > 0:
        swap_active = True
        for i in range(left, right+1):
            if swap_active is False:
                break  # stop looping if no more swaps
            else:
                swap_active = False
            for j in range(left, right - (i-left)):
                if my_list[j] > my_list[j + 1]:
                    my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
                    swap_active = True
    return