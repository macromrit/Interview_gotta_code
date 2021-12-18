def findDigits(n:int): return len(list(filter(lambda x: True if x>0 and n%x==0 else False, map(int, str(n)))))
