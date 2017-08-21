import copy
import random

# cache of input variable
my_var_cache = None


# generate input
def gen_input(num=1000000, gen_rand=True, u_limit=100000000, use_cache=True):
    global my_var_cache
    if use_cache is True and my_var_cache is not None and len(my_var_cache) == num:
        my_var = copy.copy(my_var_cache)
    else:
        if gen_rand is True:
            my_var = random.choices(range(0, u_limit), k=num)
        else:
            my_var = [27, 24, 23, 26, 24]
        my_var_cache = copy.copy(my_var)
    return my_var
