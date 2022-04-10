#2180 count integer with even number.py
def countEven(num):
    count = 0
    for i in range(1,num+1):
        add = 0
        strr = str(i)
        for j in range(len(strr)):
            add += int(strr[j])
            if add % 2 == 0:
                count += 1
    return count
nums = 30
print(countEven(nums))
