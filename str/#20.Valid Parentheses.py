def isValid(s):
    stack = []
    pairs = {"(" : ")", "[" : "]", "{":"}"}
    for idx in range(len(s)):
        parenthese = s[idx] 
        if parenthese in pairs.keys(): #만약 오른쪽 짝이 키값에 있다면
            stack.append(parenthese) #stack값에 키를 추가하라
        else:
            if stack == []: #아무것도 없을때 
                return False # 거짓
            else:
                pop = stack.pop() # 오른쪽 괄호와 stack의 마지막 값을 제외한 나머지의 짝이 다를경우 False
                if parenthese != pairs[pop]: #s[1] "(" != "["
                    return False
    if stack == []: #다 끝나고도 stack안에 아무것도 없어야한다
        return True  
s1 = "()"
print(isValid(s1))
