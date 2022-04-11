def strStr(haystack, needle):
    if needle in haystack: #만약에 니들이 헤이스택에 있다면
        return haystack.index(needle) #헤이스택안에 있는 니들의 첫 인덱스를 구해준다
    else:
        return -1 #아니면 -1을 해준다
haystack1 = "hello"
needle2 = "ll"
print(strStr(haystack1, needle2))
