from utils import my_length


# wrapper
def insertion_sort(my_list, left=0, right=None):
    my_insertion_opt_1(my_list, left, right)


# insertion sort
def my_insertion_opt_n(my_list, left=0, right=None):
    left, right, length = my_length(my_list, left, right)

    if length > 0:
        for i in range(left, right+1):
            for j in range(i, left, -1):
                if my_list[j - 1] > my_list[j]:
                    my_list[j - 1], my_list[j] = my_list[j], my_list[j - 1]
    return


# insertion sort
def my_insertion_opt_1(my_list, left=0, right=None):
    left, right, length = my_length(my_list, left, right)

    if length > 0:
        for i in range(left, right+1):
            for j in range(i, left, -1):
                if my_list[j - 1] > my_list[j]:
                    my_list[j - 1], my_list[j] = my_list[j], my_list[j - 1]
                else:
                    break
    return