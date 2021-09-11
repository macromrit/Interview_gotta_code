def compress_string(val: str)->tuple:
    if not len(val): main = []
    else:
        base = val[0]
        main_sol = list()
        for i in range(0, len(val)):
            if i==0: main_sol.append([1, int(val[i])])
            else:
                if base==val[i]: main_sol[-1][0]+=1
                else:
                    base = val[i]
                    main_sol.append([1, int(val[i])])
        main = main_sol
    return main
for elements in compress_string(str(input())): print(tuple(elements), end=' ')
