def getMoneySpent(keyboards: list, drives: list,  b: int):
    """Budget machine

    Args:
        keyboards (list): arry. of kybrds
        drives (list): arr. of drives
        b (int): max budget
    """
    ans = [(keybrd_prc, drive_prc, keybrd_prc+drive_prc) 
           for keybrd_prc in keyboards
           for drive_prc in drives]#->[(keyboard price, drive price, total price),...]
    main_sol = sorted(filter(lambda x: True if x[2]<=b else False, ans),key=lambda x:x[2], reverse=True)
    return list(main_sol), main_sol[0][2] if main_sol else -1
