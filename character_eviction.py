def character_removed(main: str, chr: str)->str:
    real_str = ''
    for element in main: 
        if element.casefold()!=chr.casefold() : real_str+=element 
        else: pass
    ans = real_str if len(main)>0 else -1
    return ans

print(character_removed("", 'a'))
