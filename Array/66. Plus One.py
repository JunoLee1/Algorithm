def plusOne(digits):
    sum =""
    for i in range(len(digits)):
        str_digits = str(digits[i])
        sum += str_digits
    sum = str(int(sum)+1)
    final_res = []
    final_res[:0] = sum
    return final_res
digit = [4,3,2,1]
print(plusOne(digit))