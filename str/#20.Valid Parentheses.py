def isValid(s):
    stack = []
    pairs = {"(" : ")", "[" : "]", "{":"}"}
    for idx in range(len(s)):
        parenthese = s[idx] 
        if parenthese in pairs.keys(): #만약 오른쪽 짝이 키값에 있다면
            stack.append(parenthese) #stack값에 추가하라
        else:
            if stack == []: #오른쪽 키값에 없으면 
                return False # 거짓
            else:
                pop = stack.pop() # 오른쪽 괄호와 stack의 마지막 값을 제외한 나머지의 짝이 다를경우 
                if parenthese != pairs[pop]:
                    return False
    if stack == []:
        return True  
s1 = "()"
print(isValid(s1))
