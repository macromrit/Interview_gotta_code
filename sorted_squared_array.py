def sorted_squared_array(real_arr: list)->list:
    '''the elements would be sorted by default
    gotta square the elements from the array and resort them just cuz neagative integers
    bug it up without any sorting implementation from the crude array'''
    if real_arr: ans = sorted(list(map(lambda x:x**2, real_arr)))
    else: ans = -1
    return ans
