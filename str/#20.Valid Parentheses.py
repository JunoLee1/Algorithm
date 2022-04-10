def isValid(s):
    pairs = {"(" :")", "{" : "}", "[" : "]"}
    idx = 0
    stack = []
    while idx < len(s):
        parenthese = s[idx]
        if parenthese in pairs.keys():
            stack.append(parenthese)
        else:
            if stack == []:
                return False 
            else:
                top = stack.pop()
                if parenthese != pairs[top]:
                    return False
            idx += 1
        if stack == []:
            return True
s1 = "()"
print(isValid(s1))
