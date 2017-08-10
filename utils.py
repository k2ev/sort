def my_length(my_list, left=0, right=None):
    if right is None:
        length = len(my_list) - left
        right = left + length - 1
    else:
        length = right - left + 1

    return left, right, length