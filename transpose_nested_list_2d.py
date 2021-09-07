def list_transpose(x: list)->int or list:
    x_legitimate = True
    for i in x:
        if i == x[0]: continue
        else:
            x_legitimate = False
            break
    if x and x_legitimate:
        try:
            sub_list = list()
            for element in range(len(x[0])):
                c = list()
                for z in x:
                    c.append(z[element])
                sub_list.append(c)
        except: sub_list = -1
    else: sub_list = -1
    return sub_list
