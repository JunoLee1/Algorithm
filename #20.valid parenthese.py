def ValidParenthese(s):
    stack  = []
    pairs = {"(" : ")", "[" : "]", "{" : "}"}
    idx = 0
    while idx < len(s):
        parenthese = s[idx]
        if parenthese in pairs.keys():
            stack.append(parenthese)
        else:
            if stack == []:
                return False 
            else:
                pop = stack.pop()
                if parenthese != stack[pop]:
                    return False
        if stack == []:
            return True
str1 = "()"
print(ValidParenthese(str1))
    