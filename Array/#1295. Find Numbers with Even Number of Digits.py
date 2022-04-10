def findNumbers(num):
    cnt = 0
    for i in num:
        if len(str(i)) %2 == 0:
            cnt += 1
    return cnt
nums = [12,345,2,6,7896]
print(findNumbers(nums))