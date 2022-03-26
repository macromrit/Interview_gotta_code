class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)>1:
            key = {x:y for x,y in (list(')('), list('}{'), list(']['))}
            stack = list()
            for i in s:
                if i in key.keys():
                    try:
                        if key[i]==stack[-1]:
                            stack.pop()
                        else:
                            return False
                    except:
                        return False
                else:
                    stack.append(i)

            return False if stack else True
        else:
            return False
