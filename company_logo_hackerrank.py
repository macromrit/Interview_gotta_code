def christiner(main_str: str)->str:
    if (3<len(main_str)<=10000) and (len(set(main_str))>=3):
        main_dict = dict()
        for i in main_str:
            if i in main_dict.keys(): main_dict[i]+=1
            else: main_dict[i]=1
        
        main_list = list()
        for z in sorted(set(main_dict.values()), reverse=True):
            high_vals = list()
            for i in main_dict.keys():
                if main_dict[i]==z: high_vals.append((i, z))
                else: pass
            main_list.append(high_vals)
        
        final_ans = list()
        for k in main_list:
            x = sorted(k, key=lambda x: x[0])
            final_ans.extend(x)
        
        return (final_ans[0:3], final_ans)
    else: return 

ans = christiner(str(input()).strip())
if ans:
    for element, count in ans[0]: print(element, count)
else: print(-1)
