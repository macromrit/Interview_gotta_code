def angryProfessor(k: int, a: list)->None:
    """angry professor

    Args:
        k (int): tally of students he wants in min
        a (list): total students with arrived spans 
    """
    ans = len(list(filter(lambda x:True if x<=0 else False, a)))#total ontime pupils
    return 'NO' if ans>=k else 'YES'
