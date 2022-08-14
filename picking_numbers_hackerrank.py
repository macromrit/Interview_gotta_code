def pickingNumbers(a: list)->int:
    a.sort(reverse=True)
    brdr_cnt = len(a)
    ref_str = 1
    ref_cnt = 0
    subby = list()
    subby_sub = list()
    while ref_cnt<brdr_cnt:
        if not subby_sub:
            subby_sub.append(a[ref_cnt])
            ref_cnt+=1
        elif all(map(lambda x: True if x-a[ref_cnt]<=1 else False, subby_sub)):
            subby_sub.append(a[ref_cnt])
            ref_cnt+=1
            if ref_cnt==brdr_cnt:
                subby.append(subby_sub)
                subby_sub = list()
                ref_cnt = ref_str
                ref_str+=1                
        else:
            subby.append(subby_sub)
            subby_sub = list()
            ref_cnt = ref_str
            ref_str+=1            
        
    return max(map(lambda x : len(x), subby))
