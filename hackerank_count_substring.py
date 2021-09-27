def count_substring(string:str, sub_string:str)->int:
    indices = list()
    count = 0
    for index, ele in enumerate(string): 
        if ele==sub_string[0]: indices.append(index)
        else: pass
        count+=1
    ans = sum([1 for x in indices if string[x:x+len(sub_string)]==sub_string]) if [1 for x in indices if string[x:x+len(sub_string)]==sub_string] else 0 
    return ans
