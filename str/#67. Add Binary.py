def addBinary(a: str, b: str) -> str:
    a_len = len(a)
    b_len = len(b)
    max_len = max(len(a), len(b))
    a = a[::-1]
    b = b[::-1]
    count = 0
    carry = 0
    res = ""
    idx = 0 
    while idx < max_len:
        count = carry
        if idx < a_len and a[idx] == "1":
            count += 1
        if idx < b_len and b[idx] == "1":
            count += 1
        res += str(count%2)
        carry = int(count/2)
        idx += 1
    if carry:
        res += "1"
    return res[::-1]
A = "11"
B = "1"
print(addBinary(A,B))
    
                