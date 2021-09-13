def fibonacci(terms: int)->int:
    first = 0
    second = 1
    final = 0
    main_list = list()
    main_list.append(first)
    main_list.append(second)
    for i in range(terms-2):
        final = first+second
        first = second
        second = final
        main_list.append(final)
    
    if terms>2: return main_list
    elif terms==2: return [0,1]
    elif terms==1: return [0]
    elif terms==0: return list()
    else: pass

main_ans = list(map(lambda x: x**3, fibonacci(int(input()))))
print(main_ans)
