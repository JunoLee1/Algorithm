def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    s = s.strip() #좌우에 빈공간을 제거한다
    str_list = s.split(" ") # " " 을 중심으로 나눈다
        
    return len(str_list[-1]) # 문장 마지막 단어의 철자 수를 구한다
s1 = "Hello World"
print(lengthOfLastWord(s1))


