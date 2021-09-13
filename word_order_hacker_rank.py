def figure_count():
    main_list = list()
    for _ in range(int(input())): main_list.append(str(input()))
    main_dict = dict()
    for i in main_list:
        if i in (main_dict.keys()): main_dict[i]+=1
        else: main_dict[i] = 1
    print(len(set(main_list)))
    for elements in main_dict.items():
        print(elements[1], end=' ')
