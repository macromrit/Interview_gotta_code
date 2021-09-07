def move_0_left(x:list)->list:
    z = list()
    for i in x:
        if i==0: z.insert(0, i)
        else: z.append(i)
    return z
