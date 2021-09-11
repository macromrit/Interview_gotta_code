def acc_key_val(base_dict: dict, exc_val)->list or None:
    '''the significant goal of this function is to shatter the myth that 
    keys cannot be accessed using values from a mapping in python
    if the module can detect an element from the given dictionary it will return a list consisting all the keys with that value
    else.. obviously will throw None'''

    if exc_val in base_dict.values():
        main_sol = list()
        for i in base_dict:
            if base_dict[i] == exc_val: main_sol.append(i)
            else: pass
        return main_sol
    else: return
