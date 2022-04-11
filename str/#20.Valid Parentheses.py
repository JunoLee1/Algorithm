def isValid(s):
    stack = []
    pairs = {"(" : ")", "[" : "]", "{":"}"}
    for idx in range(len(s)):
        parenthese = s[idx]
        if parenthese in pairs.keys():
            stack.append(parenthese)
        else:
            if stack == []:
                return False
            else:
                pop = stack.pop()
                if parenthese != pairs[pop]:
                    return False
    if stack == []:
        return True


    if stack == []:
        return True    
s1 = "()"
print(isValid(s1))
