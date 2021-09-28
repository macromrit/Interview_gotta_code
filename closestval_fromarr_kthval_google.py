def close_arr(k:list, x:int, y:int)->list:
    """close_arr -> figuring out the nearby values from a list using a value given elements should be sliced as per users desired count

    Args:
        k (list): list with ints
        x (int): value provided for figuring the nearby elements
        y (int): total tally of vicinized elements desired by the user

    Returns:
        list: with elements nearby the given value where len relies on users desirement
    """
    main_sol = list()
    if x in k: k.remove(x)
    else: pass
    for ele in enumerate(k): main_sol.append([ele, abs(x-ele[1])])
    real_ans = [x[0][1] for x in sorted(main_sol, key=lambda c: c[1])]
    return sorted(real_ans[0:y])
