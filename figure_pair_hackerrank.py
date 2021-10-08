def fig_pair(x:list)->int:
    return sum([x.count(i)//2 for i in {z for z in x}])
