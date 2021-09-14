def anagrams(str1: str, str2: str)->bool:
    return sorted([c for c in str1 if c!=' '])==sorted([v for v in str2 if v!=' '])
