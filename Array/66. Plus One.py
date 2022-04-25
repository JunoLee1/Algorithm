def plusOne(digits):
    sum ="" 
    for i in range(len(digits)):
        str_digits = str(digits[i]) #declare that digit's elements are string
        sum += str_digits #add them in sum
    sum = str(int(sum)+1) #converted sum add 1 
    final_res = [] 
    final_res[:0] = sum #final_res's list is same with sum
    return final_res #return final_res list
digit = [4,3,2,1]
print(plusOne(digit))